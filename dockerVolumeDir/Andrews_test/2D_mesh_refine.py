# mesh refinement with callback
import pygmsh

with pygmsh.geo.Geometry() as geom:
    geom.add_polygon(
        [
            [-1.0, -1.0],
            [+1.0, -1.0],
            [+1.0, +1.0],
            [-1.0, +1.0],
        ]
    )
    geom.set_mesh_size_callback(
        lambda dim, tag, x, y, z: 6.0e-2 + 2.0e-1 * (x ** 2 + y ** 2)
    )

    mesh = geom.generate_mesh()

mesh.write("2D_mesh_refine_test.vtk")
