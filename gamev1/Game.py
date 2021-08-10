from Spacecraft import SpaceCraft
from Planet import Planet
from Collision import Collision
from GUI import GUI


class Game:
    def __init__(self, width, height, img, Sounds):
        self.height  = height
        self.width = width
        
        self.physics = PhysicsEngine(width, height)
        
        self.ships = {}
        self.ship_idx = -1
        
        self.addShip(maxthrust = 0.0001, m = 10, pos = PVector(200, 240),vel = PVector(0, 0.015), \
            sounds = Sounds, img = img, p = 0)
        self.addShip(maxthrust = 0.0001, m = 10, pos = PVector(600, 240),vel = PVector(0.033, -0.01), \
                     sounds = Sounds, img = img, p = 1)
        
        self.planet = Planet(self.width/2, self.height/2, 100, m = 0.15, img = img)
        self.lastDraw = millis()
        
        self.collision = Collision()
        self.damageModel = DamageModel()
        self.gui = GUI(width, height, img)
        
    def draw(self, keyPressed):
        self.planet.draw()
        ship_a_dict = {}
        for idx, ship in self.ships.items():
            a, rm = self.physics.calcAccel(ship, self.planet)
            if rm:
                ship.health = 0
                ship.alive = False
                ship.crashed = True
            ship_a_dict[idx] = a
        laser_dict = {}
        if keyPressed:
            if key == "d": #ship1 right
                if self.ships[0].alive:
                    self.ships[0].turnRight()
            if key == "a": #ship1 left
                if self.ships[0].alive:
                    self.ships[0].turnLeft()
                
            if key == "w": #ship1 thrust
                if self.ships[0].alive:
                    thrust_accel_vec_0 = self.ships[0].thrust()
                    ship_a_dict[0].add(thrust_accel_vec_0)
    
            if key == "q":
                if self.ships[0].alive:
                    self.ships[0].fire()
            if key == "e":
                if self.ships[0].alive:
                    beg, ending = self.ships[0].fireLaser()
                    laser_dict[0] = (beg, ending)
    
            if key == "/":
                if self.ships[1].alive:
                    self.ships[1].fire()
            if key == ".":
                if self.ships[1].alive:
                    beg, ending = self.ships[1].fireLaser()
                    laser_dict[1] = (beg, ending)
                    
            if key == "r":
                if self.ships[0].alive:
                    self.ships[0].angular_vel = 0
            if key == ENTER:
                if self.ships[1].alive:
                    self.ships[1].angular_vel = 0

            if key == CODED:
                if keyCode == RIGHT:
                    if self.ships[1].alive:
                        self.ships[1].turnRight()
                elif keyCode == LEFT:
                    if self.ships[1].alive:
                        self.ships[1].turnLeft()
                elif keyCode == SHIFT: #ship2 thrust
                    if self.ships[1].alive:
                        thrust_accel_vec_1 = self.ships[1].thrust()
                        ship_a_dict[1].add(thrust_accel_vec_1)
        
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

        for idx, ship in self.ships.items():
            for cidx, coilgun_round in ship.coilgun_rounds.items():
                for idx2, ship2 in self.ships.items():
                    collision = self.collision.coilgun_spacecraft_collision_check(coilgun_round, ship2)
                    if collision:
                        relVel = PVector.sub(ship2.vel, ship.coilgun_rounds[cidx].vel).mag()
                        damage = self.damageModel.coilgun_hit(relVel)
                        ship.coilgun_rounds.pop(cidx)
                        ship2.hit = True
                        ship2.health -= damage
                        
        for laserid, laser in laser_dict.items():
                for idx, ship in self.ships.items():
                    collision = self.collision.laser_spacecraft_check(laser, ship)
                    if collision:
                        relPos = PVector.sub(self.ships[laserid].vel, ship.vel).mag()
                        damage = self.damageModel.laser_hit(relPos)
                        ship.hit = True
                        ship.health -= damage
        for idx, ship in self.ships.items():
            ship.hit = False
            if ship.alive:
                self.physics.drawPath(ship, self.planet) #later optimization-- only draw path if thrust has been executed?
            ship.draw()
        self.lastDraw = m

    def updateGUI(self):
        for idx, ship in self.ships.items():
            heatpercent = ship.heat/ship.max_heat
            healthpercent = ship.health/ship.max_health
            fuelpercent = ship.fuel_level/ship.max_fuel

            if idx == 0:
                self.gui.update_ship0_gui(heatpercent, healthpercent, fuelpercent)
            else:
                self.gui.update_ship1_gui(heatpercent, healthpercent, fuelpercent)
                
        
    def addShip(self, maxthrust, m, pos, vel, sounds, img, p):
        ship = SpaceCraft(maxthrust, m, pos, vel, sounds, img, p)
        self.ship_idx += 1
        self.ships[self.ship_idx] = ship


    def handleKeyReleased(self, key):
        if key == "w":
            self.ships[0].sounds.THRUST.pause()
            self.ships[0].sounds.THRUST.rewind()
            self.ships[0].turnOffThrust()
        if keyCode == SHIFT:
            self.ships[1].sounds.THRUST.pause()
            self.ships[1].sounds.THRUST.rewind()
            self.ships[1].turnOffThrust()
        if key == "e":
            self.ships[0].sounds.LASER.rewind()
        if key == ".":
            self.ships[1].sounds.LASER.rewind()
        if key == "q":
            self.ships[0].sounds.CANNON.rewind()
        if key == "/":
            self.ships[1].sounds.CANNON.rewind()
            
        if key == "a" or key == "d":
            self.ships[1].sounds.HISS.pause()
            self.ships[0].sounds.HISS.rewind()
        if keyCode == LEFT or keyCode == RIGHT:
            self.ships[1].sounds.HISS.pause()
            self.ships[1].sounds.HISS.rewind()
class PhysicsEngine:
    def __init__(self, width, height):
        self.G = 1 #gravitational constant
        self.width = width
        self.height = height
    def calcAccel(self, obj, planet):
        rm = False
        r = PVector.sub(obj.pos, planet.pos)
        distance = r.mag()
        if distance <= planet.s/2:
            rm = True
        if obj.type == "coilgun" and distance > 5000:
            rm  = True
        a = -(self.G*planet.mass)/distance**2
        accel_vec = r.normalize().mult(a)
        if distance <= planet.atmosphere_radius/2 and not rm:
            obj.reentering = True
            drag_coeff = 0.00005
            density = 50.0/(distance+5-planet.s/2)
            drag_constant = density*drag_coeff
            # print(drag_constant)
            drag = PVector.mult(obj.vel, drag_constant)
            accel_vec = PVector.sub(accel_vec, drag)
        else:
            obj.reentering = False

        return accel_vec, rm
    def step(self, obj, dt):
        dv = obj.accel.mult(dt)
        obj.vel.add(dv)
        dp = PVector.mult(obj.vel, dt)
        obj.pos.add(dp)
        if obj.type == "spacecraft":
            obj.theta += obj.angular_vel*dt
            damping_const = 0.000005
            if obj.angular_vel < 0:
                obj.angular_vel+=  damping_const
            elif obj.angular_vel > 0:
                obj.angular_vel-=  damping_const


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
        
class DamageModel:
    def __init__(self):
        pass
    def coilgun_hit(self, relVel):
        damage = relVel*1
        return damage
    
    def laser_hit(self, relPos):
        try:
            damage = 1.0/(0.5*float(relPos))*0.001
        except ZeroDivisionError:
            damage = 0
        if damage > 0.03:
            damage = 0.03
        return damage
