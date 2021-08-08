# Orbital-Warfare-Game
Basic 2D orbital warfare game with Newtonian physics, inspired by John Lumpkin's Human Reach novels.


## About
The Pink ship and White ship are battling it out high above Earth. Each ship has a laser and coilgun. Ships flash red when they're hit, and have limited fuel, health, and heat capacity.

<div align="center">
  <a href="https://www.youtube.com/watch?v=VJlpbi24f_g"><img src="https://img.youtube.com/vi/VJlpbi24f_g/0.jpg" alt="Sample Video"></a>
</div>


## How to play
This was created using [Processing.py](https://py.processing.org/); to play, download the repo and open it in Processing. The controls are below:
### Camera controls:
- Zoom in/out: Scroll
- Pan: Click and drag

### Pink ship:
- Fire coilgun: Q
- Fire laser: E
- Thrust: W
- Turn counter-clockwise: A
- Turn clockwise: D

### White ship:
- Fire coilgun: /
- Fire laser: .
- Thrust: SHIFT
- Turn counter-clockwise: LEFT
- Turn clockwise: RIGHT

### Mechanics:
- Temperature: Temperature rises when ships thrust, or use their lasers. If the temperature gauge gets completely full, the ship overheats and dies.
- Fuel: Fuel is used when the ships thrust. If the ship runs out of fuel, it will stop being able to maneuver.
- Damage: Laser damage is a function of distance; the closer you are to the target, the more damage the laser will cause. Coilgun damage is a function of relative velocity-- the higher the relative velocity between the coilgun round and a ship upon impact, the greater the damage.


## Basic Strategy
Lasers and coilguns deal the same amount of damage; however, coilguns are slow while lasers arrive instantaneously. Since lasers can destroy incoming coilgun shells, a useful tactic (taken straight from John Lumpkin's books), is to think about coilguns as creating "terrain" that the enemy ship needs to navigate. To prevent the enemy ship from bringing its laser to bear on you, send some coilgun shells their way to force them either to turn and thrust to dodge, or turn and fire directly at the incoming shells.

Enjoy!
