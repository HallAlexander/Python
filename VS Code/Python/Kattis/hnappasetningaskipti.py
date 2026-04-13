tables = {
    'qwerty': '~1234567890-=qwertyuiop[]asdfghjkl;\'zxcvbnm,./',
    'dvorak': '~1234567890[]\',.pyfgcrl/=aoeuidhtns-;qjkxbmwvz',
    'bjarki': '0248613579=-/bjarkigust.,loempdcnvq;[]yzhwfx\'~'
}
frm, to = input().split(' on ')
string = input()
src = tables[frm]
dst = tables[to]
mapping = {s:d for s, d in zip(src, dst)}
out = ''.join(
    c if c == ' ' else mapping.get(c, c) 
    for c in string
)
print(out)