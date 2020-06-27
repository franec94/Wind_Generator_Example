from utils.all_imports.py import *

# -------------------------------------------------------------- #
# Calculate It (Ampere)
# -------------------------------------------------------------- #

def compute_It_by_row(vector: np.ndarray) -> float:
    U_nom, R_stat, R_rot, R_app, s, X_Dsr = vector
    return compute_It(U_nom, R_stat, R_rot, R_app, s, X_Dsr)


def compute_It_by_X(X: np.ndarray) -> float:
    U_nom, R_stat, R_rot, R_app, s, X_Dsr = X[:, 0], X[:, 1], X[:, 2], X[:, 3], X[:, 4], X[:, 5]

    assert all(xi < 0 for xi in s), "Error input argument 's' was greater than zero"
    
    # Compute Numerator
    numerator = U_nom / np.sqrt(3)

    # Compute Denominator
    d1 = np.power(R_stat + (R_rot+R_app)/s, 2)
    d2 = np.power(X_Dsr, 2)
    denominator = np.sqrt(d1 + d2)

    try:
        # Return result
        return numerator / denominator
    except Exception as err:
        # Manage Division by Zero Exception
        print(str(err), file=sys.stderr)
        sys.exit(-1)
        pass


def compute_It(U_nom: float, R_stat: float, R_rot: float, R_app: float, s: float, X_Dsr: float) -> float:

    assert s < 0, "Error input argument 's' was greater than zero"

    # Compute Numerator
    numerator = U_nom / np.sqrt(3)

    # Compute Denominator
    d1 = np.power(R_stat + (R_rot+R_app)/s, 2)
    d2 = np.power(X_Dsr, 2)
    denominator = np.sqrt(d1 + d2)

    # pprint([numerator, denominator, d1, d2])
    logging.debug([numerator, denominator, d1, d2])
    try:
        # Return result
        return numerator / denominator
    except Exception as err:
        # Manage Division by Zero Exception
        print(str(err), file=sys.stderr)
        sys.exit(-1)
        pass
    pass


# -------------------------------------------------------------- #
# Calculate Pmecc (Watt)
# -------------------------------------------------------------- #

def compute_P_mecc_by_X(X: np.ndarray) -> np.ndarray:
        
    R_stat, R_rot, s, It = X[:, 0], X[:, 1], X[:, 2], X[:, 3]

    assert all(xi < 0 for xi in s), "Error input argument 's' was greater than zero"

    try:
        # Return result
        return 3 * ((1-s) / s) * (R_rot+R_app) * It ** 2
    except Exception as err:
        # Manage Division by Zero Exception
        print(str(err), file=sys.stderr)
        sys.exit(-1)
        pass
    pass

def compute_P_mecc_by_V(R_stat: np.ndarray, R_rot: np.ndarray, s: np.ndarray, It: np.ndarray) -> np.ndarray:
    assert s < 0, "Error input argument 's' was greater than zero"

    try:
        # Return result
        return 3 * ((1-s) / s) * (R_rot+R_app) * It ** 2
    except Exception as err:
        # Manage Division by Zero Exception
        print(str(err), file=sys.stderr)
        sys.exit(-1)
        pass
    pass

def compute_P_mecc(R_stat: float, R_rot: float, s: float, It: float) -> float:
    assert s < 0, "Error input argument 's' was greater than zero"

    try:
        # Return result
        return 3 * ((1-s) / s) * (R_rot+R_app) * It ** 2
    except Exception as err:
        # Manage Division by Zero Exception
        print(str(err), file=sys.stderr)
        sys.exit(-1)
        pass
    pass

# -------------------------------------------------------------- #
# Calculate P_gap (Watt)
# -------------------------------------------------------------- #

def compute_P_gap_by_X(X: np.ndarray) -> np.ndarray:
        
    R_stat, R_rot, s, It = X[:, 0], X[:, 1], X[:, 2], X[:, 3]

    assert all(xi < 0 for xi in s), "Error input argument 's' was greater than zero"

    try:
        # Return result
        return 3 / s * (R_rot+R_app) * It ** 2
    except Exception as err:
        # Manage Division by Zero Exception
        print(str(err), file=sys.stderr)
        sys.exit(-1)
        pass
    pass

def compute_P_gap_by_V(R_stat: np.ndarray, R_rot: np.ndarray, s: np.ndarray, It: np.ndarray) -> np.ndarray:
    assert s < 0, "Error input argument 's' was greater than zero"

    try:
        # Return result
        return 3 / s * (R_rot+R_app) * It ** 2
    except Exception as err:
        # Manage Division by Zero Exception
        print(str(err), file=sys.stderr)
        sys.exit(-1)
        pass
    pass

def compute_P_gap(R_stat: float, R_rot: float, s: float, It: float) -> float:
    assert s < 0, "Error input argument 's' was greater than zero"

    try:
        # Return result
        return 3 / s * (R_rot+R_app) * It ** 2
    except Exception as err:
        # Manage Division by Zero Exception
        print(str(err), file=sys.stderr)
        sys.exit(-1)
        pass
    pass

# -------------------------------------------------------------- #
# Calculate Power: P_jrot, P_jsta, and, P_cbe (Watt)
# -------------------------------------------------------------- #

def compute_Power_by_X(X: np.ndarray) -> np.ndarray:
        
    R, It = X[:, 0], X[:, 1]

    assert all(xi < 0 for xi in s), "Error input argument 's' was greater than zero"

    try:
        # Return result
        return 3 * R * It ** 2
    except Exception as err:
        # Manage Division by Zero Exception
        print(str(err), file=sys.stderr)
        sys.exit(-1)
        pass
    pass

def compute_Power_by_V(R: np.ndarray, It: np.ndarray) -> np.ndarray:
    assert s < 0, "Error input argument 's' was greater than zero"

    try:
        # Return result
        return 3 * R * It ** 2
    except Exception as err:
        # Manage Division by Zero Exception
        print(str(err), file=sys.stderr)
        sys.exit(-1)
        pass
    pass

def compute_Power(R_stat: float, R_rot: float, s: float, It: float) -> float:

    try:
        # Return result
        return 3 * R * It ** 2
    except Exception as err:
        # Manage Division by Zero Exception
        print(str(err), file=sys.stderr)
        sys.exit(-1)
        pass
    pass
