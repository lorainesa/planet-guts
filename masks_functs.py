import numpy as np
import matplotlib.pyplot as plt

def check_placement(coords, hrad, rng, aperture):
    """ Check placement of hole

    Called by add_hole(). Checks that a proposed hole doesn't overlap other holes or spiders or mirror segment edges, and that it falls within the Keck aperture. If a hole does not meet requirements, hole is discarded and add_hole() is called again. Repeats until an acceptable hole location is found.

    Args:
        coords (array): numpy array containing the proposed (x,y) coordinates. 
        design (object): Mask design object.
        rng (object): Random number generator.
        aperture (array): numpy array containing a boolean mask of the Keck primary.
    
    Returns:
        numpy array: returns the accepted (x,y) coordinates
    """

    hcoords = 100 * coords + [545, 545] # convert proposed hole center coords to coords in aperture array
    for i in range(1090):
        for j in range(1090):
            if np.sqrt((i - hcoords[0])**2 + (j - hcoords[1])**2) < (100 * hrad):
                if aperture[i, j] == 0:
                    print('Oh no! Bad hole placement :( Trying again!')
                    return 0
    return 1

def add_hole(hrad, rng, aperture):
    """ Propose a new mask hole

    Generates a proposed hole (x,y) coordinate set, then calls check_placement() to check whether these coordinates are acceptable. If they are, then these coordinates are returned. 
    
    Args:
        hrad (float): Hole radius in meters.
        rng (object): Random number generator.
        aperture (array): numpy array containing a boolean mask of the Keck primary.
    
    Returns:
        array: Returns a numpy array of the accepted hole (x,y) coordinates.
    """
    while 1:
        print('Placing hole...')
        rand_nums = rng.integers(low=-100, high=100, size=2)
        coords = (11/2) * rand_nums / 100.
        if check_placement(coords, hrad, rng, aperture) == 1:
            print('Yay! found a good hole placement.')
            return np.array(coords)

def check_redundancy(my_design):
    """ Check mask baselines for redundancy

    Checks for any redundancy in the baselines of the proposed mask design. If redundancy is above 0%, reject the mask design.

    Args:
        my_design (object): An instance of design class. The proposed mask to be tested.

    Returns:
        bool: Returns 1 if the mask has any redundancy, returns 0 if mask is fully non-redundant.
    """

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

def plot_design(my_design, aperture):
    hcoords = 100 * my_design.xy_coords + [545, 545] # convert hole center coords to coords in aperture array
    for i in range(1090):
        for j in range(1090):
            for a in range(my_design.nholes):
                if np.sqrt((i - hcoords[a, 0])**2 + (j - hcoords[a, 1])**2) < (100 * my_design.hrad):
    
                     aperture[i, j] = 0
    plt.figure()
    plt.imshow(aperture)
    plt.colorbar()
    plt.show()