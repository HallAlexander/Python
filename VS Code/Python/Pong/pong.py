import tkinter as tk
import random
global paused
paused = False

class Player:
    def __init__(self, canvas, player_status, player_score):
        self.canvas = canvas
        self.move_up = False
        self.move_down = False
        self.player = player_status
        self.score = 0
        self.score_text = player_score
        if self.player == 'p1':
            x, y, width, height = 10, 285, 10, 70
        elif self.player == 'p2':
            x, y, width, height = 480, 285, 10, 70
        self.body = self.canvas.create_rectangle(x, y, x + width, y - height, fill='white')

    def move(self):
        coordinates = self.canvas.coords(self.body)
        if self.move_up and coordinates[1] > 0:
            self.canvas.move(self.body, 0, -7.5)
        if self.move_down and coordinates[3] < 480:
            self.canvas.move(self.body, 0, 7.5)
    
    def update_score(self):
        self.canvas.itemconfig(self.score_text, text=f'{self.score}')
        if self.score == 11 and self.player == 'p1':
            self.canvas.delete(self.body)
            self.canvas.delete(player2.body)
            self.canvas.delete(ball.body)
            self.canvas.delete(self.score_text)
            self.canvas.delete(player2.score_text)
            self.canvas.create_text(250, 250, text='Player 1 wins!', font=('OCR A Extended', 32), fill='white', anchor='center')

        elif self.score == 11 and self.player == 'p2':
            self.canvas.delete(self.body)
            self.canvas.delete(player1.body)
            self.canvas.delete(ball.body)
            self.canvas.delete(self.score_text)
            self.canvas.delete(player1.score_text)
            self.canvas.create_text(250, 250, text='Player 2 wins!', font=('OCR A Extended', 32), fill='white', anchor='center')

class Ball:
    def __init__(self, canvas):
        self.canvas = canvas
        self.moving = False
        self.body = None
        self.dx = 0
        self.dy = 0
        self.create_ball()

    def create_ball(self):
        self.body = self.canvas.create_rectangle(245, 245, 255, 255, fill='white')
        
    def update_position(self):
        if self.moving:
            self.canvas.move(self.body, self.dx, self.dy)
    
    def start(self):
        if not self.moving:
            self.moving = True
            self.dx = random.choice([-2.5, 2.5])

    def collision(self):
        coords = self.canvas.coords(self.body)
        player1_coords = player1.canvas.coords(player1.body)
        player1_centre = (player1_coords[1] + player1_coords[3]) /2
        player1_upper_edge = ((player1_coords[3] - player1_coords[1]) / 4 ) + player1_coords[1]
        player1_lower_edge = ((player1_coords[3] - player1_coords[1]) / 4) + player1_centre
        player2_coords = player2.canvas.coords(player2.body)
        player2_centre = (player2_coords[1] + player2_coords[3]) / 2
        player2_upper_edge = ((player2_coords[3] - player2_coords[1]) / 4) + player2_coords[1]
        player2_lower_edge = ((player2_coords[3] - player2_coords[1]) / 4) + player2_centre

        if coords[1] < 0:
            self.dy = -self.dy
        elif coords[3] >= 480:
            self.dy = - self.dy
        elif coords[0] < 0:
            self.canvas.delete(self.body)
            self.moving = False
            self.dy = 0
            self.create_ball()
            player2.score += 1
            player2.update_score()
        elif coords[2] > 500:
            self.canvas.delete(self.body)
            self.moving = False
            self.dy = 0
            self.create_ball()
            player1.score += 1
            player1.update_score()

        elif coords[1] >= player1_coords[1] and coords[3] <= player1_coords[3] and coords[0] == player1_coords[2]:
            self.dx = -self.dx
            if (coords[1] + 5) < player1_centre and (coords[1] + 5) < player1_upper_edge:
                self.dy = random.choice([-5, -6, -7, -8])
            elif (coords[1] + 5) <= player1_centre and (coords[1] + 5) >= player1_upper_edge:
                self.dy = random.choice([-2, -3, -4, -5])
            elif (coords[1] + 5)> player1_centre and (coords[1] + 5) > player1_lower_edge:
                self.dy = random.choice([5, 6, 7, 8])
            elif (coords[1] + 5) >= player1_centre and (coords[1] + 5) <= player1_lower_edge:
                self.dy = random.choice([2, 3, 4, 5])
        elif coords[1] >= player2_coords[1] and coords[3] <= player2_coords[3] and coords[2] == player2_coords[0]:
            self.dx = -self.dx
            if (coords[3] - 5) < player2_centre and (coords[3] - 5) < player2_upper_edge:
                self.dy = random.choice([-5, -6, -7, -8])
            elif (coords[3] - 5) <= player2_centre and (coords[3] - 5) >= player2_upper_edge:
                self.dy = random.choice([-2, -3, -4, -5])
            elif (coords[3] - 5)> player2_centre and (coords[3] - 5) > player2_lower_edge:
                self.dy = random.choice([5, 6, 7, 8])
            elif (coords[3] - 5) >= player2_centre and (coords[3] - 5) <= player2_lower_edge:
                self.dy = random.choice([2, 3, 4, 5])

def p1_key_press(event):
    if event.keysym == 'w':
        player1.move_up = True

    elif event.keysym == 's':
        player1.move_down = True

def p1_key_release(event):
    if event.keysym == 'w':
        player1.move_up = False

    elif event.keysym =='s':
        player1.move_down = False

def p2_key_press(event):
    if event.keysym == 'Up':
        player2.move_up = True

    elif event.keysym == 'Down':
        player2.move_down = True

def p2_key_release(event):
    if event.keysym == 'Up':
        player2.move_up = False

    elif event.keysym == 'Down':
        player2.move_down = False

def start(event):
    ball.start()

def quit_game(event):
    root.quit()

def pause_game(event):
    global paused
    if not paused:
        paused = True
    else:
        paused = False

def game_loop():
    global paused
    if not paused:
        canvas.itemconfigure(paused_text, state='hidden')
        player1.move()
        player2.move()
        ball.update_position()
        ball.collision()

    else:
        canvas.itemconfigure(paused_text, state='normal')

    root.after(10, game_loop)


root = tk.Tk()
root.title('Pong.exe')

width, height = 500, 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
screen_width_centre = (screen_width / 2) - (width / 2)
screen_height_centre = (screen_height / 2) - (height / 2)
root.geometry('%dx%d+%d+%d' % (width, height, screen_width_centre, screen_height_centre))

frame = tk.Frame(root, bg='white', borderwidth=5, relief='sunken')
frame.pack(padx=10, pady=10)

canvas = tk.Canvas(root, bg='black', width=1280, height=720)
line_rectangles = []
for i in range(25):
    line_rectangles.append(canvas.create_rectangle(247.5, i * 20 + 2.5, 252.5, i * 20 + 12.5, fill='gray'))
canvas.pack()

player1_score = canvas.create_text(200, 50, text='0', font=('OCR A Extended', 64), fill='white', anchor='center')
player2_score = canvas.create_text(300, 50, text='0', font=('OCR A Extended', 64), fill='white', anchor='center')

paused_text = canvas.create_text(250, 250, text='PAUSED', font=('OCR A Extended', 64), fill='white', anchor='center')
canvas.itemconfigure(paused_text, state='hidden')

root.bind('<KeyPress-w>', p1_key_press)
root.bind('<KeyPress-s>', p1_key_press)
root.bind('<KeyRelease-w>', p1_key_release)
root.bind('<KeyRelease-s>', p1_key_release)

root.bind('<KeyPress-Up>', p2_key_press)
root.bind('<KeyPress-Down>', p2_key_press)
root.bind('<KeyRelease-Up>', p2_key_release)
root.bind('<KeyRelease-Down>', p2_key_release)

root.bind('<space>', start)
root.bind('<KeyPress-q>', quit_game)
root.bind('<Return>', pause_game)

player1 = Player(canvas, 'p1', player1_score)
player2 = Player(canvas, 'p2', player2_score)
ball = Ball(canvas)

game_loop()
root.mainloop()