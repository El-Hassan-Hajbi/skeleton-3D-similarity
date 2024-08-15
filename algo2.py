"""

"""

import algo1
def get_simple_points(voxel_grid):
    """
    This function takes as arguments a grid of voxels from open3D and returns the indices of voxels that are corresponding to topologically simple points
    """

    voxels = voxel_grid.get_voxels()

    for voxel in voxels:
        """
        attributs:
        voxel.grid_index
        voxel.color
        """


        # Search for 26-connected components in O intersect N_26*

    

"""
Step 1 : Indentify all manifolds comprised of 26 components surface points and border points
"""

def get_type(point):
    if point.C == 1 and point.C_ == 1:
        return "simple"
    pass
import numpy as np
if __name__ == "__main__":
    file_path = "mesh/vis/038262402.obj"

    # 2 : Voxelise 3D model
    """
    occupancy : numpy 3D array containing zeros and ones.
    """
    occupancy, voxelsGrid = algo1.mesh_to_voxels(file_path, visualise_o3d=False)
    x = np.array([6,0,5])
    def D1(x,y):
        """
        returns sum of absolute (yi-xi) for i in 1,..3
        """
        return np.sum(np.abs(x-y))
    
    def Dinf(x,y):
        """
        return max (yi-xi) for i in 1,..3
        """
        return np.max(np.abs(x-y))
    


    

    def n26_neighbors(x):
        neighbors=[]
        for voxel in voxelsGrid.get_voxels():
            y = voxel.grid_index
            if Dinf(x,y)==1:
                neighbors.append(y)
        return neighbors
    

    def is_26_adjacent(X,Y):
        """
        input : two voxels subsets
        output : boolean
        """
        for x in X:
            for y in Y:
                if Dinf(x,y)==1: # x and y are 26 neighbors
                    return True
                
        return False
    
    def find_26_path(x,y):
        # start with x, then append to the path an element from the set of 26 x-adjacent. 
        next=[x] # each element of next is a voxel 
        visited=[x]
        while len(next)>=1:
            new = []
            if y in next:
                return True
            for elt in next:
                for adj in n26_neighbors(elt):
                    if adj.tolist() not in visited:
                        new.append(adj.tolist())
                        visited.append(adj.tolist())
            next=new
        return False


    def is_26_connected(X):
        for x in X:
            for y in X:
                if not find_26_path(x.tolist(),y.tolist()):
                    return False
        return True


    X = [[5, 0, 5],
        [5, 0, 4],
        [6, 1, 4],
        [6, 0, 4],
        [7, 1, 5],
        [7, 1, 4],
        [7, 0, 4],
        [7, 0, 5],
        [7, 1, 6],
        [7, 0, 6],
        [5, 1, 4],
        [6, 0, 6],
        [5, 0, 6]]
    
    
    # As an example lets find all N26 = V1inf of x defined before 
    for voxel in voxelsGrid.get_voxels():
        x = voxel.grid_index
        X = n26_neighbors(x)
        print(is_26_connected(X))
