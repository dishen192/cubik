from ursina import *
from gui2d import *
import gui3d
import turns
import kociemba

solution = ""
mode = "3D"

# Synchronizes the 2D cube UI with the logical cube state
def cube_update():
    cube = turns.cube
    for btn in buttons:
        btn.cc = cube[btn.face][btn.row][btn.col]
        btn.color = colours[btn.cc][1]
        btn.highlight_color = color.tint(colours[btn.cc][1], 0.2)

# Builds cubestring to be passed on to Kociemba solver
def cubestring_build():
    cube = ""
    face_order = [
        "white",
        "red",
        "green",
        "yellow",
        "orange",
        "blue"
    ]
    for face in face_order:
        for btn in buttons:
            if btn.face == face:
                cube += colours[btn.cc][0]
    return cube


def show_error(msg):

    panel = WindowPanel(
        title='Error',
        content=(
            Text(msg),
        ),
        popup=True
    )

    destroy(panel, delay=2)

def get_solve():
    global solution

    try:
        cube = cubestring_build()
        solution = kociemba.solve(cube)
        solution_label.text="Solution: "+solution

    except ValueError:
        show_error("Invalid Cube State!")

solution_label = Text(text="Solution: ", text_color=color.white, position=Vec2(-0.75, -0.44), scale=1.5)

# Toggles between 2D and 3D cube views
def switch():
    global mode

    if mode == "3D":
        for cube in gui3d.cubes:
            cube.enabled = False
        for btn in buttons:
            btn.enabled = True
        mode = "2D"
        switch_btn.text = "Switch to 3D View"
    elif mode == "2D":
        for cube in gui3d.cubes:
            cube.enabled = True
        for btn in buttons:
            btn.enabled = False
        mode = "3D"
        switch_btn.text = "Switch to 2D View"

# Resets the cube state and recreates both 2D and 3D cube views
def reset():
    # Reset 3D cube
    for cube in gui3d.cubes:
        destroy(cube)
    gui3d.cubes.clear()
    gui3d.create_cube()

    # Reset 2D cube
    turns.solved_cube()
    cube_update()
    for btn in buttons:
        destroy(btn)
    buttons.clear()
    create_flatcube()
    
    for btn in buttons:
        btn.enabled = False

# Creates all UI buttons and labels used by the application
def create_ui():
    global switch_btn
    global scramble
    global get_solve_btn
    global solve_btn
    global reset_btn

    switch_btn = Button(text="Switch to 2D View", color=color.hex("#283942"), position=Vec2(0, 0.45), on_click=switch, highlight_scale=1.05, radius=0.35)
    switch_btn.fit_to_text()

    scramble = Button(text="Scramble!", position=Vec2(0.7, -0.4), color=color.orange, highlight_scale=1.05, highlight_color = color.tint(color.orange, 0.2), radius=0.2)
    scramble.fit_to_text()

    get_solve_btn = Button(text="Get Solution", position=Vec2(0.7, -0.46), color=color.hex("#A5CB71"), highlight_scale=1.05, highlight_color = color.tint(color.hex("#A5CB71"), 0.2), radius=0.1)
    get_solve_btn.fit_to_text()
    get_solve_btn._on_click = get_solve
    
    solve_btn = Button(text="Execute solution", position=Vec2(0.65, 0.34), color=color.hex("#5FAF93"), highlight_scale=1.05, highlight_color = color.tint(color.hex("#5FAF93"), 0.2), radius=0.08)
    solve_btn.fit_to_text()

    reset_btn = Button(text="Reset Cube", position=Vec2(0.7, -0.32), on_click=reset, color="#3E8CFA", highlight_scale=1.05, highlight_color = color.tint(color.hex("#3E8CFA"), 0.2), radius = 0.079)
    reset_btn.fit_to_text()
