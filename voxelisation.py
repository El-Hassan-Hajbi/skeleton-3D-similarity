import open3d as o3d
import numpy as np
import trimesh
from skimage import measure

def mesh_to_voxels(file_path, visualise_o3d=False):
    mesh  = o3d.io.read_triangle_mesh(file_path)

    # fit to unit cube
    mesh.scale(1 / np.max(mesh.get_max_bound() - mesh.get_min_bound()),
            center=mesh.get_center())
    
    print('------------ voxelization ------------------')

    voxel_grid = o3d.geometry.VoxelGrid.create_from_triangle_mesh(mesh,
                                                                voxel_size=0.05)
    
    if visualise_o3d:
        o3d.visualization.draw_geometries([voxel_grid])
    
    list_voxels = voxel_grid.get_voxels()
    maxx,maxy,maxz = get_grid_shape(list_voxels)

    grid_shape=(maxx+1, maxy+1, maxz+1)
    occupancy = np.zeros(grid_shape, dtype=np.int32)
    list_voxels = voxel_grid.get_voxels()
    for voxel in list_voxels:
        x,y,z = voxel.grid_index
        occupancy[x,y,z] = 1
    #print(voxel_grid.get_voxels())
    return occupancy, voxel_grid

def numpyArrayGrid_to_VoxelGrid(occupancy, voxels):    
    
                
    voxelgrid = o3d.geometry.VoxelGrid(voxels)
    list_voxels = voxelgrid.get_voxels()
    for voxel in list_voxels:
        x,y,z = voxel.grid_index
        color = np.array([occupancy[x,y,z]]*3)
        voxelgrid.remove_voxel(np.array([x,y,z]))
        voxelgrid.add_voxel(o3d.geometry.Voxel(np.array([x,y,z]), color))
    return voxelgrid


def get_grid_shape(list_voxels):
    minx,maxx=100,0
    miny,maxy=100,0
    minz,maxz=100,0
    for voxel in list_voxels:
        x,y,z = voxel.grid_index
        if minx > x:
            minx = x
        if maxx < x:
            maxx = x

        if miny > y:
            miny = y
        if maxy < y:
            maxy = y
        if minz > z:
            minz = z
        if maxz < z:
            maxz = z

    return maxx,maxy,maxz

if __name__ == "__main__":

    file_path1 = "mesh/vis/038262402.obj"
    file_path2 = "mesh/vis/nve7881601_0_2.obj"
    
    
    occupancy1, voxels1 = mesh_to_voxels(file_path1, visualise_o3d=False)
    occupancy2, voxels2 = mesh_to_voxels(file_path2, visualise_o3d=False)
    """
    voxels2.rotate(R=np.array([
                                [-1, 0, 0],
                                [0, -1, 0],
                                [0, 0, -1]
                            ]),
                               center=voxels2.get_center())

    """
                            

    for voxel in voxels2.get_voxels():
        x, y, z = voxel.grid_index
        color = np.array([0,0,255])
        voxels1.add_voxel(o3d.geometry.Voxel(np.array([x,y,z]), color))

    #o3d.visualization.draw_geometries([voxels1])
    union = len(voxels1.get_voxels())+len(voxels2.get_voxels())
    intersection = 0
    for v1 in voxels1.get_voxels():
        for v2 in voxels2.get_voxels():
            if (v1.grid_index - v2.grid_index).all:
                intersection+=1
    print(intersection/(union-intersection))

    #np.save('occupancy.npy', occupancy)

    # Use the marching cubes algorithm
    #verts, faces, normals, values = measure.marching_cubes(occupancy, 0.25)

    # Export in a standard file format
    #surf_mesh = trimesh.Trimesh(verts, faces, validate=True)
    #surf_mesh.export('test_mesh.off')

    #voxelgrid = numpyArrayGrid_to_VoxelGrid(occupancy, voxels)
    #print(voxelgrid.get_voxels())
    #o3d.visualization.draw_geometries([voxelgrid])