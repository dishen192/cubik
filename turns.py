# Contains cube state data and functions for executing cube moves

cube = {
    "white" : [
        ["white", "white", "white"],
        ["white", "white", "white"],
        ["white", "white", "white"]
    ],

    "yellow" : [
        ["yellow", "yellow", "yellow"],
        ["yellow", "yellow", "yellow"],
        ["yellow", "yellow", "yellow"]
    ],

    "red" : [
        ["red", "red", "red"],
        ["red", "red", "red"],
        ["red", "red", "red"]
    ],

    "orange" : [
        ["orange", "orange", "orange"],
        ["orange", "orange", "orange"],
        ["orange", "orange", "orange"]
    ],

    "green" : [
        ["green", "green", "green"],
        ["green", "green", "green"],
        ["green", "green", "green"]
    ],

    "blue" : [
        ["blue", "blue", "blue"],
        ["blue", "blue", "blue"],
        ["blue", "blue", "blue"]
    ]
}

# Upper face rotation
def up():
    global cube

    temp = cube["green"][0][:]
    
    cube["green"][0]=cube["red"][0][:]
    cube["red"][0]=cube["blue"][0][:]
    cube["blue"][0]=cube["orange"][0][:]
    cube["orange"][0]=temp

    cube["white"] = [
        [cube["white"][2][0], cube["white"][1][0], cube["white"][0][0]],
        [cube["white"][2][1], cube["white"][1][1], cube["white"][0][1]],
        [cube["white"][2][2], cube["white"][1][2], cube["white"][0][2]]
    ]

# Bottom face rotation
def down():
    global cube

    temp = cube["green"][2][:]

    cube["green"][2]=cube["orange"][2][:]
    cube["orange"][2]=cube["blue"][2][:]
    cube["blue"][2]=cube["red"][2][:]
    cube["red"][2]=temp

    cube["yellow"] = [
        [cube["yellow"][2][0], cube["yellow"][1][0], cube["yellow"][0][0]],
        [cube["yellow"][2][1], cube["yellow"][1][1], cube["yellow"][0][1]],
        [cube["yellow"][2][2], cube["yellow"][1][2], cube["yellow"][0][2]]
    ]

# Left face rotation
def left():
    global cube

    t1, t2, t3 = cube["green"][0][0], cube["green"][1][0], cube["green"][2][0]
    cube["green"][0][0], cube["green"][1][0], cube["green"][2][0] = cube["white"][0][0], cube["white"][1][0], cube["white"][2][0]
    cube["white"][0][0], cube["white"][1][0], cube["white"][2][0] = cube["blue"][2][2], cube["blue"][1][2], cube["blue"][0][2]
    cube["blue"][0][2], cube["blue"][1][2], cube["blue"][2][2] = cube["yellow"][2][0], cube["yellow"][1][0], cube["yellow"][0][0]
    cube["yellow"][0][0], cube["yellow"][1][0], cube["yellow"][2][0] = t1, t2, t3

    cube["orange"] = [
        [cube["orange"][2][0], cube["orange"][1][0], cube["orange"][0][0]],
        [cube["orange"][2][1], cube["orange"][1][1], cube["orange"][0][1]],
        [cube["orange"][2][2], cube["orange"][1][2], cube["orange"][0][2]]
    ]

# Right face rotation
def right():
    global cube

    t1, t2, t3 = cube["green"][0][2], cube["green"][1][2], cube["green"][2][2]
    cube["green"][0][2], cube["green"][1][2], cube["green"][2][2] = cube["yellow"][0][2], cube["yellow"][1][2], cube["yellow"][2][2]
    cube["yellow"][0][2], cube["yellow"][1][2], cube["yellow"][2][2] = cube["blue"][2][0], cube["blue"][1][0], cube["blue"][0][0]
    cube["blue"][0][0], cube["blue"][1][0], cube["blue"][2][0] = cube["white"][2][2], cube["white"][1][2], cube["white"][0][2]
    cube["white"][0][2], cube["white"][1][2], cube["white"][2][2] = t1, t2, t3

    cube["red"] = [
        [cube["red"][2][0], cube["red"][1][0], cube["red"][0][0]],
        [cube["red"][2][1], cube["red"][1][1], cube["red"][0][1]],
        [cube["red"][2][2], cube["red"][1][2], cube["red"][0][2]]
    ]

# Front face rotation
def front():
    global cube

    t1, t2, t3 = cube["white"][2][0], cube["white"][2][1], cube["white"][2][2]
    cube["white"][2][0], cube["white"][2][1], cube["white"][2][2] = cube["orange"][2][2], cube["orange"][1][2], cube["orange"][0][2]
    cube["orange"][0][2], cube["orange"][1][2], cube["orange"][2][2] = cube["yellow"][0][0], cube["yellow"][0][1], cube["yellow"][0][2]
    cube["yellow"][0][0], cube["yellow"][0][1], cube["yellow"][0][2] = cube["red"][2][0], cube["red"][1][0], cube["red"][0][0]
    cube["red"][0][0], cube["red"][1][0], cube["red"][2][0] = t1, t2, t3

    cube["green"] = [
        [cube["green"][2][0], cube["green"][1][0], cube["green"][0][0]],
        [cube["green"][2][1], cube["green"][1][1], cube["green"][0][1]],
        [cube["green"][2][2], cube["green"][1][2], cube["green"][0][2]]
    ]

# Back face rotation
def back():
    global cube

    t1, t2, t3 = cube["yellow"][2][0], cube["yellow"][2][1], cube["yellow"][2][2]
    cube["yellow"][2][0], cube["yellow"][2][1], cube["yellow"][2][2] = cube["orange"][0][0], cube["orange"][1][0], cube["orange"][2][0]
    cube["orange"][0][0], cube["orange"][1][0], cube["orange"][2][0] = cube["white"][0][2], cube["white"][0][1], cube["white"][0][0]
    cube["white"][0][0], cube["white"][0][1], cube["white"][0][2] = cube["red"][0][2], cube["red"][1][2], cube["red"][2][2]
    cube["red"][2][2], cube["red"][1][2], cube["red"][0][2] = t1, t2, t3

    cube["blue"] = [
        [cube["blue"][2][0], cube["blue"][1][0], cube["blue"][0][0]],
        [cube["blue"][2][1], cube["blue"][1][1], cube["blue"][0][1]],
        [cube["blue"][2][2], cube["blue"][1][2], cube["blue"][0][2]]
    ]

# Execute prime/inverse moves
def prime(move):
    for i in range(3):
        move()

# Handle double moves
def twice(move):
    for i in range(2):
        move()

# Solved cube state
def solved_cube():
    global cube
    cube = {
        "white" : [
            ["white", "white", "white"],
            ["white", "white", "white"],
            ["white", "white", "white"]
        ],

        "yellow" : [
            ["yellow", "yellow", "yellow"],
            ["yellow", "yellow", "yellow"],
            ["yellow", "yellow", "yellow"]
        ],

        "red" : [
            ["red", "red", "red"],
            ["red", "red", "red"],
            ["red", "red", "red"]
        ],

        "orange" : [
            ["orange", "orange", "orange"],
            ["orange", "orange", "orange"],
            ["orange", "orange", "orange"]
        ],

        "green" : [
            ["green", "green", "green"],
            ["green", "green", "green"],
            ["green", "green", "green"]
        ],

        "blue" : [
            ["blue", "blue", "blue"],
            ["blue", "blue", "blue"],
            ["blue", "blue", "blue"]
        ]
    }