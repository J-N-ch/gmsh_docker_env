
import meshio

filename = "3D_test.vtk"

mesh = meshio.read(
    filename,  # string, os.PathLike, or a buffer/open file
    file_format="vtk", # optional if filename is a path; inferred from extension
)

print(mesh.cells_dict)
#print(mesh.cells_dict['triangle'])
print(mesh.cells_dict['tetra'])

points = mesh.points

#cells = [ ("triangle", mesh.cells_dict['triangle']) ]
cells = [ ("tetra", mesh.cells_dict['tetra']) ]

meshio.write_points_cells(
    #"3D_test.msh", # Gmsh file
    "3D_test.inp", # Abaqus file
    points,
    cells,
    # Optionally provide extra data on points, cells, etc.
    # point_data=point_data,
    # cell_data=cell_data,
    # field_data=field_data
)
