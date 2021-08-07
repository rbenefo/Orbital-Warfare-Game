from Spacecraft import SpaceCraft
from Planet import Planet
from Collision import Collision
class Game:
    def __init__(self, width, height):
        self.height  = height
        self.width = width
        
        self.physics = PhysicsEngine(width, height)
        
        self.ships = {}
        self.ship_idx = -1
        
        self.addShip(maxthrust = 0.00005, m = 10, x = 100, y = 240, rgb = color(255, 0, 255))
        self.addShip(maxthrust = 0.00005, m = 10, x = 150, y = 240, rgb = color(255, 255, 255))
        
        self.planet = Planet(self.width/2, self.height/2, 100, m = 0.3)
        self.lastDraw = millis()
        
        self.collision = Collision()
        
    def draw(self, keyPressed):
        self.planet.draw()
        ship_a_dict = {}
        for idx, ship in self.ships.items():
            a, rm = self.physics.calcAccel(ship, self.planet)
            ship_a_dict[idx] = a
        laser_dict = {}
        if keyPressed:
            if key == "t": #ship1 thrust
                thrust_accel_vec_0 = self.ships[0].thrust()
                ship_a_dict[0].add(thrust_accel_vec_0)
            if key == "p": #ship2 thrust
                thrust_accel_vec_1 = self.ships[1].thrust()
                ship_a_dict[1].add(thrust_accel_vec_1)
            if key == "d": #ship2 right
                self.ships[1].turnRight()
            if key == "a": #ship2 left
                self.ships[1].turnLeft()

            if key == "f":
                self.ships[0].fire()
            if key == "e":
                beg, ending = self.ships[0].fireLaser()
                laser_dict[0] = (beg, ending)

            if key == "l":
                self.ships[1].fire()
            if key == "k":
                beg, ending = self.ships[1].fireLaser()
                laser_dict[1] = (beg, ending)

            if key == CODED:
                if keyCode == RIGHT:
                    self.ships[0].turnRight()
                elif keyCode == LEFT:
                    self.ships[0].turnLeft()
        m = millis()
        dt = m - self.lastDraw

        for idx, ship in self.ships.items():
            ship.applyAccel(ship_a_dict[idx])
            self.physics.step(ship, dt)
        for idx, ship in self.ships.items():
                for cidx, coilgun_round in ship.coilgun_rounds.items():
                    a, rm = self.physics.calcAccel(coilgun_round, self.planet)
                    coilgun_round.applyAccel(a)
                    self.physics.step(coilgun_round, dt)
                    coilgun_round.draw()
                    if rm:
                        ship.coilgun_rounds.pop(cidx)
            
        for idx, ship in self.ships.items():
            for laserid, laser in laser_dict.items():
                for cidx, coilgun_round in ship.coilgun_rounds.items():
                    if self.collision.laser_coilgun_check(laser, coilgun_round):
                        ship.coilgun_rounds.pop(cidx)
                        continue
                    for idx2, ship2 in self.ships.items():
                        collision = self.collision.coilgun_spacecraft_collision_check(coilgun_round, ship2)
                        if collision:
                            ship.coilgun_rounds.pop(cidx)
                            ship2.hit = True
        for laserid, laser in laser_dict.items():
            for idx, ship in self.ships.items():
                collision = self.collision.laser_spacecraft_check(laser, ship)
                if collision:
                    ship.hit = True
        for idx, ship in self.ships.items():
            ship.draw()
            ship.hit = False
            self.physics.drawPath(ship, self.planet) #later optimization-- only draw path if thrust has been executed?
        self.lastDraw = m

    
    def addShip(self, maxthrust, m, x, y, rgb):
        ship = SpaceCraft(maxthrust, m, x, y, rgb)
        self.ship_idx += 1
        self.ships[self.ship_idx] = ship


    def handleKeyReleased(self, key):
        if key == "t":
            self.ships[0].turnOffThrust()
        if key == "p":
            self.ships[1].turnOffThrust()

class PhysicsEngine:
    def __init__(self, width, height):
        self.G = 1 #gravitational constant
        self.width = width
        self.height = height
    def calcAccel(self, obj, planet):
        rm = False
        r = PVector.sub(obj.pos, planet.pos)
        distance = r.mag()
        if distance <= planet.s/2 or distance >= 1000:
            rm = True
        a = -(self.G*planet.mass)/distance**2
        accel_vec = r.normalize().mult(a)
        return accel_vec, rm
    def step(self, obj, dt):
        dv = obj.accel.mult(dt)
        obj.vel.add(dv)
        dp = PVector.mult(obj.vel, dt)
        obj.pos.add(dp)


    def drawPath(self, obj, planet):
        mu = self.G*planet.mass
        rel_dist_vec = PVector.sub(obj.pos, planet.pos)
        r = rel_dist_vec.mag()
        a = mu*r/(2*mu-r*obj.vel.magSq())
        h = rel_dist_vec[0]*obj.vel[1]-rel_dist_vec[1]*obj.vel[0]
        a = mu*r/(2*mu-r*(obj.vel[1]**2+obj.vel[0]**2))
        ex = rel_dist_vec[0]/r - h*obj.vel[1]/mu
        ey = rel_dist_vec[1]/r + h*obj.vel[0]/mu
        eccentricity_vector = PVector(ex, ey)
        
        e = eccentricity_vector.mag()
        b = a*sqrt(1-e**2)
        
        empty_focus = PVector(2*a*ex, 2*a*ey)
        center = PVector.add(empty_focus, PVector(0,0)).div(2)
        center_translated = center.add(PVector(self.width/2,self.height/2))
        angle = PVector.angleBetween(eccentricity_vector, PVector(1,0))
        stroke(255)
        strokeWeight(1)
        noFill()
        pushMatrix()
        translate(center_translated[0], center_translated[1])
        if ey > 0:
            rotate(angle)
        else:
            rotate(-angle)
        ellipse(0,0, 2*a,2*b)
        popMatrix()
