from settings import *


class Block(pg.sprite.Sprite):
    def __init__(self, tetromino,pos):
        self.tetromino = tetromino
        self.pos = vec(pos) + INIT_POS_OFFSET
        
        super().__init__(tetromino.tetris.sprite_group)
        self.image = pg.Surface([TILE_SIZE, TILE_SIZE])
        pg.draw.rect(self.image, 'red', (1,1,TILE_SIZE-2,TILE_SIZE-2),border_radius=8)
        self.rect = self.image.get_rect()
        
    def rotate(self, pivot_pos):
        translated = self.pos - pivot_pos
        rotated = translated.rotate(90)
        return rotated + pivot_pos
        
    def set_rect_pos(self):
        self.rect.topleft = self.pos * TILE_SIZE
        
    def update(self):
        self.set_rect_pos()
        

class Tetromino:
    def __init__(self,tetris,num):
        self.block_num = num
        self.max_number_move = len (MOVEMENT[self.block_num])
        self.move_no = 0
        self.tetris = tetris
        self.shape = TETREMINO_SHAPE[self.block_num]
        self.blocks = [Block(self,pos) for pos in TETROMINOES[self.shape]]
        self.landing = False
        
    def rotate(self):
        pivot_pos = self.blocks[0].pos
        new_block_positions = [block.rotate(pivot_pos) for block in self.blocks]
          
        for i, block in enumerate(self.blocks):
            block.pos =new_block_positions[i]
        
    def move(self,direction):
        move_direction = MOVE_DIRECTIONS[direction]
                
        for block in self.blocks:
                block.pos += move_direction
  
    def update(self):
        
        if self.max_number_move == self.move_no:
            self.landing = True
            
        elif MOVEMENT[self.block_num][self.move_no] == 1:
            self.rotate()
            self.move_no += 1
        else:
            self.move(direction=MOVEMENT[self.block_num][self.move_no])
            self.move_no += 1
