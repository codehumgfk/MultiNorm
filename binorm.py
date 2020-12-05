import numpy as np
import matplotlib.pyplot as plt

n = 100
mux, muy = 40, 60
sigmax, sigmay = 10, 5
rho = 0.7

randomx = np.random.normal(mux, sigmax, [n])
muy2 = muy + sigmay/sigmax * rho * (randomx - mux)
sigmay2 = ((1 - rho**2) * sigmay*2)**0.5 
randomy = np.random.normal(muy2, sigmay2)

plt.figure()
plt.scatter(randomx,randomy)
plt.xticks([mux-2*sigmax, mux-sigmax, mux, mux+sigmax, mux+2*sigmax]
          ,[r'$\mu_x-2\sigma_x$', r'$\mu_x-\sigma_x$', r'$\mu_x$', r'$\mu_x+\sigma_x$', r'$\mu_x+2\sigma_x$'])
plt.xlabel('x')
plt.yticks([muy-2*sigmay, muy-sigmay, muy, muy+sigmay, muy+2*sigmay]
          ,[r'$\mu_y-2\sigma_y$', r'$\mu_y-\sigma_y$', r'$\mu_y$', r'$\mu_y+\sigma_y$', r'$\mu_y+2\sigma_y$'])
plt.ylabel('y')
plt.savefig('binorm.png')
plt.close()
