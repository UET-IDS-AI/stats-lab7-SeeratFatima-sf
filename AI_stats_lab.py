import numpy as np

def uniform_analysis(a, n_samples=10000):
    theoretical_mean = a / 2
    theoretical_variance = (a ** 2) / 12

    x = np.random.uniform(0, a, n_samples)
    sample_mean = np.mean(x)
    sample_variance = np.var(x)

    mean_error = abs(sample_mean - theoretical_mean)
    variance_error = abs(sample_variance - theoretical_variance)

    # Theoretical values for Z = 2X + 1
    # E[Z] = 2*E[X] + 1 = a + 1
    # Var[Z] = 4 * Var[X] = 4 * (a^2 / 12) = a^2 / 3
    transformed_mean = a + 1                  # was: np.mean(2 * x + 1)
    transformed_variance = (a ** 2) / 3       # was: np.var(2 * x + 1)

    return (
        theoretical_mean,
        theoretical_variance,
        sample_mean,
        sample_variance,
        mean_error,
        variance_error,
        transformed_mean,
        transformed_variance
    )
