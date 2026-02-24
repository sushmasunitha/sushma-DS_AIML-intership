import numpy as np

np.random.seed(42)

X = np.linspace(-5, 5, 100)
y = 3 * (X ** 2) + 2 * X + 5 + np.random.randn(100) * 5

split = int(0.8 * len(X))
X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

def train_linear_regression(X, y):
    X_b = np.c_[np.ones(len(X)), X]   
    theta = np.linalg.inv(X_b.T @ X_b) @ X_b.T @ y
    return theta

def predict(X, theta):
    X_b = np.c_[np.ones(len(X)), X]
    return X_b @ theta

def r2_score(y_true, y_pred):
    ss_total = np.sum((y_true - np.mean(y_true)) ** 2)
    ss_residual = np.sum((y_true - y_pred) ** 2)
    return 1 - (ss_residual / ss_total)

theta_linear = train_linear_regression(X_train.reshape(-1,1), y_train)
y_pred_linear = predict(X_test.reshape(-1,1), theta_linear)

r2_linear = r2_score(y_test, y_pred_linear)

print("R² Score (Original Features):", r2_linear)


X_train_poly = np.c_[X_train, X_train**2]
X_test_poly = np.c_[X_test, X_test**2]

theta_poly = train_linear_regression(X_train_poly, y_train)
y_pred_poly = predict(X_test_poly, theta_poly)

r2_poly = r2_score(y_test, y_pred_poly)

print("R² Score (Polynomial Features):", r2_poly)