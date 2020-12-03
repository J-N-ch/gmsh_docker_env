import pygmsh

with pygmsh.geo.Geometry() as geom:
    geom.add_polygon(
        [
            [0.0, 0.0],
            [1.0, -0.2],
            [1.1, 1.2],
            [0.1, 0.7],
        ],
        mesh_size=0.1,
    )
    mesh = geom.generate_mesh()

# mesh.points, mesh.cells, ...
# mesh.write("out.vtk"et hlsearch
mesh.write("2D_polygon_test.vtk")

