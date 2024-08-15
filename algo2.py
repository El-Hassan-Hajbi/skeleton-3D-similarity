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

def test():
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





def n26_neighbors(x, voxelsGrid):
    neighbors=[]
    for voxel in voxelsGrid.get_voxels():
        y = voxel.grid_index
        if Dinf(x,y)==1:
            neighbors.append(y)
    return neighbors

def is_in_list(voxel_grid_index, neighbors_list):
  """Checks if a voxel grid index is present in a list of neighbors.

  Args:
    voxel_grid_index: A NumPy array representing the voxel grid index.
    neighbors_list: A list of NumPy arrays representing neighbor grid indices.

  Returns:
    True if the voxel grid index is found in the neighbors list, False otherwise.
  """

  neighbors_tuples = [tuple(neighbor) for neighbor in neighbors_list]
  return tuple(voxel_grid_index) in neighbors_tuples

def remove_array(array_to_remove, list_of_arrays):
  """Removes a NumPy array from a list of NumPy arrays.

  Args:
    array_to_remove: The NumPy array to remove.
    list_of_arrays: The list of NumPy arrays.

  Returns:
    A new list without the removed array.
  """

  return [array for array in list_of_arrays if not np.array_equal(array, array_to_remove)]

def n6_neighbors_outside(center, voxelsGrid):
    neighbors=[]
    for dx, dy, dz in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
        neighbors.append(center + np.array([dx, dy, dz]))
    #print(len(neighbors))
    for voxel in voxelsGrid.get_voxels():
        if is_in_list(voxel.grid_index, neighbors):
            neighbors=remove_array(voxel.grid_index, neighbors)
    #print(len(neighbors))

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

import connected_components as CC

if __name__ == "__main__":
    file_path = "038262402.obj"
    import time
    # 2 : Voxelise 3D model
    """
    occupancy : numpy 3D array containing zeros and ones.
    """
    occupancy, voxelsGrid = algo1.mesh_to_voxels(file_path, visualise_o3d=False)
    voxel_index = np.array([6,1,5])
    def test_neighbors(x):
        n26_neighbors(x, voxelsGrid)
    start = time.time()
    
    test_neighbors(voxel_index)
    print(time.time()-start)
    import open3d as o3d
    def fill_voxel_grid(voxels_grid,voxel_index):
        voxel_grid = o3d.geometry.VoxelGrid()
        voxel_grid.voxel_size = voxels_grid.voxel_size
        voxel_grid.origin = voxels_grid.origin
        neighbors = n6_neighbors_outside(voxel_index, voxels_grid)
        #for voxel in voxels_grid.get_voxels():
        new_voxel = o3d.geometry.Voxel(grid_index=voxel_index, color=np.array([255, 0, 0]))
        voxel_grid.add_voxel(new_voxel)
        for voxel_idx in neighbors:
            new_voxel = o3d.geometry.Voxel(grid_index=voxel_idx, color=np.array([0, 0, 255]))
            voxel_grid.add_voxel(new_voxel)
        return voxel_grid

    # Assuming you have a valid voxelsGrid here
    new_voxel_grid = fill_voxel_grid(voxelsGrid, voxel_index)

    # Check if the new voxel grid has voxels
    #if len(new_voxel_grid.get_voxels()) > 0:
    #    o3d.visualization.draw_geometries([new_voxel_grid])
    #else:
    #    print("New voxel grid is empty.")

    Y = n26_neighbors(voxel_index, voxelsGrid)
    #print(Y)
    class Vertices():
        def __init__(self, grid_idx, vertex):
            self.grid_idx = grid_idx
            self.vertex = vertex

    adj={}
    V = []
    idx = 1
    for y in Y:
        V.append(Vertices(grid_idx=y, vertex=idx))
        idx+=1
    
    for v1 in V:
        neighbors=[]
        for v2 in V:
            if Dinf(v1.grid_idx,v2.grid_idx)==1:
                neighbors.append(v2.vertex)
        adj[v1.vertex]=neighbors
    print(adj)
    vertices = [v.vertex for v in V]
    print(vertices)
    
    print(CC.find_connected_components(vertices, adj))
    
    def C_star(x, voxelgrid):
        # find 26-neighbors in the voxelised 3D model
        Y = n26_neighbors(x, voxelgrid)
        # Transform this set into vertices and adjacency matrix (the definition of adjacent depends on n)
        adj={}
        V = []
        idx = 1
        for y in Y:
            V.append(Vertices(grid_idx=y, vertex=idx))
            idx+=1
        for v1 in V:
            neighbors=[]
            for v2 in V:
                if Dinf(v1.grid_idx,v2.grid_idx)==1:
                    neighbors.append(v2.vertex)
            adj[v1.vertex]=neighbors
        vertices = [v.vertex for v in V]
        # Calculate the number of 26 connected components 
        nbr_CC = CC.find_connected_components(vertices, adj)
        
        return nbr_CC
    
    def C_(x, voxelgrid):
        # find 26-neighbors in the voxelised 3D model
        Y = n6_neighbors_outside(x, voxelgrid)
        # Transform this set into vertices and adjacency matrix (the definition of adjacent depends on n)
        adj={}
        V = []
        idx = 1
        for y in Y:
            V.append(Vertices(grid_idx=y, vertex=idx))
            idx+=1
        for v1 in V:
            neighbors=[]
            for v2 in V:
                if D1(v1.grid_idx,v2.grid_idx)==1:
                    neighbors.append(v2.vertex)
            adj[v1.vertex]=neighbors
        vertices = [v.vertex for v in V]
        # Calculate the number of 6 connected components 
        nbr_CC = CC.find_connected_components(vertices, adj)
        
        return nbr_CC
    
    print(C_(voxel_index, voxelsGrid))

    voxel_grid = o3d.geometry.VoxelGrid()
    voxel_grid.voxel_size = voxelsGrid.voxel_size
    voxel_grid.origin = voxelsGrid.origin
    
    idx=0
    SBP = []
    for voxel in voxelsGrid.get_voxels():
        print(f"Processing voxel number {idx}")
        idx+=1
        c_ = C_(voxel.grid_index, voxelsGrid)
        c_star = C_star(voxel.grid_index, voxelsGrid)
        if c_ == 2 and c_star == 1: # surface points
            new_voxel = o3d.geometry.Voxel(grid_index=voxel.grid_index, color=np.array([255, 0, 0]))
            SBP.append(voxel.grid_index)
            voxel_grid.add_voxel(new_voxel)
        if c_ == 1 and c_star == 1: # border (simple) points
            new_voxel = o3d.geometry.Voxel(grid_index=voxel.grid_index, color=np.array([0, 0, 255]))
            SBP.append(voxel.grid_index)
            voxel_grid.add_voxel(new_voxel)

        if c_ == 1 and c_star > 2\
            or c_ == 2 and c_star > 2\
            or c_ > 2 and c_star == 1\
            or c_ > 2 and c_star >= 2: # junction points
            new_voxel = o3d.geometry.Voxel(grid_index=voxel.grid_index, color=np.array([0, 255, 0]))
            voxel_grid.add_voxel(new_voxel)

        if c_ == 1 and c_star == 2: # curve points
            new_voxel = o3d.geometry.Voxel(grid_index=voxel.grid_index, color=np.array([100, 100, 100]))
            voxel_grid.add_voxel(new_voxel)
        #else : 
        #    new_voxel = o3d.geometry.Voxel(grid_index=voxel.grid_index, color=np.array([0, 255, 0]))
        #    voxel_grid.add_voxel(new_voxel)

    if len(voxel_grid.get_voxels()) > 0:
        o3d.visualization.draw_geometries([voxel_grid])
    else:
        print("New voxel grid is empty.")
    #test()
      
    """for p in SBP: # contains all surface and border points
        neighbors=[]
        for v in SBP:
            if Dinf(p,v)==1:
                neighbors.append(v)"""

