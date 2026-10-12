from problem1 import *
from problem2 import *

# encase in a function so I can call from Problem 6
def get_elements_p5():

    # set up - all in AU, about Sun
    pos_vec = [0.7,  0.6, 0.3]
    vel_vec = [-0.8, 0.8, 0]
    miu = 1

    # get orbital elements
    position_velocity_vector = [pos_vec, vel_vec]
    a, e, O, i, w, nu = get_orbital_params(position_velocity_vector=position_velocity_vector, miu=1)

    return a,e,O,i,w,nu, pos_vec, vel_vec, miu

if __name__ == "__main__":

    # destructure everything
    a,e,O,i,w,nu, pos_vec, vel_vec, miu = get_elements_p5()

    # get other props (period, p, h_vec and h, energy)
    T = 2*np.pi*np.sqrt((a**3/miu))
    p = a*(1-e**2)
    h_ = np.cross(pos_vec, vel_vec)
    h = np.linalg.norm(h_)
    energy = -(miu/(2*a))

    # determine if asteroid can impact earth

    # find ascending and descending nodes of asteroid's orbit 
    r_asc = p / (1 + e*np.cos(np.radians(-w)))
    r_desc = p / (1 + e*np.cos(np.radians(180 - w)))
    R_earth = 6378 / 1.496e8

    # assume earth has a circular orbit with radius 1AU
    impact = abs(r_asc - 1) <= R_earth or abs(r_desc - 1) <= R_earth

    print("(a) a, e, O, i, w, nu:", a, e, O, i, w, nu)
    print("(b) T [TU]:", T)
    print("(c) p [AU]:", p)
    print("(d) h_ [AU^2/TU]:", h_, " h:", h)
    print("(e) energy [AU^2/TU^2]:", energy)
    print("r at nodes [AU]:", r_asc, r_desc)
    print("impact:", impact)
