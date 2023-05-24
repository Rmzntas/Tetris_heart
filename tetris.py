from settings import *
from tetromino import Tetromino

class Tetris:
    def __init__(self,app):
        self.app = app
        self.block_no = 0
        self.sprite_group = pg.sprite.Group()
        self.tetromino = Tetromino(self,self.block_no)
    
    def check_tetromino_landing(self):
        if self.tetromino.landing:
            self.block_no += 1
            if  self.block_no is not len(TETREMINO_SHAPE):
                self.tetromino = Tetromino(self,self.block_no)
            else:
                self.block_no -=1
            
    def draw_grid(self):
        for x in range (FIELD_W):
            for y in range (FIELD_H):
                pg.draw.rect(self.app.screen, 'black',
                             (x*TILE_SIZE, y * TILE_SIZE, TILE_SIZE , TILE_SIZE),1)
        
    def update(self):
        if self.app.anim_trigger:
            self.tetromino.update()
            self.check_tetromino_landing()
        self.sprite_group.update()
        
    def draw(self):
        self.draw_grid()
        self.sprite_group.draw(self.app.screen)
        