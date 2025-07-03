import tkinter as tk
from tkinter import Button
# ---- Setup base window ----
#Create a maximized window called root, with the title Enigma machine
root = tk.Tk()
root.title('Engima Machine')
root.state('zoomed')

#Setting window size, the size is the same as fullscreen. Commented out code is to have a centered custom window size.

#width, height = 1920, 1080
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
#screen_width_centre = (screen_width / 2) - (width / 2)
#screen_height_centre = (screen_height / 2) - (height / 2)
#root.geometry('%dx%d+%d+%d' % (width, height, screen_width_centre, screen_height_centre))
root.geometry('%dx%d' % (screen_width, screen_height))

#Background colour
bg_colour = '#000026'

#Compile the window
frame = tk.Frame(root, bg='white', borderwidth=5, relief='sunken')
frame.pack(padx=10, pady=10)

canvas = tk.Canvas(root, bg=bg_colour, height=screen_height, width=screen_width)
canvas.pack()
# ---- Base setup end ----



class key:
    def __init__(self, canvas, x, y, radius, label):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.radius = radius
        self.label = label
        self.oval = self.canvas.create_oval(
            x - radius, y - radius,
            x + radius, y + radius,
            fill='lightgray', outline='black'        )
        self.text = self.canvas.create_text(x, y, text=label, font=('elephant', 16, 'bold'))
    
    def set_colour(self, colour):
        """Set the colour of the key."""
        self.canvas.itemconfig(self.oval, fill=colour)
        
class rotor:
    def __init__(self, canvas, x, y, rotor_encryption, turn_over, position):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.rotor_encryption = rotor_encryption
        self.base = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.turn_over = turn_over
        self.position = position
        self.rect_id = None
        self.text_id = None
        
    def draw(self):
        width = 50
        height = 75
        rect_x1 = self.x - width // 2
        rect_y1 = self.y - height // 2
        rect_x2 = self.x + width // 2
        rect_y2 = self.y + height // 2
        
        self.rect_id = self.canvas.create_rectangle(rect_x1, rect_y1, rect_x2, rect_y2, fill='lightgray', outline='black')
        self.text_id = self.canvas.create_text(self.x, self.y, text=self.get_display(), font=('elephant', 16, 'bold'))
        
        
    def increment(self):
        self.position = (self.position + 1) % 26
        self.update_display()
    
    def decrement(self):
        self.position = (self.position - 1) % 26
        self.update_display()
        
    def encode_forward(self, char):
        return self.rotor_encryption[(ord(char) - 65 + self.position) % 26]
    
    def encode_reverse(self, char):
        return self.base[(self.rotor_encryption.index(char) - self.position) % 26]
    
    def get_display(self):
        return chr((self.position % 26) + 65)
    
    def update_display(self):
        self.canvas.itemconfig(self.text_id, text=self.get_display())
        
    def turn(self):
        return self.position == ord(self.turn_over) - ord('A')
    
class reflector:
    def __init__(self, canvas, x, y, reflector_encryption):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.reflector_encryption = reflector_encryption
        
    def encode(self, char):
        return self.reflector_encryption[ord(char) - 65]

class connector:
    def __init__(self, canvas, x, y, label, enigma_ref):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.label = label
        self.enigma = enigma_ref
        self.connection = None
        self.connected_to_label = None
        
        self.rect = self.canvas.create_rectangle(
            x - 25, y - 50, x + 25, y + 50, fill='#cd7f32', outline='white'
        )
        self.text = self.canvas.create_text(
            x, y, text=label, font=('elephant', 12, 'bold'), fill='black'
        )
        
        self.canvas.tag_bind(self.rect, '<Button-1>', self.start_drag)
        self.canvas.tag_bind(self.text, '<Button-1>', self.start_drag)
        self.canvas.tag_bind(self.rect, '<B1-Motion>', self.drag)
        self.canvas.tag_bind(self.text, '<B1-Motion>', self.drag)
        self.canvas.tag_bind(self.rect, '<ButtonRelease-1>', self.stop_drag)
        self.canvas.tag_bind(self.text, '<ButtonRelease-1>', self.stop_drag)
    
        self.drag_data = {'x':0, 'y':0}
        
    def start_drag(self, event):
        self.drag_data['x'] = event.x
        self.drag_data['y'] = event.y
            
    def drag(self, event):
        dx = event.x - self.drag_data['x']
        dy = event.y - self.drag_data['y']
        self.canvas.move(self.rect, dx, dy)
        self.canvas.move(self.text, dx, dy)
        self.drag_data['x'] = event.x
        self.drag_data['y'] = event.y 
        
    def stop_drag(self, event):
        self.x = event.x
        self.y = event.y
        nearest_distance = float('inf')
        nearest_socket = None
        distance_limit = 50
        previous_label = self.connected_to_label
        
        for label, socket in self.enigma.plug_sockets.items():
            sx, sy = socket['coords']
            dx = self.x - sx
            dy = self.y - sy
            dist = abs(dx) + abs(dy)
            if dist < nearest_distance and abs(dx) <= distance_limit and abs(dy) <= distance_limit:
                    nearest_distance = dist
                    nearest_socket = (label, socket)
            
        if nearest_socket and not nearest_socket[1]['connected']:
            label, socket = nearest_socket
            self.connection = True
            socket['connected'] = True
            self.x, self.y = socket['coords']
            self.canvas.coords(self.rect, self.x - 25, self.y - 50, self.x + 25, self.y + 50)
            self.canvas.coords(self.text, self.x, self.y)
            if previous_label and previous_label != label:
                self.enigma.plug_sockets[previous_label]['connected'] = False
            self.connected_to_label = label
            
        else:
            self.connection = False
            if previous_label:
                self.enigma.plug_sockets[previous_label]['connected'] = False
                self.connected_to_label = None  
        
    def snap_to_socket(self, target_label):
        if target_label in self.enigma.plug_sockets:
            socket = self.enigma.plug_sockets[target_label]
            if not socket['connected']:
                self.x, self.y = socket['coords']
                self.canvas.coords(self.rect, self.x - 25, self.y - 50, self.x + 25, self.y + 50)
                self.canvas.coords(self.text, self.x, self.y)
                socket['connected'] = True
                self.connection = True
                self.connected_to_label = target_label        

class Connectors:
    def __init__(self, canvas, x1, y1, x2, y2, label1, label2, enigma_ref):
        self.canvas = canvas
        self.connector1 = connector(canvas, x1, y1, label1, enigma)
        self.connector2 = connector(canvas, x2, y2, label2, enigma)
        self.enigma = enigma_ref
        self.line = None
        self.label1 = label1
        self.label2 = label2
        self.connection_label1 = None
        self.connection_label2 = None
        
        self.update_line()

    def update_line(self):
        if self.connector1.connection and self.connector2.connection:
            self.connection_label1 = self.connector1.connected_to_label
            self.connection_label2 = self.connector2.connected_to_label
            self.enigma.plug_connections[self.connection_label1] = self.connection_label2
            self.enigma.plug_connections[self.connection_label2] = self.connection_label1
            x1, y1 = self.canvas.coords(self.connector1.text)
            x2, y2 = self.canvas.coords(self.connector2.text)
            if self.line:
                self.canvas.coords(self.line, x1, y1, x2, y2)
            else:
                self.line = self.canvas.create_line(x1, y1, x2, y2, fill='white', width=2)
        elif self.line:
            self.canvas.delete(self.line)
            del self.enigma.plug_connections[self.connection_label1]
            del self.enigma.plug_connections[self.connection_label2]
            self.connection_label1 = None
            self.connection_label2 = None
            self.line = None
            
        self.canvas.after(100, self.update_line)
           
class enigma_machine:
    def __init__(self, canvas):
        self.canvas = canvas
        self.master = canvas.master
        self.active_key = None
        self.pressed_key = None
        self.active_num = 0       
        self.indexes = [0, 0, 0]  # rotor1_index, rotor2_index, rotor3_index
        self.key_arr = {}
        self.active_reflector = 0
        self.reflector_buttons = []
        
        self.active_rotor_index = 0
        self.manual_mode_active = False
        self.rotor_highlights = []
        
        self.plug_sockets = {}
        self.plug_connections = {}
        #self.plug_connectors = []
        
    #The lamp/key layout for the machine, three rows and then turn it into a matrix with rows.
        self.row1 = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P']
        self.row2 = ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L']
        self.row3 = ['Z', 'X', 'C', 'V', 'B', 'N', 'M']
        self.rows = [self.row1, self.row2, self.row3]

    def create_keys(self):
    #Create the keys/lamps, with equal spacing.
        key_radius = screen_width // 30
        key_spacing_x = 2.5 * key_radius
        key_spacing_y = 3 * key_radius
        start_y = screen_height // 3
        
        for row_index, row in enumerate(self.rows):
            y = start_y + row_index * key_spacing_y
            row_width = len(row) * key_spacing_x
            start_x = (screen_width - row_width) // 2 + key_spacing_x // 2

            for key_index, key_label in enumerate(row):
                x = start_x + key_index * key_spacing_x
                self.key_arr[key_label] = (key(self.canvas, x, y, key_radius, key_label))

    def key_press(self, event):         
        key = event.keysym.upper()  
        
        if key == 'LEFT':
            if self.manual_mode_active:
                self.active_rotor_index = (self.active_rotor_index + 1) % 3
                self.update_rotor_controls()
            
            else:
                self.manual_mode_active = True
                self.active_rotor_index = 2
                self.update_rotor_controls()
                
        elif key == 'RIGHT':
            if self.manual_mode_active:
                self.active_rotor_index = (self.active_rotor_index - 1) % 3
                self.update_rotor_controls()
                
            else:
                self.manual_mode_active = True
                self.update_rotor_controls()    
        
        elif key == 'UP' and self.manual_mode_active:
            self.rotors[self.active_rotor_index].increment()
            return
        
        elif key == 'DOWN' and self.manual_mode_active:
            self.rotors[self.active_rotor_index].decrement()
            return
        
        elif len(key) == 1 and key.isalpha():
            if self.manual_mode_active:
                self.manual_mode_active = False
                self.update_rotor_controls()
                
            if key and self.active_key != None:
                pass
            
            elif key and key != self.active_key:
                self.active_key = key
                self.pressed_key = key
                self.rotor_logic()
                self.key_arr[self.active_key].set_colour('yellow')
                print(self.active_key)
                       
    def key_release(self, event):
        key = event.char.upper()
        
        if key == self.pressed_key:
            self.key_arr[self.active_key].set_colour('lightgray')
            self.active_key = None
            self.pressed_key = None

    def rotor_setup(self):
        rotor_encryption = {
            'rotor1': 'EKMFLGDQVZNTOWYHXUSPAIBRCJ',
            'turn_over1': 'Q',
            'rotor2': 'AJDKSIRUXBLHWTMCQGZNPYFVOE',
            'turn_over2': 'E',
            'rotor3': 'BDFHJLCPRTXVZNYEIWGAKMUSQO',
            'turn_over3': 'V',
            'rotor4': 'ESOVPZJAYQUIRHXLNFTGKDCMWB',
            'turn_over4': 'J',
            'rotor5': 'VZBRGITYUPSDNHLXAWMJQOFECK',
            'turn_over5': 'Z'
        }
        self.rotor_pool = [
            {'name': 'I', 'encryption':'EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'turnover':'Q'},
            {'name': 'II', 'encryption':'AJDKSIRUXBLHWTMCQGZNPYFVOE', 'turnover':'E'},
            {'name': 'III', 'encryption':'BDFHJLCPRTXVZNYEIWGAKMUSQO', 'turnover':'V'},
            {'name': 'IV', 'encryption':'ESOVPZJAYQUIRHXLNFTGKDCMWB', 'turnover':'J'},
            {'name': 'V', 'encryption':'VZBRGITYUPSDNHLXAWMJQOFECK', 'turnover':'Z'}
        ]
        
        mid_x = screen_width // 2
        y = screen_height // 8
        
        positions = [mid_x - 120, mid_x, mid_x + 120]
        
        self.rotors = [
            rotor(canvas, positions[2], y, self.rotor_pool[0]['encryption'], self.rotor_pool[0]['turnover'], self.indexes[0]),
            rotor(canvas, positions[1], y, self.rotor_pool[1]['encryption'], self.rotor_pool[1]['turnover'], self.indexes[1]),
            rotor(canvas, positions[0], y, self.rotor_pool[2]['encryption'], self.rotor_pool[2]['turnover'], self.indexes[2])
        ]
        used_rotors = [r.rotor_encryption for r in self.rotors]
        self.rotor_labels = []
        self.label_texts = []
        for i, r in enumerate(self.rotor_pool):
            if used_rotors[0] in r['encryption']:
                self.label_texts.append(self.rotor_pool[i]['name'])
            elif used_rotors[1] in r['encryption']:
                self.label_texts.append(self.rotor_pool[i]['name'])
            elif used_rotors[2] in r['encryption']:
                self.label_texts.append(self.rotor_pool[i]['name'])
                
        for i, rotor_obj in enumerate(self.rotors):
            rotor_obj.draw()
            self.rotor_highlights.append(rotor_obj.rect_id)
            self.canvas.tag_bind(rotor_obj.rect_id, '<Button-1>', lambda e, idx=i: self.show_rotor_swap(e, idx))
            
        
        canvas.create_text(screen_width // 2, (screen_height // 8) - 80, text='Rotors', font=('elephant', 32, 'bold'), fill='white')
        canvas.create_text((screen_width // 15) - 10, screen_height - (screen_height // 3) + 5, text='Reflectors', font=('Elephant', 24, 'bold'), fill='white')
        
        for pos, text in zip(positions[::-1], self.label_texts):
            text_id = canvas.create_text(pos, (screen_height // 8) + 50, text='Rotor %s' % text, font=('Elephant', 16, 'bold'), fill='white')
            self.rotor_labels.append(text_id)

        self.switch_button = self.canvas.create_text(
            screen_width // 2, screen_height - 175, text='🔁 Plugboard', fill='white', font=('elephant', 24)
        )
        self.canvas.tag_bind(self.switch_button, '<Button-1>', lambda e: self.plugboard())
             
    def show_rotor_swap(self, event, rotor_index):
        used_rotors = [r.rotor_encryption for r in self.rotors]
        available_rotors = [r for r in self.rotor_pool if r['encryption'] not in used_rotors]
        
        self.close_rotor_popup()
        
        self.rotor_popup = tk.Toplevel(self.master)
        self.rotor_popup.wm_overrideredirect(True)
        self.rotor_popup.configure(bg='lightgray')
        self.rotor_popup.geometry(f'+{event.x_root + 10}+{event.y_root + 10}')
        txt = tk.Label(self.rotor_popup, text='Swap rotors', font=('Elephant', 10, 'bold'), bg='lightgray')
        txt.pack(fill='x', padx=4, pady=(4, 2))
        for i, r in enumerate(available_rotors):
            b = tk.Button(self.rotor_popup, text='Rotor %s' % r['name'], font=('Elephant', 10, 'bold'),
                          command=lambda r=r: self.swap_rotor(rotor_index, r))
            b.pack(fill='x')
            
        self.master.after(100, lambda: self.master.bind_all('<Button-1>', self.check_close_popup, add='+'))
        
    def close_rotor_popup(self):
        if hasattr(self, 'rotor_popup') and self.rotor_popup:
            self.rotor_popup.destroy()
            self.rotor_popup = None
            self.master.unbind_all('<Button-1>')
            
    def check_close_popup(self, event):
        if self.rotor_popup:
            x1 = self.rotor_popup.winfo_rootx()
            y1 = self.rotor_popup.winfo_rooty()
            x2 = x1 + self.rotor_popup.winfo_width()
            y2 = y1 + self.rotor_popup.winfo_height()
            if not (x1 <= event.x_root <= x2 and y1 <= event.y_root <= y2):
                self.close_rotor_popup()
    
    def swap_rotor(self, rotor_index, new_rotor_data):
        self.rotors[rotor_index].rotor_encryption = new_rotor_data['encryption']
        self.rotors[rotor_index].turn_over = new_rotor_data['turnover']
        print(self.rotors[rotor_index].turn_over)
        self.rotors[rotor_index].position = 0
        self.indexes[rotor_index] = 0
        self.label_texts[rotor_index] = new_rotor_data['name']
        self.canvas.itemconfig(self.rotor_labels[rotor_index], text='Rotor %s' % new_rotor_data['name'])
        self.rotors[rotor_index].update_display()
        self.close_rotor_popup()         
        
    def update_rotor_controls(self):
        for i, rect in enumerate(self.rotor_highlights):
            color = '#70adff' if i == self.active_rotor_index else 'lightgray'
            self.canvas.itemconfig(self.rotor_highlights[i], fill=color, outline='black')
        if not self.manual_mode_active:
            for i in range(3):
                self.canvas.itemconfig(self.rotor_highlights[i], fill='lightgray', outline='black')
            
    def reflector_setup(self):
        self.reflector_encryption = [
            'EJMZALYXVBWFCRQUONTSPIKHGD',
            'YRUHQSLDPXNGOKMIEBFZCWVJAT',
            'FVPJIAOYEDRZXWGCTKUQSBNMHL'
        ]
                
        
        
        self.reflectors = [
            reflector(canvas, 0, 0, self.reflector_encryption[0]),
            reflector(canvas, 0, 0, self.reflector_encryption[1]),
            reflector(canvas, 0, 0, self.reflector_encryption[2])
        ]
        
    def create_reflector_buttons(self):
        labels = ['A', 'B', 'C']
        
        x = 40
        start_y = screen_height // 2 - 135
       
        box_width = 100
        box_height = 70
        spacing = 30
        
        
        for i, label in enumerate(labels):
            y = start_y + i * (box_height + spacing)
            
            rect_id = self.canvas.create_rectangle(
                x, y, x + box_width, y + box_height,
                fill='lightgray', outline='black'
            )
            
            text_id = self.canvas.create_text(
                x + box_width // 2, y + box_height // 2,
                text=label, font=('elephant', 16, 'bold')
            )
            
            self.reflector_buttons.append({
                'rect': rect_id,
                'text': text_id,
                'label': label
                })
        self.highlight_selected_reflector()
        self.canvas.bind('<Button-1>', self.reflector_button_click)

    def highlight_selected_reflector(self):
        for i, box in enumerate(self.reflector_buttons):
            color = '#70adff' if i == self.active_reflector else 'lightgray'
            self.canvas.itemconfig(box['rect'], fill=color)
                                
    def reflector_button_click(self, event):
        for i, box in enumerate(self.reflector_buttons):
            x1, y1, x2, y2 = self.canvas.coords(box['rect'])
            if x1 <= event.x <= x2 and y1 <= event.y <= y2:
                self.active_reflector = i
                self.highlight_selected_reflector()
                break
              
    def rotor_logic(self):
        
        if self.active_key in self.plug_connections:
            self.active_key = self.plug_connections[self.active_key]
        self.active_key = self.rotors[0].encode_forward(self.active_key)
        self.active_key = self.rotors[1].encode_forward(self.active_key)
        self.active_key = self.rotors[2].encode_forward(self.active_key)
        
        self.active_key = self.reflectors[self.active_reflector].encode(self.active_key)
        
        self.active_key = self.rotors[2].encode_reverse(self.active_key)
        self.active_key = self.rotors[1].encode_reverse(self.active_key)
        self.active_key = self.rotors[0].encode_reverse(self.active_key)
        
        if self.active_key in self.plug_connections:
            self.active_key = self.plug_connections[self.active_key]
                        
        if self.rotors[1].turn():
            self.rotors[2].increment()
            self.indexes[2] = (self.indexes[2] + 1) % 26
        if self.rotors[0].turn():
            self.rotors[1].increment()
            self.indexes[1] = (self.indexes[1] + 1) % 26
        self.rotors[0].increment()
        self.indexes[0] = (self.indexes[0]) % 26
        
    
    
    save_state = {}
    
    def plugboard_button_click(self, event, x1, x2, y1, y2, plug_window):
        if x1 <= event.x <= x2 and y1 <= event.y <= y2:
            self.save_plugboard_state()
            plug_window.destroy()
    
    def save_plugboard_state(self):
        for p in self.plug_sockets:
            if self.plug_sockets[p]['connected'] == True:
                self.save_state[p] = self.plug_sockets[p]['coords']    
                
    def plugboard_plugs(self, canvas):
        plug_width = 60
        plug_height = 120
        hole_radius = 10
        plug_spacing_x = 160
        plug_spacing_y = 200
        start_y = screen_height // 4
        
        self.plug_sockets = {}
        
        for row_index, row in enumerate(self.rows):
            y = start_y + row_index * plug_spacing_y
            row_width = len(row) * plug_spacing_x
            start_x = (screen_width - row_width) // 2 + plug_spacing_x // 2

            for i, label in enumerate(row):
                x = start_x + i * plug_spacing_x
                
                rect = canvas.create_rectangle(
                    x - plug_width // 2, y - plug_height // 2,
                    x + plug_width // 2, y + plug_height // 2,
                    fill='lightgray', outline='black'
                )
                hole_offset = 30
                for dy in [-hole_offset, hole_offset]:
                    canvas.create_oval(
                        x - hole_radius, y + dy - hole_radius,
                        x + hole_radius, y + dy + hole_radius,
                        fill='black'
                    )

                
                text = canvas.create_text(x, y + plug_height // 2 + 25, text=label, font=('elephant', 24, 'bold'), fill='white')
                self.plug_sockets[label] = {
                    'rect': rect,
                    'text': text,
                    'coords': (x, y),
                    'connected': False
                }

    def plugboard(self):
        plug_window = tk.Toplevel(self.master)
        canvas = tk.Canvas(plug_window, bg=bg_colour, height=screen_height, width=screen_width)
        canvas.pack()
        plug_window.title('Plugboard')
        plug_window.state('zoomed')
        plug_window.configure(bg=bg_colour)
        plug_window.grab_set()

        
        
        
        canvas.create_text(screen_width // 2, 50, text='Plugboard', font=('elephant', 32, 'bold'), fill='white')
        
        close_button = canvas.create_rectangle(screen_width // 2 - 160, screen_height - 140, screen_width // 2 + 160, screen_height - 90, fill=bg_colour, outline='white')
        canvas.create_text(screen_width // 2, screen_height - 115, text='↑ Close plugboard', font=('elephant', 24, 'bold'), fill='white')

        x1, y1, x2, y2 = canvas.coords(close_button)
        canvas.bind('<Button-1>', lambda event: self.plugboard_button_click(event, x1, x2, y1, y2, plug_window))

        self.plugboard_plugs(canvas)
        
        
        pair_labels = [('1A', '1B'), ('2A', '2B'), ('3A', '3B'), ('4A', '4B'), ('5A', '5B'),
               ('6A', '6B'), ('7A', '7B'), ('8A', '8B'), ('9A', '9B'), ('10A', '10B')]
        self.plug_connectors = []
        start_x = (screen_width // 11) - 25
        start_y1, start_y2 = screen_height // 3, screen_height - (screen_height // 3)
        spacing_x = (screen_width // 9) - 25
        
        #self.plug_connectors.append(Connectors(canvas, screen_width // 2 - 200, screen_height // 2, screen_width // 2 + 200, screen_height // 2, '1A', '1B', self))
        #self.plug_connectors.append(Connectors(canvas, screen_width // 2 - 500, screen_height // 2, screen_width // 2 + 300, screen_height // 2, '2A', '2B', self))
        for i, (label1, label2) in enumerate(pair_labels):
                x = start_x + i * spacing_x
                pair = Connectors(canvas, x, start_y1, x, start_y2, label1, label2, self)
                self.plug_connectors.append(pair)
        j = 0
        for i, socket_label in enumerate(self.plug_connections.keys()):
            if i % 2 == 1:
                continue
            label1 = socket_label
            label2 = self.plug_connections[socket_label]
            
            #for connector_pair in self.plug_connectors:
                #print(connector_pair)
            self.plug_connectors[j].connector1.snap_to_socket(self.plug_connections[label1])
            self.plug_connectors[j].connector2.snap_to_socket(self.plug_connections[label2])
            j += 1
                        
        

#run the functions
enigma = enigma_machine(canvas)
enigma.create_keys()
enigma.rotor_setup()
enigma.reflector_setup()
enigma.create_reflector_buttons()
#Enable key presses and reset of the lamps
root.bind('<KeyPress>', enigma.key_press)
root.bind('<KeyRelease>', enigma.key_release)
#Run the loop which creates the window.
root.mainloop()
