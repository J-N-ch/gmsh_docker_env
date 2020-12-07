
import meshio

filename = "2D_polygon_test.vtk"

mesh = meshio.read(
    filename,  # string, os.PathLike, or a buffer/open file
    file_format="vtk", # optional if filename is a path; inferred from extension
)

print(mesh.cells_dict['triangle'])

