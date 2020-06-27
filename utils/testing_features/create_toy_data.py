from utils.all_imports.py import *

# ---------------------------------------------------------- #
# Create Toy Data
# ---------------------------------------------------------- #

def get_dict_unit_measures_input_data() -> dict:
  var_names = "U_nom,R_stat,R_rot,R_app,X_Dsr".split(',')
  var_unit_measures = "Volt,Ohm,Ohm,Ohm,Ohm".split(',')
  var_uim_dict = dict(zip(var_names, var_unit_measures))
  return var_uim_dict

def get_dict_unit_measures_results() -> dict:
  result_names = "It,P_jrot,P_jstat,P_gbe,P_mecc".split(',')
  result_unit_measures = "Ampere,Watt,Watt,Watt,Watt".split(',')
  res_uim_dict = dict(zip(result_names, result_unit_measures))
  return res_uim_dict


def get_toy_input_data() -> tuple:
  # Toy Input Data
  U_nom = 690  # Volt
  R_stat = 0.009 # Ohm
  R_rot = 0.008  # Ohm
  R_app = 0.017  # Ohm
  X_Dsr = 0.068  # Ohm
  s = -0.13
  return

# ---------------------------------------------------------- #
# Create Toy Dataset
# ---------------------------------------------------------- #

def create_data_matrix_old(rows: int, cols: int, U_nom: float, R_stat: float, R_rot: float, R_app: float, s: float, X_Dsr: float) -> np.ndarray:
    
    assert rows > 0, "Number of rows must be strictly greater than zero"
    assert cols > 0, "Number of columns must be strictly greater than zero"

    deltas_list = [2*1e+2, 2*1e-3, 2*1e-3, 2*1e-3, -1*1e-1, 1e-3]

    U_nom_v = np.linspace(start=U_nom, stop=(U_nom+deltas_list[0]), num=rows, endpoint=True, retstep=False, dtype=None, axis=0)
    R_stat_v = np.linspace(start=R_stat, stop=(R_stat+deltas_list[1]), num=rows, endpoint=True, retstep=False, dtype=None, axis=0)
    R_rot_v = np.linspace(start=R_rot, stop=(R_rot+deltas_list[2]), num=rows, endpoint=True, retstep=False, dtype=None, axis=0)
    R_app_v = np.linspace(start=R_app, stop=(R_app+deltas_list[3]), num=rows, endpoint=True, retstep=False, dtype=None, axis=0)
    s_v = np.linspace(start=s, stop=(s+deltas_list[4]), num=rows, endpoint=True, retstep=False, dtype=None, axis=0)
    X_Dsr_v = np.linspace(start=X_Dsr, stop=(X_Dsr+deltas_list[5]), num=rows, endpoint=True, retstep=False, dtype=None, axis=0)

    res = np.concatenate((U_nom_v, R_stat_v, R_rot_v, R_app_v, s_v, X_Dsr_v))
    assert len(res) == rows * cols

    X = np.zeros((rows, cols))
    for ii in range(cols):
        X[:, ii] = res[ii*rows:(ii+1)*rows]
    return X


def create_data_matrix_new(rows: int, cols: int, U_nom: float, R_stat: float, R_rot: float, R_app: float, s: float, X_Dsr: float, deltas_list: list = None) -> np.ndarray:
    
    assert rows > 0, "Number of rows must be strictly greater than zero"
    assert cols > 0, "Number of columns must be strictly greater than zero"
    
    if deltas_list is None:
        deltas_list = [2*1e+2, 2*1e-3, 2*1e-3, 2*1e-3, -1*1e-1, 1e-3]
    else:
        assert len(deltas_list) == cols, "deltas_list and number of columns mismatch"
        pass

    variables = [U_nom, R_stat, R_rot, R_app, s, X_Dsr]
    pairs_var_delta = list(zip(variables, deltas_list))
    
    X = np.zeros((rows, cols))
    for ii, (var, delta_var) in enumerate(pairs_var_delta):
        X[:, ii] = np.linspace(start=var, stop=(var+delta_var), num=rows, endpoint=True, retstep=False, dtype=None, axis=0)
    return X

def create_data_matrix(rows: int, cols: int, U_nom: float, R_stat: float, R_rot: float, R_app: float, s: float, X_Dsr: float, deltas_list=None, old_version: bool = False) -> np.ndarray:
    if old_version is True:
        return create_data_matrix_old(rows, cols, U_nom, R_stat, R_rot, R_app, s, X_Dsr)

    return create_data_matrix_new(rows, cols, U_nom, R_stat, R_rot, R_app, s, X_Dsr, deltas_list)