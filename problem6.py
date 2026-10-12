from problem5 import get_elements_p5
from problem2 import get_velocity_position_vector

# use problem 5 function, then use problem 2 function
param_vector = get_elements_p5()[:6]
r, v = get_velocity_position_vector(param_vector, miu=1)


# print out to confirm these are same values given in 2-5
print(f"r = [{r[0]:.6f}, {r[1]:.6f}, {r[2]:.6f}]  AU")
print(f"v = [{v[0]:.6f}, {v[1]:.6f}, {v[2]:.6f}]  AU/TU")
