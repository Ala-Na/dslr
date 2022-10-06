import numpy as np
from typing import Tuple
import os

class LogisticRegression():
    """
    Description:
        My personnal logistic regression to classify things.
    """

    supported_penalities = ['l2', None]

    def __init__(self, theta: np.ndarray or list, alpha: float = 0.001, \
            max_iter: int = 1000, penalty: str ='l2', lambda_: float = 1.0) \
            -> None:
        assert isinstance(alpha, float)
        assert isinstance(max_iter, int)
        if isinstance(theta, np.ndarray):
            assert np.issubdtype(theta.dtype, np.number)
            self.theta = theta
        else:
            try:
                self.theta = np.asarray(theta).reshape((len(theta), 1))
                assert np.issubdtype(self.theta.dtype, np.number)
            except:
                raise ValueError("Thetas not valid")
        self.alpha = alpha
        self.max_iter= max_iter
        assert penalty in self.supported_penalities
        assert isinstance(lambda_, float)
        self.penalty = penalty
        self.lambda_ = lambda_ if penalty != None else 0
        if self.lambda_ < 0:
            raise ValueError("Lambda must be positive")

    def predict(self, x: np.ndarray) -> np.ndarray:
        if not isinstance(x, np.ndarray) \
                or not np.issubdtype(x.dtype, np.number) or x.ndim != 2 \
                or x.shape[0] == 0 or x.shape[1] != self.theta.shape[0] - 1:
            return None
        X = np.insert(x, 0, 1.0, axis=1)
        return 1 / (1 + np.exp(-X @ self.theta))


    def cost(self, y: np.ndarray, y_hat: np.ndarray) \
            -> np.ndarray or None:
        eps=1e-15
        if not isinstance(y, np.ndarray) \
                or not np.issubdtype(y.dtype, np.number) \
                or y.ndim != 2 or y.shape[0] == 0 or y.shape[1] != 1:
            return None
        if not isinstance(y_hat, np.ndarray) \
                or not np.issubdtype(y_hat.dtype, np.number) \
                or y_hat.ndim != 2 or y_hat.shape != y.shape:
            return None
        if not isinstance(eps, float):
            return None
        one_vec = np.ones((1, y.shape[1]))
        m = y.shape[0]
        return ((-1 / m) * (y.T.dot(np.log(y_hat + eps)) \
            + (one_vec - y).T.dot(np.log(one_vec - y_hat + eps))) \
            + ((self.lambda_ / (2 * m)) * self.l2(self.theta))).item()

    def cost_derivative(self, x: np.ndarray, y: np.ndarray) \
            -> np.ndarray or None:
        if not isinstance(x, np.ndarray) \
                or not np.issubdtype(x.dtype, np.number) \
                or x.ndim != 2 or x.size == 0 \
                or x.shape[1] != self.theta.shape[0] - 1:
            return None
        if not isinstance(y, np.ndarray) \
                or not np.issubdtype(y.dtype, np.number) \
                or y.ndim != 2 or y.shape != (x.shape[0], 1):
            return None
        m = y.shape[0]
        X = np.insert(x, 0, 1.0, axis=1)
        y_hat = 1 / (1 + np.exp(-X @ self.theta))
        theta_cp = self.theta.copy()
        theta_cp[0][0] = 0
        return (1 / m) * (X.T.dot(y_hat - y) + self.lambda_ * theta_cp)


    def gradient_descent(self, x: np.ndarray, y: np.ndarray, \
            x_val: np.ndarray or None = None, y_val: np.ndarray or None = None, \
            batch_size: int or None = None) -> Tuple[list, list] or None:
        """
        Batch_size = 1 to run stochastic gradient descent
        x_val and y_val : Validation set to stop training if stable, if not
        present, training will stop once a threshold of 1e-6 is reached between
        two thetas iteration. MSE on validation set is only checked each 100
        epochs to avoid slowing down the training.
        """
        if not isinstance(x, np.ndarray) \
                or not np.issubdtype(x.dtype, np.number) \
                or x.ndim != 2 or x.size == 0 \
                or x.shape[1] != self.theta.shape[0] - 1:
            return None
        if not isinstance(y, np.ndarray) \
                or not np.issubdtype(y.dtype, np.number) \
                or y.ndim != 2 or y.shape != (x.shape[0], 1):
            return None
        if x_val is not None and (not isinstance(x_val, np.ndarray) \
                or not np.issubdtype(x_val.dtype, np.number) \
                or x_val.ndim != 2 or x_val.size == 0 \
                or x_val.shape[1] != self.theta.shape[0] - 1):
            return None
        if y_val is not None and (not isinstance(y_val, np.ndarray) \
                or not np.issubdtype(y_val.dtype, np.number) \
                or y_val.ndim != 2 or y_val.shape != (x_val.shape[0], 1)):
            return None
        if y_val is not None and x_val is not None:
            mse = []
        for i in range(0, self.max_iter):
            x_sample = x
            y_sample = y
            if batch_size != None and batch_size > 0:
                random_idx = np.random.randint(0, x.shape[0], batch_size)
                x_sample = np.take(x, random_idx, axis=0).reshape(batch_size, -1)
                y_sample = np.take(y, random_idx).reshape(batch_size, 1)
            diff = self.alpha \
                * self.cost_derivative(x_sample, y_sample)
            self.theta = self.theta - diff
            if diff.all() < 1e-6:
                break
            if y_val is not None and x_val is not None and i % 100 == 0:
                mse.append(self.mean_squared_error(y_val, \
                self.predict(x_val)))
                if len(mse) >= 2 and mse[-2] - mse[-1] < 1e-6:
                    break
        if y_val is not None and x_val is not None:
            return mse

    def l2(self) -> np.ndarray:
        theta_cp = self.theta.copy()
        theta_cp[0][0] = 0
        return np.sum(theta_cp ** 2)


    def mean_squared_error(self, y: np.ndarray, y_hat: np.ndarray) -> float:
        if not isinstance(y, np.ndarray) \
                or not np.issubdtype(y.dtype, np.number) \
                or y.ndim != 2 or y.shape[1] != 1 or y.shape[0] == 0:
            return None
        if not isinstance(y_hat, np.ndarray) \
                or not np.issubdtype(y_hat.dtype, np.number) \
                or y_hat.ndim != 2 or y_hat.shape[1] != 1 \
                or y_hat.shape[0] != y.shape[0]:
            return None
        mse = ((y_hat - y) ** 2).mean(axis=None)
        return float(mse)

    def save_values_npz(self, filepath='theta.npz') -> None:
        if (os.path.isfile(filepath)):
                os.remove(filepath)
        try:
            np.savez(filepath, theta=self.theta)
        except:
            print("\033[91mOops, can't save values in {} file.\033[0m".format(filepath))

    def get_values_npz(self, filepath='theta.npz') -> None:
        try:
            values = np.load(filepath)
            assert np.issubdtype(values['theta'].dtype, np.number) and values['theta'].shape == self.theta.shape
            self.theta = values['theta']
        except:
            print("\033[91mOops, can't get values from {} file.\033[0m".format(filepath))

    def set_values(self, theta) -> None:
        assert np.issubdtype(theta.dtype, np.number) and theta.shape == self.theta.shape
        self.theta = theta
