from utils.all_imports import *
from utils.testing_features.create_toy_data import *
from utils.testing_features.compute_wind_generation import *


def get_data_matrix_X(nrows: int, ncols: int, verbose: int = 0):
  U_nom, R_stat, R_rot, R_app, X_Dsr, s = get_toy_input_data()
  X = create_data_matrix(rows=nrows, cols=ncols, U_nom=U_nom, R_stat=R_stat, R_rot=R_rot, R_app=R_app, s=s, X_Dsr=X_Dsr)

  cols_X = "U_nom,R_stat,R_rot,R_app,s,X_Dsr".split(',')
  df_X = pd.DataFrame(data=X, columns=cols_X)

  if verbose == 1:
    print(df_X.head())
  return X, df_X


def get_It_results(X: np.ndarray, df_X: pd.DataFrame, verbose: int = 0):
  It_v = compute_It_by_X(X)

  df_It = pd.DataFrame(data=It_v[:, np.newaxis], columns=['It'])
  df_X_It = pd.concat([df_X, df_It], axis=1)
  
  if verbose == 1:
    print(df_X_It.head())
  
  return It_v, df_X_It


def get_Pmecc_results(df_X_It: pd.DataFrame, verbose: int = 0):

  target_cols = 'R_app,R_rot,s,It'.split(',')
  X_mecc = df_X_It[target_cols].values
  Pmecc_v = compute_P_mecc_by_X(X=X_mecc)
  
  It_v = df_X_It['It'].values


  df_Pmecc = pd.DataFrame(data=Pmecc_v[:, np.newaxis], columns=['Pmecc'])
  df_It = pd.DataFrame(data=It_v[:, np.newaxis], columns=['It'])
  df_results = pd.concat([df_It, df_Pmecc], axis=1)

  if verbose == 1:
    print(df_results.head())
  
  return Pmecc_v, df_results


def get_P_gap_results(df_X_It: pd.DataFrame, verbose: int = 0):
  It_v = df_X_It['It'].values

  target_cols = 'R_stat,R_rot,s,It'.split(',')
  X_gap = df_X_It[target_cols].values
  P_gap_v = compute_P_gap_by_X(X=X_gap)

  df_P_gap_v = pd.DataFrame(data=P_gap_v[:, np.newaxis], columns=['P_gap'])
  df_It = pd.DataFrame(data=It_v[:, np.newaxis], columns=['It'])

  # df_results = pd.concat([df_It, df_P_gap_v], axis=1)
  df_X_gap = df_X_It[target_cols]
  df_results = pd.concat([df_X_gap, df_P_gap_v], axis=1)

  if verbose == 1:
    print(df_results.head())
  return P_gap_v, df_X_gap

def run_simulation(n: int = 100, verbose: int = 0):

  assert n > 0, "Number of instances 'n' should be strictly positive"

  rows, cols = n, 6
  X, df_X = get_data_matrix_X(nrows=rows, ncols=cols, verbose=verbose)

  It_v, df_X_It = get_It_results(X=X, df_X=df_X, verbose=verbose)

  Pmecc_v, df_results = get_Pmecc_results(df_X_It=df_X_It, verbose=verbose)

  P_gap_v, df_X_gap = get_P_gap_results(df_X_It, verbose=verbose)
  pass