import numpy as np
from typing import Tuple

def united_shuffle(x: np.ndarray, y: np.ndarray) \
        -> Tuple[np.ndarray, np.ndarray]:
    p = np.random.permutation(len(x))
    return x[p], y[p]

def data_spliter(x: np.ndarray, y: np.ndarray, proportion: float) \
        -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray] or None:
    """
    Shuffles and splits the dataset (given by x and y) into a training
    and a test set, while respecting the given proportion of examples to
    be kept in the training set.
    Args:
        x: has to be an numpy.array, a matrix of dimension m * n.
        y: has to be an numpy.array, a vector of dimension m * 1.
        proportion: has to be a float, the proportion of the dataset
        that will be assigned to the training set.
    Return:
        (x_train, x_test, y_train, y_test) as a tuple of numpy.array
        None if x or y is an empty numpy.array.
        None if x and y do not share compatible dimensions.
        None if x, y or proportion is not of expected type.
    Raises:
        This function should not raise any Exception.
    """
    if not isinstance(x, np.ndarray) or not np.issubdtype(x.dtype, np.number) \
            or x.ndim != 2 or x.shape[0] == 0 or x.shape[1] == 0:
        return None
    if not isinstance(y, np.ndarray) or not np.issubdtype(y.dtype, np.number) \
            or y.ndim != 2 or y.shape != (x.shape[0], 1):
        return None
    if not isinstance(proportion, float) or proportion > 1 or proportion < 0:
        return None
    ind_split = (int)(x.shape[0] * proportion)
    x, y = united_shuffle(x, y)
    return (x[:ind_split, :], x[ind_split:, :], y[:ind_split, :], \
        y[ind_split:, :])

def scale(x: np.ndarray, option: str ='mean_normalization', \
        lst1: np.ndarray or None = None, lst2: np.ndarray or None = None) \
        -> Tuple[np.ndarray, list, list] or None:
    if lst1 is not None and lst2 is not None:
        assert (lst1.shape[0] == x.shape[1])
        assert (lst2.shape[0] == x.shape[1])
    if option == 'mean_normalization':
        if lst1 is None or lst2 is None:
            lst1 = np.mean(x, axis=0) # means
            lst2 = np.std(x, axis=0) # stds
        x = (x - lst1) / lst2
        return x, lst1, lst2 # scaled array, means, stds
    elif option == 'min_max':
        if lst1 is None or lst2 is None:
            lst1 = np.amin(x, axis=0) # mins
            lst2 = np.amax(x, axis=0) # maxs
        x = (x - lst1) / (lst2 - lst1)
        return x, lst1, lst2 # scaled array, mins, maxs
    elif option == 'robust':
        if lst1 is None or lst2 is None:
            lst1 = np.percentile(x, 25, axis=0) # first quartil
            lst2 = np.percentile(x, 75, axis=0) # third quartil
        x = (x - lst1) / (lst2 - lst1)
        return x, lst1, lst2 # scaled array, first qrt, third
    print('scale option non recognized')
    return None
