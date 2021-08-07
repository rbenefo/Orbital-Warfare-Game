from Game import Game
from Camera import Camera
height  = int(480*1.5)
width = 640*2

game = Game(width, height)
scale_factor = 1
xOffset = 0
yOffset = 0
bx = 0
by = 0

def mouseWheel(event):
    global scale_factor
    e = event.getCount()
    scale_factor += e*0.001
    if scale_factor < 0:
        scale_factor = 0

def mouseDragged():
    global bx, by
    bx = mouseX-xOffset
    by = mouseY - yOffset

def mousePressed():
    global xOffset, yOffset
    xOffset = mouseX-bx
    yOffset = mouseY-by
    
def setup():
    bx = width/2
    by = height/2
    size(width, height)


def keyReleased():
    game.handleKeyReleased(key)
        
def draw():
    background(0, 0, 0);
    print(bx)
    translate(bx, by)
    scale(scale_factor)
    game.draw(keyPressed)
