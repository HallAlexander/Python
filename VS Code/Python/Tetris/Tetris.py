import tkinter as tk

def game_loop():

    root.after(100, game_loop)


root = tk.Tk()
root.title('Tetris')

width, height = 100, 100
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
screen_width_centre = (screen_width / 2) - (width / 2)
screen_height_centre = (screen_height / 2) - (height / 2)
root.geometry('%dx%d+%d+%d' % (width, height, screen_width_centre, screen_height_centre))

frame = tk.Frame(root, bg='white', borderwidth=5, relief='sunken')
frame.pack(padx=10, pady=10)

game_loop()
root.mainloop()
