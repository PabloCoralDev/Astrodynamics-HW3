import matplotlib.pyplot as plt
from problem1 import *
from problem2 import *


# organize each problem and param vector : (name_for_chart, params, miu, R-planet(assumed), (r_unit, v_unit))
problems = [

    ("Problem 7", [15307.548, 0.7, 194, 39, 85, 48], 398600, 6378, ("km", "km/s")),
    ("Problem 8", [19133.333, 0.5, 30, 45, 45, 0], 398600, 6378, ("km", "km/s")),
    ("Problem 9", [20000, 0.45, 59, 27, 94, 58], 398600, 6378, ("km", "km/s")),
    ("Problem 10", [1.6, 0.4, 287, 46, 28, 139], 1, 1, ("DU", "DU/TU")), # make sure to use canonical units for time and distance

]


# set up fig and a unit sphere (scaled by R_planet in each plot)
fig = plt.figure(figsize=(12, 10))
theta, phi = np.meshgrid(np.linspace(0, 2*np.pi, 30), np.linspace(0, np.pi, 15))
sphere = np.array([np.cos(theta)*np.sin(phi), np.sin(theta)*np.sin(phi), np.cos(phi)])


# go thru each problem, destruct in shape {1, [problem]} (enumerate), get r, v and print/plot.
for k, (name, params, miu, R_planet, (r_unit, v_unit)) in enumerate(problems):
    r, v = get_velocity_position_vector(params, miu=miu)

    # print problem label, r and v vecs for each
    label = f"r = [{r[0]:.2f}, {r[1]:.2f}, {r[2]:.2f}] {r_unit}\nv = [{v[0]:.3f}, {v[1]:.3f}, {v[2]:.3f}] {v_unit}"
    print(f"\n{name}\n{label}")


    # create orbit path for nu 0 to 360 (full path); extract all params except nu, then concatenate a var nu
    orbit = np.array([get_velocity_position_vector(params[:5] + [nu], miu=miu)[0] for nu in range(361)]) # range is exclusive (so this will go until 360)

    # make sublot per problem with planet (3d shpere), orbit and scatter for locn of orbiting object
    ax = fig.add_subplot(2, 2, k + 1, projection="3d")

    # plot everything
    ax.plot_surface(*(R_planet*sphere), color="grey", alpha=0.5)
    ax.plot(*orbit.T, color="blue")
    ax.scatter(*r, color="red")
    ax.text(*r, label, fontsize=8)

    ax.set(title=name, xlabel=f"X ({r_unit})", ylabel=f"Y ({r_unit})", zlabel=f"Z ({r_unit})", aspect="equal")

plt.tight_layout()
plt.savefig("report/figures/problems7to10_orbits.png", dpi=200)
plt.show()
