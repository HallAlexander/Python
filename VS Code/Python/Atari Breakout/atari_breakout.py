import tkinter as tk
import random

class Player:
    def __init__(self, canvas):
        self.canvas = canvas
        self.move_left = False
        self.move_right = False
        x, y, width, height  = 500, 690, 150, 10
        self.body = self.canvas.create_rectangle(x, y, x + width, y - height, fill='white')
    
    def move(self):
        coordinates = self.canvas.coords(self.body)
        if self.move_left and coordinates[0] > 0:
            self.canvas.move(self.body, -10, 0)
        if self.move_right and coordinates[2] < 1280:
            self.canvas.move(self.body, 10, 0)

class Block:
    def __init__(self, canvas, colour, level):
        self.canvas = canvas
        self.colour = colour
        self.level = level
        self.position = (1.5, (30 * self.level) + 5)
        self.blocks = []
        if self.level % 2 == 1:
            self.blocks.append(self.canvas.create_rectangle(self.position[0], self.position[1], self.position[0] + 40, self.position[1] + 25, fill=self.colour))
            x = self.position[0] + 45
            y = self.position[1]
            self.position = (x, y)
        while(self.position[0] + 75 < 1280):
            self.create_block(self.position[0], self.position[1])
            x = self.position[0] + 80
            y = self.position[1]
            self.position = (x, y)
        if self.level % 2 == 1:
            self.blocks.append(self.canvas.create_rectangle(self.position[0], self.position[1], self.position[0] + 35, self.position[1] + 25, fill=self.colour))

    def create_block(self, x, y):
        self.blocks.append(self.canvas.create_rectangle(x, y, x + 75, y + 25, fill=self.colour))

    def check_collision(self, ball_coords):
        for block in self.blocks:
            coords = self.canvas.coords(block)
            if (ball_coords[0] < coords[2] and ball_coords[2] > coords[0] and 
                ball_coords[1] < coords[3] and ball_coords[3] > coords[1]):
                self.canvas.delete(block)
                self.blocks.remove(block)
                if random.random() < 0.25:
                    lvl_up_orbs.append(lvl_up_orb(canvas, coords))
                return True
        return False

class Ball:
    def __init__(self, canvas, lives_text):
        self.canvas = canvas
        self.moving = False
        self.body = None
        self.dx = 0
        self.dy = -10
        self.lives_text = lives_text
        self.lives = 3
        self.create_ball()
        

    def create_ball(self):
        coords = player.canvas.coords(player.body)
        player_centre = (coords[0] + coords[2]) / 2
        self.body = self.canvas.create_oval(player_centre - 10, 660, player_centre + 10, 680, fill='white')

    def update_position(self):
        if not self.moving:
            coords = player.canvas.coords(player.body)
            player_centre = (coords[0] + coords[2]) / 2
            ball_coords = self.canvas.coords(self.body)
            dx = player_centre - (ball_coords[0] + ball_coords[2]) / 2
            self.canvas.move(self.body, dx, 0)
        else:
            self.canvas.move(self.body, self.dx, self.dy)
    
    def shoot(self):
        if not self.moving:
            self.moving = True
            self.dx = random.choice([-5, 5])

    def collision(self):
        coords = self.canvas.coords(self.body)
        player_coords = player.canvas.coords(player.body)
        player_centre = (player_coords[0] + player_coords[2]) / 2
        if coords[0] < 0:
            self.dx = -self.dx
        elif coords[2] > 1280:
            self.dx = -self.dx
        elif coords[1] < 0:
            self.dy = -self.dy
        elif coords[1] > 720:
            self.lives -= 1
            self.update_lives()
            if self.lives == 0:
                print('Game Over!')
                root.quit()         #Make it so the window says game over and you press q to quit
            self.canvas.delete(self.body)
            self.moving = False
            self.create_ball()
        elif coords[0] >= player_coords[0] and coords[2] <= player_coords[2] and coords[3] > player_coords[1]:
            self.dy = -self.dy
            if coords[0] < player_centre and self.dx > 0:
                self.dx = -self.dx
            if coords[0] > player_centre and self.dx < 0:
                self.dx = -self.dx    
        for block in all_blocks:
            if block.check_collision(coords):
                self.dy = -self.dy
                return
    
    def update_lives(self):
        self.canvas.itemconfig(self.lives_text, text=f'Lives: {self.lives}')

class lvl_up_orb:
    def __init__(self, canvas, block_coords):
        self.canvas = canvas
        block_centre = (block_coords[0] + block_coords[2]) / 2
        self.body = self.canvas.create_oval(block_centre - 10, block_coords[3], block_centre + 10, block_coords[3] + 20, fill='white')
        self.colours = ['blue', 'red', 'lime', '#7F00FF', '#FF00FF', 'yellow', 'orange', 'white', '#C8DC9A', 'cyan']
        self.colour_index = 0
        self.change_colour()

    def move(self):
        self.canvas.move(self.body, 0, 5)
        self.collision()
    
    def collision(self):
        coords = self.canvas.coords(self.body)
        player_coords = player.canvas.coords(player.body)
        if (coords[0] <= player_coords[2] and coords[2] >= player_coords[0] and coords[3] >= player_coords[1] and coords[1] <= player_coords[3]):
            level_up(None)
            self.canvas.delete(self.body)
            lvl_up_orbs.remove(self)

    def change_colour(self):
        new_colour = self.colours[self.colour_index]
        self.canvas.itemconfig(self.body, fill=new_colour)
        self.colour_index = (self.colour_index + 1) % len(self.colours)
        self.canvas.after(100, self.change_colour)

def key_press(event):
    if event.keysym in ['Left', 'a']:
        player.move_left = True

    elif event.keysym in ['Right', 'd']:
        player.move_right = True

def key_release(event):
    if event.keysym in ['Left', 'a']:
        player.move_left = False

    elif event.keysym in ['Right', 'd']:
        player.move_right = False

def level_up(event):
    coords = player.canvas.coords(player.body)
    centre = (coords[0] + coords[2]) / 2
    player.canvas.scale(player.body, centre, 0, 1.2, 1)

def shoot(event):
    ball.shoot()

def quit_game(event):
    root.quit()

def game_loop():
    player.move()
    ball.update_position()
    ball.collision()
    for orb in lvl_up_orbs:
        orb.move()
    root.after(20, game_loop)

root = tk.Tk()
root.title('Atari Breakout.exe')

width, height = 1280, 720
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
screen_width_centre = (screen_width / 2) - (width / 2)
screen_height_centre = (screen_height / 2) - (height / 2)
root.geometry('%dx%d+%d+%d' % (width, height, screen_width_centre, screen_height_centre))

frame = tk.Frame(root, bg='white', borderwidth=5, relief='sunken')
frame.pack(padx=10, pady=10)

canvas = tk.Canvas(root, bg='black', width=1280, height=720)
canvas.pack()

lives_text = canvas.create_text(100, 650, text='Lives: 3', font='Arial, 28', fill='white', anchor='center')

root.bind('<KeyPress-Left>', key_press)
root.bind('<KeyPress-Right>', key_press)
root.bind('<KeyPress-a>', key_press)
root.bind('<KeyPress-d>', key_press)
root.bind('<KeyRelease-Left>', key_release)
root.bind('<KeyRelease-Right>', key_release)
root.bind('<KeyRelease-a>', key_release)
root.bind('<KeyRelease-d>', key_release)
root.bind('<KeyPress-q>', quit_game)
root.bind('<space>', shoot)

player = Player(canvas)

all_blocks = [
    Block(canvas, 'red', 0),
    Block(canvas, 'orange', 1),
    Block(canvas, 'yellow', 2),
    Block(canvas, 'lime', 3),
    Block(canvas, 'blue', 4),
    Block(canvas, 'purple', 5),
    Block(canvas, 'cyan', 6)
]
ball = Ball(canvas, lives_text)
lvl_up_orbs = []

game_loop()

root.mainloop()
