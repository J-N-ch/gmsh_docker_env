
import meshio

filename = "2D_polygon_test.vtk"

mesh = meshio.read(
    filename,  # string, os.PathLike, or a buffer/open file
    file_format="vtk", # optional if filename is a path; inferred from extension
)

print(mesh.cells_dict)
print(mesh.cells_dict['triangle'])

points = mesh.points

cells = [("triangle", mesh.cells_dict['triangle'])]
meshio.write_points_cells(
    "foo.msh",
    #"foo.stl,
    points,
    cells,
    # Optionally provide extra data on points, cells, etc.
    # point_data=point_data,
    # cell_data=cell_data,
    # field_data=field_data
)
