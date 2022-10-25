from vpython import *

import math

def main():
    # simulate the motion of the earth around the sun
    # define constants
    
    # universal gravitational constant
    G = 6.67e-11

    # mass of the sun
    m_sun = 1.989e30

    # mass of the earth
    m_earth = 5.972e24

    # mass of the moon
    m_moon = 7.348e22

    # create the objects
    sun = sphere (pos=vector(0, 0, 0), radius = 5e10, color=color.yellow)

    earth = sphere (pos=vector(1.496e11, 0, 0), radius = 1e10, color=color.blue, make_trail = True)

    moon = sphere (pos=vector(1.496e11 + 3.844e8, 0, 0), radius = .5e10, color=color.white, make_trail = True)

    earth.velocity = vector (0, 3e4, 0)

    moon.velocity = vector (0,3e4 + 1.022e3,0)

    t = 0
    
    dt = 3600

    while t < 1e10:
        
        rate(300)

        res_vector = earth.pos - sun.pos

        rem_vector = moon.pos - earth.pos

        rms_vector = moon.pos - sun.pos

        Fes_grav = -((G * m_earth * m_sun) / (mag(res_vector)**2)) * norm(res_vector)

        Fem_grav = -((G * m_earth * m_moon) / (mag(rem_vector)**2)) * norm(rem_vector)

        Fms_grav = -((G * m_moon * m_sun) / (mag(rms_vector)**2)) * norm(rms_vector)

        F_earth_net = Fes_grav - Fem_grav

        F_moon_net = Fms_grav + Fem_grav

        earth.pos = earth.pos + earth.velocity * dt
        
        moon.pos = moon.pos + moon.velocity * dt
        
        earth.velocity = earth.velocity + (F_earth_net/ m_earth) * dt
        
        moon.velocity = moon.velocity + (F_moon_net / m_moon) * dt
        
        t = t + dt

main()


