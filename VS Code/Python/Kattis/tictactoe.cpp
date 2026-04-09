#include <bits/stdc++.h>

using namespace std;

// ── Cell encoding ─────────────────────────────────────────────────────────────
// 0='.', 1='x', 2='X', 3='o', 4='O'
// 3 bits per cell × 9 cells = 27 bits for board
// xs(3) XS(2) os(3) OS(2) turn(1) = 11 bits
// Total key: 38 bits, fits in uint64_t

static const int EMPTY=0, XS_=1, XL=2, OS_=3, OL=4;

inline int cell_encode(char c){
    switch(c){ case 'x':return 1; case 'X':return 2;
               case 'o':return 3; case 'O':return 4; default:return 0; }
}
inline char cell_decode(int v){
    switch(v){ case 1:return 'x'; case 2:return 'X';
               case 3:return 'o'; case 4:return 'O'; default:return '.'; }
}

// Board stored as array of 9 ints (3-bit values)
using Board = array<int,9>;

inline uint64_t make_key(const Board& b, int xs, int XS, int os, int OS, int turn){
    uint64_t k=0;
    for(int i=0;i<9;i++) k = k*5 + b[i];
    k = k*5+xs; k = k*3+XS; k = k*5+os; k = k*3+OS; k = k*2+turn;
    return k;
}

// ── Win check ─────────────────────────────────────────────────────────────────
static const int LINES[8][3]={{0,1,2},{3,4,5},{6,7,8},
                               {0,3,6},{1,4,7},{2,5,8},
                               {0,4,8},{2,4,6}};

// Returns 1 if X wins, -1 if O wins, 0 otherwise
inline int check_winner(const Board& b){
    for(auto& ln : LINES){
        int a=b[ln[0]], bv=b[ln[1]], c=b[ln[2]];
        if(a==0) continue;
        // normalise: X-large and X-small both count for X
        int an=(a>=3)?2:1, bn=(bv>=3)?2:1, cn=(c>=3)?2:1;
        // Actually: 1,2 = X-side; 3,4 = O-side
        int as_=(a==1||a==2)?1:(a==3||a==4)?-1:0;
        int bs_=(bv==1||bv==2)?1:(bv==3||bv==4)?-1:0;
        int cs_=(c==1||c==2)?1:(c==3||c==4)?-1:0;
        if(as_!=0 && as_==bs_ && bs_==cs_) return as_;
    }
    return 0;
}

// ── Move generation ───────────────────────────────────────────────────────────
struct State { Board b; int8_t xs,XS,os,OS; };

void get_moves(const Board& b, int xs, int XS, int os, int OS, int turn,
               vector<State>& out){
    out.clear();
    int sm  = (turn==0) ? XS_ : OS_;   // our small piece value
    int lg  = (turn==0) ? XL  : OL;    // our large piece value
    int sc  = (turn==0) ? xs  : os;    // our small count
    int lc  = (turn==0) ? XS  : OS;    // our large count

    auto make = [&](Board nb, int nxs, int nXS, int nos, int nOS){
        out.push_back({nb,(int8_t)nxs,(int8_t)nXS,(int8_t)nos,(int8_t)nOS});
    };

    // 1. Place small from hand on empty
    if(sc > 0){
        for(int i=0;i<9;i++){
            if(b[i]==EMPTY){
                Board nb=b; nb[i]=sm;
                int nxs=xs,nXS=XS,nos=os,nOS=OS;
                if(turn==0) nxs--; else nos--;
                make(nb,nxs,nXS,nos,nOS);
            }
        }
    }

    // 2. Place large from hand
    if(lc > 0){
        for(int i=0;i<9;i++){
            int cell=b[i];
            if(cell==EMPTY){
                Board nb=b; nb[i]=lg;
                int nxs=xs,nXS=XS,nos=os,nOS=OS;
                if(turn==0) nXS--; else nOS--;
                make(nb,nxs,nXS,nos,nOS);
            } else if(cell==XS_||cell==OS_){
                // capture any small — it's removed from game
                Board nb=b; nb[i]=lg;
                int nxs=xs,nXS=XS,nos=os,nOS=OS;
                if(turn==0) nXS--; else nOS--;
                make(nb,nxs,nXS,nos,nOS);
            }
        }
    }

    // 3. Move already-placed large piece onto any small
    for(int src=0;src<9;src++){
        if(b[src]!=lg) continue;
        for(int dst=0;dst<9;dst++){
            if(dst==src) continue;
            int cell=b[dst];
            if(cell==XS_||cell==OS_){
                Board nb=b; nb[src]=EMPTY; nb[dst]=lg;
                // hand counts unchanged (no piece spent, captured small removed)
                make(nb,xs,XS,os,OS);
            }
        }
    }
}

// ── Transposition table ───────────────────────────────────────────────────────
unordered_map<uint64_t,int8_t> TT;

// ── Minimax with alpha-beta ───────────────────────────────────────────────────
// turn: 0=X (maximiser), 1=O (minimiser)
// Returns +1 (X wins) or -1 (O wins)
int minimax(const Board& b, int xs, int XS, int os, int OS, int turn,
            int alpha, int beta){
    // TT lookup
    uint64_t key = make_key(b,xs,XS,os,OS,turn);
    auto it = TT.find(key);
    if(it != TT.end()) return it->second;

    // Terminal: win check
    int w = check_winner(b);
    if(w != 0){ TT[key]=(int8_t)w; return w; }

    // Generate moves
    static thread_local vector<State> moves;
    moves.clear();
    get_moves(b,xs,XS,os,OS,turn,moves);

    if(moves.empty()){
        int r = (turn==0) ? -1 : 1;
        TT[key]=(int8_t)r; return r;
    }

    // Move ordering: put immediate wins first for better pruning
    int next_turn = 1-turn;
    {
        int win_val = (turn==0) ? 1 : -1;
        stable_partition(moves.begin(), moves.end(), [&](const State& m){
            return check_winner(m.b) == win_val;
        });
    }
    if(turn==0){  // maximiser
        int best=-2;
        for(auto& m : moves){
            int s = minimax(m.b,m.xs,m.XS,m.os,m.OS,next_turn,alpha,beta);
            if(s>best) best=s;
            if(best>alpha) alpha=best;
            if(alpha>=beta) break;
        }
        TT[key]=(int8_t)best; return best;
    } else {      // minimiser
        int best=2;
        for(auto& m : moves){
            int s = minimax(m.b,m.xs,m.XS,m.os,m.OS,next_turn,alpha,beta);
            if(s<best) best=s;
            if(best<beta) beta=best;
            if(alpha>=beta) break;
        }
        TT[key]=(int8_t)best; return best;
    }
}

// ── I/O helpers ───────────────────────────────────────────────────────────────
Board read_board(){
    Board b;
    for(int r=0;r<3;r++){
        string row; cin>>row;
        for(int c=0;c<3;c++) b[r*3+c]=cell_encode(row[c]);
    }
    return b;
}

void print_board(const Board& b){
    for(int r=0;r<3;r++){
        for(int c=0;c<3;c++) cout<<cell_decode(b[r*3+c]);
        cout<<'\n';
    }
    cout<<flush;
}

void sync_counts(const Board& b, int& xs, int& XS, int& os, int& OS){
    int cx=0,cX=0,co=0,cO=0;
    for(int i=0;i<9;i++){
        if(b[i]==XS_) cx++;
        else if(b[i]==XL) cX++;
        else if(b[i]==OS_) co++;
        else if(b[i]==OL) cO++;
    }
    xs=4-cx; XS=2-cX; os=4-co; OS=2-cO;
}

// ── compute: pick best move for X ─────────────────────────────────────────────
Board compute(const Board& b, int& xs, int& XS, int& os, int& OS){
    static vector<State> moves;
    get_moves(b,xs,XS,os,OS,0,moves);

    if(moves.empty()) return b;  // no moves, we lose

    int best_score=-2;
    State* best=nullptr;

    for(auto& m : moves){
        int s = minimax(m.b,m.xs,m.XS,m.os,m.OS,1,-2,2);
        if(s > best_score){ best_score=s; best=&m; }
        if(best_score==1) break;  // can't do better
    }

    xs=best->xs; XS=best->XS; os=best->os; OS=best->OS;
    return best->b;
}

// ── Main ──────────────────────────────────────────────────────────────────────
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    TT.reserve(1<<21);

    int xs=4,XS=2,os=4,OS=2;
    Board b; b.fill(EMPTY);

    // First move: we go first on empty board
    b = compute(b,xs,XS,os,OS);
    print_board(b);

    while(true){
        // Read opponent's move
        string first; cin>>first;
        if(first=="Sigur!"||first=="Tap!") return 0;
        string second,third; cin>>second>>third;
        for(int c=0;c<3;c++) b[c]=cell_encode(first[c]);
        for(int c=0;c<3;c++) b[3+c]=cell_encode(second[c]);
        for(int c=0;c<3;c++) b[6+c]=cell_encode(third[c]);

        sync_counts(b,xs,XS,os,OS);

        b = compute(b,xs,XS,os,OS);
        print_board(b);
    }
}