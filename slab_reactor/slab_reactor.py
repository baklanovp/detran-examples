# pyexamples/slab_reactor/slab_reactor.py
#
# This implements the test cases published in Scott Mosher's
# Ph.D. thesis, "A Variational Coarse Mesh Transport Method".
# All data and reference values are from Appendix A of that 
# work.
#
#   Core     keff
#   =====   =========
#     1     1.258247 
#     2     1.007066 
#     3     0.805372
#
# These results are based on a 32-point Gauss-Legendre,
# 2 meshes per water region, 4 meshes per fuel region.
#
# Note, the assembly kinf's were found using the same
# parameters to be 
#
#   Assembly     kinf
#   ========   =========
#      A       1.329576914
#      B       1.298737436
#      C       0.681362819
#      D       0.191909997

import sys
sys.path.insert(0, '../')
import config

from detran import *
import slab_reactor_materials
import slab_reactor_geometry
import time

def run() :

  #------------------------------------------------------------------------------#
  # Initialize
  #------------------------------------------------------------------------------#

  Manager.initialize(sys.argv)

  #------------------------------------------------------------------------------#
  # Input
  #------------------------------------------------------------------------------#

  inp = InputDB.Create()
  inp.put_str("problem_type",               "eigenvalue")
  inp.put_int("number_groups",              2)
  inp.put_str("equation",                   "dd")
  inp.put_str("inner_solver",               "SI")
  inp.put_int("inner_max_iters",            1000)
  inp.put_dbl("inner_tolerance",            1e-7)
  inp.put_int("inner_print_level",          0)
  inp.put_str("outer_solver",               "GS")
  inp.put_int("outer_max_iters",            1000)
  inp.put_dbl("outer_tolerance",            1e-7)
  inp.put_int("outer_print_level",          0)
  inp.put_str("eigen_solver",               "PI")
  inp.put_int("eigen_max_iters",            200)
  inp.put_dbl("eigen_tolerance",            1e-7)
  inp.put_str("bc_west",                    "vacuum")
  inp.put_str("bc_east",                    "vacuum")
  inp.put_str("quad_type",                  "gl")  # gausslegendre
  inp.put_int("quad_number_polar_octant",   16)

  #------------------------------------------------------------------------------#
  # Material
  #------------------------------------------------------------------------------#

  mat = slab_reactor_materials.get_materials()

  #------------------------------------------------------------------------------#
  # Mesh
  #------------------------------------------------------------------------------#

  # Options are: assemblyX for X=0,1,2,3 or coreX for X=0,1,2
  mesh = slab_reactor_geometry.get_mesh("core0")

  #------------------------------------------------------------------------------#
  # Solve
  #------------------------------------------------------------------------------#

  start = time.time()
  solver = Eigen1D(inp, mat, mesh)
  solver.solve()
  elapsed = (time.time() - start)
  print elapsed, " seconds"

if __name__ == "__main__":
  Manager.initialize(sys.argv)
  run()
