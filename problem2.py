
import numpy as np
from scipy.spatial.transform import Rotation as R

def get_velocity_position_vector(orbital_parameters, miu=398600.4418):

    ## simple Euler rotations - Can use scipy.spacial.transform
    # destruct from incoming vector
    a, e, O, i, w, nu = orbital_parameters 

    # create Rotation objects - we will have a 3-1-3 (Z-X-Z) Rotation

    rot1 = R.from_euler('z', O, degrees=True)
    rot2 = R.from_euler('x', i, degrees=True)
    rot3 = R.from_euler('z', w, degrees=True) 

    # multiply together to get overall transformation matrix
    rotation_matrix = rot1 * rot2 * rot3

    # get perifocal position and velocity, then convert into inertial frame
    # nu comes in as degrees, np.cos/np.sin need radians
    nu = np.radians(nu)
    p = a*(1-e**2)
    r = (p/(1+e*np.cos(nu)))
    r_perifocal = np.array([r*np.cos(nu), r*np.sin(nu), 0])
    v_perifocal = np.sqrt((miu/p))*np.array([-np.sin(nu), (e+np.cos(nu)), 0])


    r_intertial = rotation_matrix.apply(r_perifocal)
    v_intertial = rotation_matrix.apply(v_perifocal)

    return [r_intertial, v_intertial]



    