# ------------------------------------------# 
# Standard Imports
# ------------------------------------------# 


# ------------------------------------------# 
# Custom Imports
# ------------------------------------------# 

from utils.all_imports import *
from utils.testing_features.compute_wind_generation import *
from utils.testing_features.create_toy_data import *


SEED = 42
N = 100

def main():
  
  # Get Toy input data
  U_nom, R_stat, R_rot, R_app, X_Dsr, s = get_toy_input_data()

  # Get Dicts for displaying Unit Measures
  var_uim_dict = get_dict_unit_measures_input_data()
  res_uim_dict = get_dict_unit_measures_results()

  It = compute_It(U_nom, R_stat, R_rot, R_app, s, X_Dsr)
  print("%.2f %s" % (It, res_uim_dict['It']))
  pass

if __name__ == "__main__":

  random.seed(SEED)
  np.random.seed(seed=SEED)
  
  main()
  pass
  