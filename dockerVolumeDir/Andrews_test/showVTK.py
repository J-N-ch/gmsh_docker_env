import pyvista as pv

# read the data
#grid = pv.read('2D_polygon_test.vtk')
#grid = pv.read('3D_test.vtk')
grid = pv.read('3D_refineBall_test.vtk')

# plot the data with an automatically created Plotter
grid.plot(show_edges=True)
