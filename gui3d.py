from ursina import *

cube_colors = [
    color.hex("#D14040"),
    color.orange,
    color.white,
    color.yellow,
    color.azure,
    color.green,
]

cube_spacing = 1.04
cubes = []

# Create all cubies and stickers for 3D cube
def create_cube():
    global cubes

    for e in cubes:
        try:
            destroy(e)
        except:
            pass
    cubes.clear()

    for x in range(3):
        for y in range(3):
            for z in range(3):
                e = Entity(model="cube", position=Vec3((x-1)*cube_spacing, (y-1)*cube_spacing, (z-1)*cube_spacing), texture='white_cube', color="#000000")
                
                # Create Red face
                if x-1 == 1:
                    sticker = Entity(parent=e, model='plane', position=(0.52, 0, 0), texture='white_cube', color=cube_colors[0])
                    sticker.look_at(sticker.world_position + Vec3.right, axis=Vec3.up)
                    sticker.scale = 0.95
                    
                # Create Orange face
                if x-1 == -1:
                    sticker = Entity(parent=e, model='plane', position=(-0.52, 0, 0), texture='white_cube', color=cube_colors[1])
                    sticker.look_at(sticker.world_position + Vec3.left, axis=Vec3.up)
                    sticker.scale = 0.95
                    
                # Create White face
                if y-1 == 1:
                    sticker = Entity(parent=e, model='plane', position=(0, 0.52, 0), texture='white_cube', color=cube_colors[2])
                    sticker.look_at(sticker.world_position + Vec3.up, axis=Vec3.up)
                    sticker.scale = 0.95
                    
                # Create Yellow face
                if y-1 == -1:
                    sticker = Entity(parent=e, model='plane', position=(0, -0.52, 0), texture='white_cube', color=cube_colors[3])
                    sticker.look_at(sticker.world_position + Vec3.down, axis=Vec3.up)
                    sticker.scale = 0.95
                    
                # Create Blue face
                if z-1 == 1:
                    sticker = Entity(parent=e, model='plane', position=(0, 0, 0.52), texture='white_cube', color=cube_colors[4])
                    sticker.look_at(sticker.world_position + Vec3.forward, axis=Vec3.up)
                    sticker.scale = 0.95
                    
                # Create Green face
                if z-1 == -1:
                    sticker = Entity(parent=e, model='plane', position=(0, 0, -0.52), texture='white_cube', color=cube_colors[5])
                    sticker.look_at(sticker.world_position + Vec3.back, axis=Vec3.up)
                    sticker.scale = 0.95
                cubes.append(e)
