from mask_testing_pipeline import x_choose_y
import numpy as np

class design:
    def __init__(self, nholes, hrad, xy_coords, uv_coords):
        self.nholes = nholes
        self.hrad = hrad
        self.xy_coords = np.empty([nholes, 2])
        self.uv_coords = np.empty([x_choose_y(self.nholes, 2), 2])
        
    def make_uv_coords(self, uv_coords):
        count = 0
        for i in range(self.nholes):
            xy1 = self.xy_coords[i]
            for j in range(self.nholes):
                if (i == j) or (j < i):
                    continue
                xy2 = self.xy_coords[j]
                u = np.abs(np.sqrt(xy1[0] - xy2[0]))
                v = np.abs(np.sqrt(xy1[1] - xy2[1]))
                uv_coords[count, :] = [u, v]
                count += 1
        self.uv_coords = uv_coords
        return self.uv_coords

    def get_uvs(self):
        self.uv_coords = self.make_uv_coords(self.uv_coords)
        return self.uv_coords

                