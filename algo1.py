from voxelisation import mesh_to_voxels, numpyArrayGrid_to_VoxelGrid
from EDT import get_EDT, central_difference_gradient
from skimage import measure
import open3d as o3d

def get_AOF(grid, gradD):
    """
    Calculates the average over 26 interior neighbors for each voxel.

    Args:
        grid: A 3D numpy array representing your grid.
        vector: The vector used to calculate the scalar product.

    Returns:
        A 3D numpy array of the same shape as the input grid, with values
        representing the calculated averages for each interior voxel.
    """

    result = np.zeros(grid.shape, dtype=np.float64)  # Initialize result array

    x_dim, y_dim, z_dim = grid.shape

    # Iterate through all interior voxels
    for x in range(1, x_dim - 1):
        for y in range(1, y_dim - 1):
            for z in range(1, z_dim - 1):
                total = 0.0
                neighbor_count = 0

                # Iterate within a 3x3x3 cube, considering all 26 neighbors
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        for k in range(-1, 2):
                            xi, yi, zi = x + i, y + j, z + k

                            # Exclude the center voxel itself
                            if not (i == 0 and j == 0 and k == 0):
                                neighbor_val = grid[xi, yi, zi]
                                outward_normal = np.array([xi - x, yi - y, zi - z])
                                normalized_normal = outward_normal / np.linalg.norm(outward_normal)
                                vector = np.array([gradD[0][xi,yi,zi], gradD[1][xi,yi,zi], gradD[2][xi,yi,zi]])
                                scalar_product = np.dot(vector, normalized_normal)

                                total += scalar_product * neighbor_val
                                neighbor_count += 1
                #if (total / neighbor_count<0):
                #    result[x, y, z] = 1
                #else:
                if (total / neighbor_count <-0.19):
                    result[x,y,z]= 0
                else:    
                    result[x, y, z] = 1
                #result[x, y, z] = total / neighbor_count
    print(np.min(result))
    return result






if __name__ == "__main__":
    import trimesh
    import numpy as np

    # 1 : Load mesh
    file_path = "038262402.obj"
    file_path = "nve7881601_0_2.obj"

    # 2 : Voxelise 3D model
    """
    occupancy : numpy 3D array containing zeros and ones.
    """
    occupancy, voxelsGrid = mesh_to_voxels(file_path, visualise_o3d=False)
    #occupancy = np.load("occupancy.npy")
    #print(occupancy.shape)
    # 3.a : Euclidian Distance Transform
    D = get_EDT(occupancy)

    # 3.b : Gradient of EDT
    gradD = central_difference_gradient(D)
    #print(gradD)

    # 4 : Average Outward Flux Map
    AOF = get_AOF(occupancy, gradD)
    #print(AOF.shape)
    #print(AOF[10,18,10])

    voxels = numpyArrayGrid_to_VoxelGrid(AOF, voxelsGrid)
    #print(voxels.get_voxels())
    o3d.visualization.draw_geometries([voxels])

    

  
    
    



    