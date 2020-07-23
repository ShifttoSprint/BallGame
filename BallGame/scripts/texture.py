import pygame
pygame.init()

def load_texture(file,size,sizeh=32):
    bitmap=pygame.image.load(file)
    bitmap=pygame.transform.scale(bitmap,(size,sizeh))
    surface=pygame.Surface((size,sizeh),pygame.HWSURFACE|pygame.SRCALPHA)
    surface.blit(bitmap,(0,0))
    return surface

    
Player=load_texture("graphics\\ball.png",16,16)
Back=load_texture("graphics\\back.png",400,600)
ObsR=load_texture("graphics\\obstacleR.png",10,64)
ObsL=load_texture("graphics\\obstacleL.png",10,64)


TextureTags={"1":ObsR,"2":ObsL,"3":Back,"4":Player}
