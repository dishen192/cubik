from ursina import *
import gui3d
import turns
import shared_logic

is_rotating = False
key_input = False
rotation_helper = Entity()

rotation_map = {
    "U": Vec3(0, 1, 0),
    "D": Vec3(0, -1, 0),
    "L": Vec3(-1, 0, 0),
    "R": Vec3(1, 0, 0),
    "F": Vec3(0, 0, -1),
    "B": Vec3(0, 0, 1)
}

move_map = {
    "U": turns.up,
    "D": turns.down,
    "L": turns.left,
    "R": turns.right,
    "F": turns.front,
    "B": turns.back,
}

# Animates rotation of a cube layer by grouping needed cubies under a helper entity
def rotate_side(normal, direction=1, speed=1):
    global is_rotating

    if is_rotating:
        return
    
    is_rotating=True

    # Left and Right rotations
    if normal == Vec3(1,0,0):
        [setattr(e, 'world_parent', rotation_helper) for e in gui3d.cubes if e.x > 0]
        rotation_helper.animate('rotation_x', 90 * direction, duration=.15*speed, curve=curve.linear, interrupt='finish')
    elif normal == Vec3(-1,0,0):
        [setattr(e, 'world_parent', rotation_helper) for e in gui3d.cubes if e.x < 0]
        rotation_helper.animate('rotation_x', -90 * direction, duration=.15*speed, curve=curve.linear, interrupt='finish')

    # Top and Bottom rotations
    elif normal == Vec3(0,1,0):
        [setattr(e, 'world_parent', rotation_helper) for e in gui3d.cubes if e.y > 0]
        rotation_helper.animate('rotation_y', 90 * direction, duration=.15*speed, curve=curve.linear, interrupt='finish')
    elif normal == Vec3(0,-1,0):
        [setattr(e, 'world_parent', rotation_helper) for e in gui3d.cubes if e.y < 0]
        rotation_helper.animate('rotation_y', -90 * direction, duration=.15*speed, curve=curve.linear, interrupt='finish')

    # Front and Back rotations
    elif normal == Vec3(0,0,1):
        [setattr(e, 'world_parent', rotation_helper) for e in gui3d.cubes if e.z > 0]
        rotation_helper.animate('rotation_z', -90 * direction, duration=.15*speed, curve=curve.linear, interrupt='finish')
    elif normal == Vec3(0,0,-1):
        [setattr(e, 'world_parent', rotation_helper) for e in gui3d.cubes if e.z < 0]
        rotation_helper.animate('rotation_z', 90 * direction, duration=.15*speed, curve=curve.linear, interrupt='finish')

    invoke(reset_rotation_helper, delay=.2*speed)

# Resets the rotation helper entity for the next rotation
def reset_rotation_helper():
    global is_rotating

    [setattr(e, 'world_parent', scene) for e in gui3d.cubes]
    rotation_helper.rotation = (0,0,0)
    is_rotating=False

# Executes both the visual rotation and logical cube move
def do_move(move, prime):
    rotate_side(rotation_map[move], prime)

    if prime == -1:
            turns.prime(move_map[move])
    else:
            move_map[move]()
    shared_logic.cube_update()

def input(key):
    if key == 'tab':
        shared_logic.switch()
    if key_input==False:
        return

    if key == 'r':
        if held_keys['left shift'] or held_keys['right shift']:
            do_move("R", -1)
        else:
            do_move("R", 1)

    elif key == 'l':
        if held_keys['left shift'] or held_keys['right shift']:
            do_move("L", -1)
        else:
            do_move("L", 1)

    elif key == 'u':
        if held_keys['left shift'] or held_keys['right shift']:
            do_move("U", -1)
        else:
            do_move("U", 1)

    elif key == 'd':
        if held_keys['left shift'] or held_keys['right shift']:
            do_move("D", -1)
        else:
            do_move("D", 1)

    elif key == 'f':
        if held_keys['left shift'] or held_keys['right shift']:
            do_move("F", -1)
        else:
            do_move("F", 1)

    elif key == 'b':
        if held_keys['left shift'] or held_keys['right shift']:
            do_move("B", -1)
        else:
            do_move("B", 1)

# Parses scramble strings into individual moves.
# .split() only works correctly when moves are separated by spaces.
# This parser also handles compact move strings with missing spaces.

# Example:
# D'B2F2DF2L2DF2U2R2B2D2FDR2DFL'B'R2D
# D' B2 F2D F2L2DF2 U2R2 B2 D2 FD R2 DFL'B'R2D
def move_parser(moves):
    moveset = []
    i=0
    while i<len(moves):
        ch=moves[i]
        if ch in "URFDLB":
            move = ch
            if i+1<len(moves):
                nex = moves[i+1]
                if nex=="'" or nex=="2":
                    move+=nex
                    i+=1
            moveset.append(move)
        i+=1
    return moveset

scr_entry = InputField(text_color=color.white, position=Vec2(-0.09, -0.4), scale=(1.4, 0.05))
def scramble_cube():
    delay=0

    moves = move_parser(scr_entry.text)
    for move in moves:
        try:
            if move.endswith("'"):
                invoke(do_move, move[:-1], -1, delay=delay)
            elif move.endswith("2"):
                invoke(do_move, move[:-1], 1, delay=delay)
                delay+=0.25
                invoke(do_move, move[:-1], 1, delay=delay)
            else:
                invoke(do_move, move, 1, delay=delay)
            delay+=0.25
        except KeyError:
            print(move, " is invalid and wasn't executed")
    
# Animates the Kociemba solution sequence on the cube
def solve_cube():
    delay = 0
    shared_logic.solve_btn.enabled = False
    shared_logic.scramble.enabled = False
    shared_logic.reset_btn.enabled = False
    shared_logic.get_solve()

    moves = shared_logic.solution.split()

    for move in moves:

        try:
            if move.endswith("'"):
                invoke(do_move, move[:-1], -1, delay=delay)
            elif move.endswith("2"):
                invoke(do_move, move[:-1], 1, delay=delay)
                delay += 0.25
                invoke(do_move, move[:-1], 1, delay=delay)
            else:
                invoke(do_move,move,1,delay=delay)
            delay += 0.25

        except KeyError:
            print(move, "is invalid")

    invoke(setattr, shared_logic.solve_btn, "enabled", True, delay=delay)
    invoke(setattr, shared_logic.scramble, "enabled", True, delay=delay)
    invoke(setattr, shared_logic.reset_btn, "enabled", True, delay=delay)

shared_logic.scramble._on_click = scramble_cube
shared_logic.solve_btn._on_click = solve_cube

# Toggles keyboard move input on/off and updates the button text
def key_inp_onclick():
    global key_input

    if key_inp_btn.text=="Turn Key Input On":
        key_inp_btn.text="Turn Key Input Off"
        key_input=True
    elif key_inp_btn.text=="Turn Key Input Off":
        key_inp_btn.text="Turn Key Input On"
        key_input=False

    key_inp_btn.fit_to_text()

key_inp_btn = Button(text="Turn Key Input On", position=Vec2(0.65, 0.4), on_click=key_inp_onclick, color="#9F77F6", highlight_scale=1.05, highlight_color = color.tint(color.hex("#9F77F6"), 0.2), radius=0.078)
key_inp_btn.fit_to_text()
