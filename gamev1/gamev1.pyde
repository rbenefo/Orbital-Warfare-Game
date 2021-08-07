from Game import Game

height  = int(480*1.5)
width = 640*2

game = Game(width, height)
    
        

def setup():
    size(width, height)


def keyReleased():
    game.handleKeyReleased(key)
        
def draw():
    background(0, 0, 0);
    game.draw(keyPressed)
