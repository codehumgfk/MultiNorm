import numpy as np
import matplotlib.pyplot as plt

n = 300
dim = 3
mux, muy, muz = 40, 60, 80
mu = np.array([[mux]
               ,[muy]
               ,[muz]])
sigmax, sigmay, sigmaz = 10, 5, 15
sigmaxy, sigmayz, sigmazx = 0.3 * sigmax * sigmay, 0.5 * sigmay * sigmaz, 0.7 * sigmaz * sigmax
Cov = np.array([[sigmax**2, sigmaxy, sigmazx]
               ,[sigmaxy, sigmay**2, sigmayz]
               ,[sigmazx, sigmayz, sigmaz**2]])
upTriang = np.linalg.cholesky(Cov)
randomz = np.random.randn(dim, n)
randomx, randomy, randomz = mu + np.dot(upTriang, randomz)


fig = plt.figure(figsize=(10,30), tight_layout=True)
ax1, ax2, ax3 = fig.add_subplot(311),fig.add_subplot(312), fig.add_subplot(313)
ax1.scatter(randomx,randomy)
ax1.set_xticks([mux-2*sigmax, mux-sigmax, mux, mux+sigmax, mux+2*sigmax])
ax1.set_xticklabels([r'$\mu_x-2\sigma_x$', r'$\mu_x-\sigma_x$', r'$\mu_x$', r'$\mu_x+\sigma_x$', r'$\mu_x+2\sigma_x$'])
ax1.set_xlabel('x')
ax1.set_yticks([muy-2*sigmay, muy-sigmay, muy, muy+sigmay, muy+2*sigmay])
ax1.set_yticklabels([r'$\mu_y-2\sigma_y$', r'$\mu_y-\sigma_y$', r'$\mu_y$', r'$\mu_y+\sigma_y$', r'$\mu_y+2\sigma_y$'])
ax1.set_ylabel('y')
ax1.grid()
ax2.scatter(randomy,randomz)
ax2.set_xticks([muy-2*sigmay, muy-sigmay, muy, muy+sigmay, muy+2*sigmay])
ax2.set_xticklabels([r'$\mu_y-2\sigma_y$', r'$\mu_y-\sigma_y$', r'$\mu_y$', r'$\mu_y+\sigma_y$', r'$\mu_y+2\sigma_y$'])
ax2.set_xlabel('y')
ax2.set_yticks([muz-2*sigmaz, muz-sigmaz, muz, muz+sigmaz, muz+2*sigmaz])
ax2.set_yticklabels([r'$\mu_z-2\sigma_z$', r'$\mu_z-\sigma_z$', r'$\mu_z$', r'$\mu_z+\sigma_z$', r'$\mu_z+2\sigma_z$'])
ax2.set_ylabel('z')
ax2.grid()
ax3.scatter(randomz,randomx)
ax3.set_xticks([muz-2*sigmaz, muz-sigmaz, muz, muz+sigmaz, muz+2*sigmaz])
ax3.set_xticklabels([r'$\mu_z-2\sigma_z$', r'$\mu_z-\sigma_z$', r'$\mu_z$', r'$\mu_z+\sigma_z$', r'$\mu_z+2\sigma_z$'])
ax3.set_xlabel('z')
ax3.set_yticks([mux-2*sigmax, mux-sigmax, mux, mux+sigmax, mux+2*sigmax])
ax3.set_yticklabels([r'$\mu_x-2\sigma_x$', r'$\mu_x-\sigma_x$', r'$\mu_x$', r'$\mu_x+\sigma_x$', r'$\mu_x+2\sigma_x$'])
ax3.set_ylabel('x')
ax3.grid()
fig.savefig('multinorm.png')
plt.close()
