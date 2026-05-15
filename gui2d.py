from ursina import *

# face_name : [cube notation, display color, x position, y position]
colours = {
    "white": ["U", color.white, 0, 0.215],
    "red": ["R", color.hex("#D14040"), 0.215, 0],
    "green": ["F", color.green, 0, 0],
    "yellow": ["D", color.yellow, 0, -0.215],
    "orange": ["L", color.orange, -0.215, 0],
    "blue": ["B", color.azure, 0.430, 0]
}

buttons = []
colour_order = list(colours.keys())

# Function for creating a face of the cube
def create_face(face, x, y):
    start_x = x
    
    for i in range(3):
        for j in range(3):
            btn = Button(color=colours[face][1], position=Vec2(x-0.15, y+0.1), scale=0.065, radius=0.15)
            btn._on_click=lambda b=btn: btn_on_click(b)
            btn.face = face
            btn.cc = face
            btn.row = i
            btn.col = j

            if i==1 and j==1:
                btn._on_click=None

            buttons.append(btn)
            x+=0.07
        x=start_x
        y-=0.07

# Create all faces of the cubes by referencing the colours dictionary
def create_flatcube():
    for face in colours:
        create_face(face, colours[face][2], colours[face][3])

# Command for changing colours on click
def btn_on_click(btn):
    btn.cc = next_colour(btn.cc)
    btn.color = colours[btn.cc][1]
    btn.highlight_color = color.tint(colours[btn.cc][1], 0.2)

# Helper command for btn_on_click()
def next_colour(current):
    global colour_order

    return colour_order[
        (colour_order.index(current) + 1)
        % len(colour_order)
    ]
