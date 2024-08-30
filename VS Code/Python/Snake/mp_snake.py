import tkinter as tk

class Snake:
    def __init__(self, canvas, snake_colour, player_status, score_text):
        self.canvas = canvas
        self.player_status = player_status
        if self.player_status == 'p1':
            self.body = [(250, 245), (240, 250), (230, 250)]
            self.direction = 'Left'
        else:
            self.body = [(250, 255), (240, 250), (230, 250)]
            self.direction = 'Right'
        self.snake_colour = snake_colour
        self.squares = []
        self.score = 0
        self.score_text = score_text
        for x, y in self.body:
            square = canvas.create_rectangle(x, y, x + 10, y + 10, fill=self.snake_colour)
            self.squares.append(square)


    def move(self):
        head_x, head_y = self.body[0]
        if self.direction == 'Up':
            head_y -= 10
        elif self.direction == 'Down':
            head_y += 10
        elif self.direction == 'Left':
            head_x -= 10
        elif self.direction == 'Right':
            head_x += 10
        
        new_head = (head_x, head_y)
        self.body = [new_head] + self.body[:-1]

        for square, (x, y) in zip(self.squares, self.body):
            self.canvas.coords(square, x, y, x + 10, y + 10)

    def grow(self):
        tail_x, tail_y = self.body[-1]
        if self.direction == 'Up':
            tail_y += 10
        elif self.direction == 'Down':
            tail_y -= 10
        elif self.direction == 'Left':
            tail_x += 10
        elif self.direction == 'Right':
            tail_x -= 10

        new_tail = (tail_x, tail_y)
        self.body.append(new_tail)
        square = self.canvas.create_rectangle(tail_x, tail_y, tail_x + 10, tail_y + 10, fill=self.snake_colour)
        self.squares.append(square)
        
        self.score += 1
        self.update_score()
    
    def update_score(self):
        self.canvas.itemconfig(self.score_text, text=f'Score: {self.score}')

    def destroy(self):
        for square in self.squares:
            self.canvas.delete(square)

class Food:
    def __init__(self, canvas, bg_colour):
        self.canvas = canvas
        self.bg_colour = bg_colour
        self.position = (100, 100)
        self.food_parts = []
        self.create_food(self.position[0], self.position[1])

    def create_food(self, x, y):
        size = 10/6
        self.food_parts.append(self.canvas.create_rectangle(x - size, y - size, x + size, y + size, fill=self.bg_colour, outline=self.bg_colour)) #center
        self.food_parts.append(self.canvas.create_rectangle(x - 3 * size, y - size, x - size, y + size, fill="red", outline="red")) #left
        self.food_parts.append(self.canvas.create_rectangle(x + size, y - size, x + 3 * size, y + size, fill="red", outline="red")) #right
        self.food_parts.append(self.canvas.create_rectangle(x - size, y - 3 * size, x + size, y - size, fill="red", outline="red")) #top
        self.food_parts.append(self.canvas.create_rectangle(x - size, y + size, x + size, y + 3 * size, fill="red", outline="red")) #bottom

    def relocate(self):
        import random
        x = random.randint(5, 45) * 10 + 5
        y = random.randint(5, 45) * 10 + 5
        self.position = (x, y)

        for part in self.food_parts:
            self.canvas.delete(part)
        self.food_parts = []
        self.create_food(x, y)
    
    def destroy(self):
        for part in self.food_parts:
            self.canvas.delete(part)


def p1_change_direction(event):
    if event.keysym == 'w' and snake1.direction != 'Down':
        snake1.direction = 'Up'
    elif event.keysym == 's' and snake1.direction != 'Up':
        snake1.direction = 'Down'
    elif event.keysym == 'a' and snake1.direction != 'Right':
        snake1.direction = 'Left'
    elif event.keysym == 'd' and snake1.direction != 'Left':
        snake1.direction = 'Right'

def p2_change_direction(event):
    if event.keysym == 'Up' and snake2.direction != 'Down':
        snake2.direction = 'Up'
    elif event.keysym == 'Down' and snake2.direction != 'Up':
        snake2.direction = 'Down'
    elif event.keysym == 'Left' and snake2.direction != 'Right':
        snake2.direction = 'Left'
    elif event.keysym == 'Right' and snake2.direction != 'Left':
        snake2.direction = 'Right'

def debug1(event):
    food.relocate()
    snake1.grow()

def debug2(event):
    food.relocate()
    snake2.grow()
    
def quit_game(event):
    root.quit()

def game_loop():
    snake1.move()
    snake2.move()

    head1_x, head1_y = snake1.body[0]
    food_x, food_y = food.position
    if abs(head1_x - food_x) < 10 and abs(head1_y - food_y) < 10:
        food.relocate()
        snake1.grow()
    
    head2_x, head2_y = snake2.body[0]
    food_x, food_y = food.position
    if abs(head2_x - food_x) < 10 and abs(head2_y - food_y) < 10:
        food.relocate()
        snake2.grow()
  

    head1_x, head1_y = snake1.body[0]
    if head1_x < 0 or head1_x >= 500 or head1_y < 0 or head1_y >= 500:
        snake1.destroy()
        snake2.destroy()
        food.destroy()
        canvas.create_text(250, 230, text='Game Over!', font=('Arial', 32), fill='white', anchor='center')
        canvas.create_text(250, 260, text='Player 2 won with the score: {}'.format(snake2.score), font=('Arial', 14), fill=snake2_colour, anchor='center')
        canvas.delete(score_text1)
        canvas.delete(score_text2)

    if len(snake1.body) != len(set(snake1.body)):
        snake1.destroy()
        snake2.destroy()
        food.destroy()
        canvas.create_text(250, 230, text='Game Over!', font=('Arial', 32), fill='white', anchor='center')
        canvas.create_text(250, 260, text='Player 2 won with the score: {}'.format(snake2.score), font=('Arial', 14), fill=snake2_colour, anchor='center')
        canvas.delete(score_text1)
        canvas.delete(score_text2)

    head2_x, head2_y = snake2.body[0]
    if head2_x < 0 or head2_x >= 500 or head2_y < 0 or head2_y >= 500:
        snake1.destroy()
        snake2.destroy()
        food.destroy()
        canvas.create_text(250, 230, text='Game Over!', font=('Arial', 32), fill='white', anchor='center')
        canvas.create_text(250, 260, text='Player 1 won with the score: {}'.format(snake1.score), font=('Arial', 14), fill=snake1_colour, anchor='center')
        canvas.delete(score_text1)
        canvas.delete(score_text2)

    if len(snake2.body) != len(set(snake2.body)):
        snake1.destroy()
        snake2.destroy()
        food.destroy()
        canvas.create_text(250, 230, text='Game Over!', font=('Arial', 32), fill='white', anchor='center')
        canvas.create_text(250, 260, text='Player 1 won with the score: {}'.format(snake1.score), font=('Arial', 14), fill=snake1_colour, anchor='center')
        canvas.delete(score_text1)
        canvas.delete(score_text2)

    if snake1.score > snake2.score:
        canvas.itemconfig(score_text_leader, text=f'Leader: Player 1',)
    elif snake1.score < snake2.score:
        canvas.itemconfig(score_text_leader, text=f'Leader: Player 2')
        
    
    root.after(75, game_loop)

root = tk.Tk()
root.title('Snake.exe')

width, height = 500, 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
screen_width_centre = (screen_width / 2) - (width / 2)
screen_height_centre = (screen_height / 2) - (height / 2)
root.geometry('%dx%d+%d+%d' % (width, height, screen_width_centre, screen_height_centre))

bg_colour = '#000026'
snake1_colour = '#9FFE36'
snake2_colour = 'cyan'

frame = tk.Frame(root, bg='white', borderwidth=5, relief='sunken')
frame.pack(padx=10, pady=10)

canvas = tk.Canvas(root, bg=bg_colour, height=500, width=500)
canvas.pack()

score_text1 = canvas.create_text(50, 20, text='Score: 0', font=('Arial', 14), fill=snake1_colour, anchor='center')
score_text2 = canvas.create_text(450, 20, text='Score: 0', font=('Arial', 14), fill=snake2_colour, anchor='center')
score_text_leader = canvas.create_text(250, 20, text='Leader: NaN', font=('Arial, 14'), fill='white', anchor='center')

root.bind('<KeyPress-w>', p1_change_direction)
root.bind('<KeyPress-s>', p1_change_direction)
root.bind('<KeyPress-a>', p1_change_direction)
root.bind('<KeyPress-d>', p1_change_direction)
root.bind('<KeyPress-Up>', p2_change_direction)
root.bind('<KeyPress-Down>', p2_change_direction)
root.bind('<KeyPress-Left>', p2_change_direction)
root.bind('<KeyPress-Right>', p2_change_direction)
root.bind('<KeyPress-q>', quit_game)
root.bind('<space>', debug1)
root.bind('<Return>', debug2)

snake1 = Snake(canvas, snake1_colour, 'p1', score_text1)
snake2 = Snake(canvas, snake2_colour, 'p2', score_text2)
food = Food(canvas, bg_colour)

game_loop()

root.mainloop()
