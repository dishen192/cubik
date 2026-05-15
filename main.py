from ursina import *
import gui3d
import gui2d
import shared_logic

app = Ursina()

#Window Settings
window.borderless = True
window.fullscreen = True
window.color = color._40
window.fps_counter.enabled = False
window.entity_counter.enabled = False
window.collider_counter.enabled = False
window.exit_button.enabled = True
window.exit_button.visible = True
window.exit_button.position = Vec2(0.8, 0.5)
window.cog_button.enabled = False

# Create both the 2D and 3D cubes
gui3d.create_cube()
gui2d.create_flatcube()

# Hide the 2D cube from view during the start
for btn in gui2d.buttons:
    btn.enabled = False

# Camera settings
cam = EditorCamera()
cam.rotation = (30, -45, 0)

# Creating all the helper buttons like reset, solve, scramble, etc
shared_logic.create_ui()

from logic import * #Imported after create_ui() to avoid execution problems

# To disable camera entity keyboard shortcuts baked into ursina
def update():

    if scr_entry.active:
        cam.ignore_input = True
    else:
        cam.ignore_input = False

app.run()