import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

k = 1.380649e-23
q = 1.602176634e-19
Veb = 0.6

N = 100000

R1 = 2.2 * 10**3
R2 = 19 * 10**3

sigmaR1 = 5/100 * R1
dR1 = np.random.normal(R1, 2 * sigmaR1, N)

sigmaR2 = 5/100 * R2
dR2 = np.random.normal(R2, 2 * sigmaR2, N)


T = 300
sigmaT = 10
dT = np.random.normal(T, sigmaT, N)

A = 8
sigmaA = 0.5
dA = np.random.normal(A, sigmaA, N)
dA = np.clip(dA, 14.5, None)
beta = (-2) * 10**(-3) * 1/274.15
sigmaBeta = 25/100 * beta
dBeta = np.random.normal(beta, abs(sigmaBeta), N)

Vref = dR2/dR1 * ((k * dT)/q * np.log(dA)) +  (Veb + dBeta*dT)

medie = np.mean(Vref)
deviatie = np.std(Vref)

print(Vref)
print(np.mean(Vref))
print(np.std(Vref))

plt.hist(Vref, bins=100, density=True, alpha=0.7, color='blue', label='Distributie Vref')
plt.axvline(medie, color='red', linestyle='dashed', linewidth=2, label=f'Medie = {medie:.3f} V')
plt.axvline(medie + deviatie, color='green', linestyle='dashed', linewidth=1, label=f'+σ = {medie+deviatie:.3f} V')
plt.axvline(medie - deviatie, color='green', linestyle='dashed', linewidth=1, label=f'-σ = {medie-deviatie:.3f} V')
plt.title('Distributia Vref - Monte Carlo')
plt.xlabel('Vref [V]')
plt.ylabel('Densitate')
plt.grid(True)
plt.legend()
plt.show()

plt.figure()
plt.plot(Vref, '.', markersize=1, alpha=0.3)
plt.title('Vref pentru fiecare esantion')
plt.xlabel('Index esantion')
plt.ylabel('Vref [V]')
plt.grid(True)
plt.show()
