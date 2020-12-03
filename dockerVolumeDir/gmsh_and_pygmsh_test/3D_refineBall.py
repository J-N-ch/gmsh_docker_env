# ball with mesh refinement
from math import sqrt
import pygmsh


with pygmsh.occ.Geometry() as geom:
    geom.add_ball([0.0, 0.0, 0.0], 10.0)

    geom.set_mesh_size_callback(
        lambda dim, tag, x, y, z: 0.5*abs(sqrt(x ** 2 + y ** 2 + z ** 2) - 0.5) + 0.1
    )
    mesh = geom.generate_mesh()
mesh.write("3D_refineBall_test.vtk")
