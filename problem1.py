import numpy as np

def get_orbital_params(position_velocity_vector, miu=398600.4418):
    """
    Position & inertial velocity [r, v] -> orbital elements [a, e, O, i, w, nu] (angles in degrees).
    Assumes the planet is an inertial frame with basis Ix = [1,0,0], Iy = [0,1,0], Iz = [0,0,1].
    """
    
    # little helper
    norm = lambda vec: np.linalg.norm(vec) 

    # def inertial frame
    Ix_ = [1,0,0]
    Iy_ = [0,1,0]
    Iz_= [0,0,1]

    # destructure from incoming vector
    r_, v_ = np.asarray(position_velocity_vector, dtype=float)

    # get hvec
    h_ = np.cross(r_, v_)

    # get constant values
    p = (norm(h_)**2)/miu
    e_ = ((np.cross(v_, h_))/miu) - (r_/norm(r_))
    e = norm(e_)
    a = (p/(1-e**2))
    n_ = np.cross(Iz_, h_)

    # form data structure with what goes in each arctan
    """
    The angles are:
    O = arctan(A/B), with 2pi correction
    i = arctan(A/B), without correction
    w = arctan(A/B), with 2pi correction
    nu = arctan(A/B), with 2pi correction
    """

    angle_inputs = {

        "O": {

            "A": np.dot(n_, Iy_), 
            "B": np.dot(n_, Ix_),
            "correction": True
        },

        "i": {

            "A": np.dot(h_, np.cross(n_, Iz_)),
            "B": norm(n_)*np.dot(h_, Iz_),
            "correction": False
        }, 
        
        "w": {

            "A": np.dot(e_, np.cross(h_, n_)),
            "B": norm(h_)*np.dot(e_, n_),
            "correction": True
        },        
        
        "nu": {

            "A": np.dot(r_, np.cross(h_, e_)),
            "B": norm(h_)*np.dot(r_, e_),
            "correction": True
        }
    }


    # form angle outputs (4-quadrant arctan, add 2pi to negatives where correction applies)
    angles = {}

    for name, inputs in angle_inputs.items():

        angle = np.arctan2(inputs["A"], inputs["B"])

        if inputs["correction"] and angle < 0:
            angle += 2*np.pi

        angles[name] = angle

    # convert to degrees to match problem2 inputs
    O, i, w, nu = (np.degrees(angles[k]) for k in ("O", "i", "w", "nu"))

    # put together ourputs into vec: [a, e, O, i, w, nu]
    out_vec = [a, e, O, i, w, nu]

    return out_vec

