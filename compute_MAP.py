import numpy as np
from cmdstanpy import CmdStanModel
import matplotlib.pyplot as plt

# Define the Stan model
stan_model_code = """
data {
    int<lower=0> N;
    vector[N] y;
}
parameters {
    real mu;
}
model {
    y ~ normal(mu, 1.0);
}
"""

# Write the Stan model to a file
with open('model.stan', 'w') as f:
    f.write(stan_model_code)

# Compile the Stan model
stan_model = CmdStanModel(stan_file='model.stan')

# Generate some synthetic data
np.random.seed(1)
N = 100
y = np.random.normal(0, 1, N)

y = np.array([-2., -1., 0., 1., 2.])
N = len(y)
# Prepare data for Stan
data = {'N': N, 'y': y}

# Find the MAP estimate using CmdStanPy's optimize method
map_estimate = stan_model.optimize(data=data)

print("MAP estimate of mu:", map_estimate.stan_variable('mu'))

# Define the log-posterior function
def log_posterior(mu, y):
    sigma = 1.0
    N = len(y)
    return -0.5 * N * np.log(2 * np.pi * sigma**2) - np.sum((y - mu)**2) / (2 * sigma**2)

# Plot the log-posterior for mu in the range [-4, 4]
mu_values = np.linspace(-4, 4, 100)
log_posterior_values = [log_posterior(mu, y) for mu in mu_values]

plt.plot(mu_values, log_posterior_values)
plt.xlabel('mu')
plt.ylabel('Log-posterior')
plt.title('Log-posterior for mu in the range [-4, 4]')
plt.show()
