import numpy as np

def check_placement(coords, design, rng, aperture):
    # check to make sure hole falls onto a mirror segment and doesn't overlap a spider or another hole
    # uses a boolean mask of the aperture and holes already placed
    # if there's a problem, calls add_hole() again
    check = 
    if check == 1:
        coords = add_hole(design.hrad, rng, aperture)

def add_hole(hrad, rng, aperture):
    # generates coordinates for a new hole, checks that hole doesn't intersect spiders or other holes and falls within aperture
    coords = rng.integer(low=-5, high=5, size=2, dtype=float)
    check_placement(coords, hrad, rng, aperture)
    return coords

def check_redundancy(my_design):
    # checks that baselines are 0% redundant
    uv_rad = my_design.hrad
    n = 50000
    for i in my_design.uv_coords:
        b1 = i
        for j in my_design.uv_coords:
            if i[0] == j[0] and i[1] == j[1]:
                continue
            b2 = j
            d1 = np.sqrt((b1[0] - b2[0])**2 + (b1[1] - b2[1])**2) # both are positive
            d2 = np.sqrt((-b1[0] - b2[0])**2 + (-b1[1] - b2[1])**2) # one is negative
            d = np.min([d1, d2])
            if d < 2*uv_rad:
                test_uvs = np.random.uniform(low=0, high=2*uv_rad, size=(2,n))
                dist_b1 = np.sqrt((test_uvs[0,:] - uv_rad)**2 + (test_uvs[1,:] - uv_rad)**2)
                dist_b2 = np.sqrt((test_uvs[0,:] - (uv_rad + d))**2 + (test_uvs[1,:] - (uv_rad))**2)
                count1 = (dist_b1 <= uv_rad).sum()
                count2 = 0
                for q in range(n):
                    if dist_b1[q] <= uv_rad and dist_b2[q] < uv_rad:
                        count2 += 1
                red = 100 * np.round(count2 / count1, 2)
                if red > 0:
                    return 1
    return 0
