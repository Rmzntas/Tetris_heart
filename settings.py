import pygame as pg

vec =pg.math.Vector2

FPS = 60
FIELD_COLOR = (48, 39, 32)

ANIM_TIME_INTERVAL = 80

TILE_SIZE = 35
FIELD_SIZE = FIELD_W, FIELD_H = 17,18
FIELD_RES = FIELD_W * TILE_SIZE, FIELD_H * TILE_SIZE

#Starting position
INIT_POS_OFFSET = vec(FIELD_W // 2 , 1)

# l: left     r: right    d: down
MOVE_DIRECTIONS = {'l': vec(-1, 0), 'r': vec(1, 0), 'd': vec(0, 1)}

TETROMINOES = {
    'T': [(0, 0), (-1, 0), (1, 0), (0, -1)],
    'O': [(0, 0), (0, -1), (1, 0), (1, -1)],
    'J': [(0, 0), (-1, 0), (0, -1), (0, -2)],
    'L': [(0, 0), (1, 0), (0, -1), (0, -2)],
    'I': [(0, 0), (0, 1), (0, -1), (0, -2)],
    'S': [(0, 0), (-1, 0), (0, -1), (1, -1)],
    'Z': [(0, 0), (1, 0), (0, -1), (-1, -1)]
}

TETREMINO_SHAPE = ['I','T','Z','S','T','J','S','T','L','J','I','Z','O','J','J','J','T','I','I','J','I','J','Z','T','Z','L']

MOVEMENT = [  
    ['d','d','d','d','d','d','d','d','d','d','d','d','d','d','d'],          #I
    ['d','d',1,'d','d',1,'d','d',1,'d','d','d','l','d','d','d','d','d'],    #T
    ['d','d',1,'d','d','d','d','r','d','d','d','d','d','d','d','d'],        #Z
    ['d','d','d','d','l','d','d','d','l','d','d','d','d','d','d'],          #S
    ['d',1,'d','d',1,'d','d','r','d','d','r','d','d','r','d','d','d'],      #T
    ['d','d',1,'d','d','d',1,'d','d','d','r','d','d','d'],                  #J
    ['d','d','l','d','d','d','l','d','d','d','l','d','d','d','d'],          #S
    ['d',1,'d','d','d',1,'d','d','d',1,'d','d','d','d'],                    #T
    ['d','l','d','d','l','d','d','l','d','d','l','d','d','l','d','d'],      #L
    ['d','d',1,'d','r','d','d','r','d','d','r','d','d','d','d'],            #J
    ['d','d',1,'d','l','d','d','l','d','d','l','d','d','d'],                #I
    ['d','d',1,'d','r','d','d','r','d','d','d','d'],                        #Z
    ['d','d','r','d','d','r','d','r','d','r','d','d','d','d'],              #O
    ['d',1,'d','d',1,'d','d','r','d','d','d'],                              #J
    ['d',1,'d','d','l','d','l','d','l','d','d','d','d'],                    #J
    ['d',1,'d',1,'d','d',1,'d','d','d','d'],                                #J
    [1,'d','d',1,'d',1,'l','d','l','d','l','d','l','d','d'],                #T
    ['d','r','d','r','d','r','d','r','d','r','d','r','d','d','d'],          #I
    ['d','l','d','l','d','l','d','l','d','l','d','l','d','d','d'],          #I
    ['d','r','d','r','d','r','d','r','d','r','d','d','d'],                  #J
    ['d',1,'d','d','r','d','d','d','d'],                                    #I
    ['d',1,'d','l','d','l','d','l','d','d','d',],                           #J
    ['l',1,'d','l','d','l','d','l','d','l','d','d'],                        #Z
    ['d','d','r','d','r','d','d','d'],                                      #T
    ['d','d','l','d','d','l','d','d'],                                      #Z
    ['r',1,'d','r',1,'r','d','r','d','d','d']                               #L
]
