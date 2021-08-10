from Game import Game
from Camera import Camera

add_library("minim")
height  = int(480*1.5)
width = 640*2


class Sounds:
    def __init__(self):
        self.THRUST = minim.loadFile("thrust.wav")
        self.LASER = minim.loadFile("laser.wav")
        self.CANNON = minim.loadFile("cannon.wav")
        self.HISS = minim.loadFile("hiss.wav")
    
class Images:
    def __init__(self):
        self.PLANET = loadImage("planet5.png")
        self.INDICATOR = loadImage("indicator1.png")
        self.INDICATOR_BASE = loadImage("indicator_base.png")
        self.INDICATOR_ELLIPSE = loadImage("indicator_ellipse.png")
        self.SPACECRAFT_BODY_0 = loadImage("spacecraft_body_0.png")
        self.SPACECRAFT_HEAD_0 = loadImage("spacecraft_head_0.png")
        self.SPACECRAFT_BODY_1 = loadImage("spacecraft_body_1.png")
        self.SPACECRAFT_HEAD_1 = loadImage("spacecraft_head_1.png")
    

scale_factor = 1
xOffset = 0
yOffset = 0
bx = 0
by = 0


def setup():
    bx = width/2
    by = height/2
    size(width, height)
    global img, game, bg
    global minim
    minim = Minim(this)
    sf = Sounds()
    img = Images()
    bg = loadImage("background.png")
    bg.resize(width, height)
    game = Game(width, height, img, sf)


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


def keyReleased():
    game.handleKeyReleased(key)

def draw():
    background(bg)
    # background(5, 3, 28)
    pushMatrix()
    translate(bx, by)
    scale(scale_factor)
    game.draw(keyPressed)
    popMatrix()
    game.updateGUI()
