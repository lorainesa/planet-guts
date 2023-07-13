{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "1a0182a3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "import numpy  as np\n",
    "import matplotlib.pyplot as plt\n",
    "from matplotlib import rc\n",
    "import matplotlib.patches as patches\n",
    "import matplotlib.pyplot as plt\n",
    "import copy\n",
    "from scipy import integrate\n",
    "import mpmath as mp\n",
    "###########################################################33\n",
    "#Constant definitions\n",
    "zeta3 = 1.2020569031595942853997381615114499907649862923404988817922715553\n",
    "dalpha = 1.13\n",
    "C = 7.*np.pi**4/(180.*zeta3)\n",
    "# T = T0/sqrt(t), with T0 in units of MeV\n",
    "T0 = np.sqrt(132.)*0.1 \n",
    "arm = 2.9e-4\n",
    "Trm = 2.7255*8.617e-5/10**6/arm\n",
    "###############################################################\n",
    "#Decay function definitions\n",
    "decaym = lambda T: np.exp(-0.1/T)\n",
    "decayeqmr = lambda T: np.exp(-8.098494310344826*10**(-7)/T)\n",
    "###############################################################\n",
    "#Density of neutrino species calculations\n",
    "#For neutrinos g_s=2 thus for relativistic neutrinos\n",
    "def rho_relnu(T):\n",
    "    return 7*2*np.pi**2*T**4/(8*30)\n",
    "def n_relnu(T):\n",
    "    return 3*1.202*2*T**3/(4*np.pi**2)   \n",
    "#############################################3\n",
    "def sinLowRH(msvar,TR,NeffT,Tdec):\n",
    "    return NeffT*C*Tdec/msvar/10./dalpha*(5./TR)**3\n",
    "#####################################################    \n",
    "## msvar in units of MeV\n",
    "def taudark(msvar,svar,TR,NeffT):\n",
    "    return C**2*NeffT**2*T0**2/msvar**2/((10.*dalpha*(TR/5.)**3)**2)/svar**2\n",
    "#f_graciela\n",
    "#sin2=sinLowRH(msvar,TR,NeffT,Tdec)\n",
    "def f_graciela(sin2,T_RH):\n",
    "    return 11.3*sin2*(T_RH/5)**3\n",
    "#Temperature correction\n",
    "Temp_corr=4.11/3.15\n",
    "###############################\n",
    "#PART 1:Reheating calculation\n",
    "#sinLowRH(msvar,TR,NeffT,Tdec)\n",
    "#taudark=taudark(msvar,svar,TR,NeffT)\n",
    "#sin2=sinLowRH(msvar,TR,NeffT,Tdec)\n",
    "#neff:nefft7h0,nefft7stand\n",
    "#temp CMB today approx 0.2348*10**(-9)MeV\n",
    "#T=np.linspace(0.2348*10**(-9),7)\n",
    "#def C_reheat(sin2,T_RH,T_wf):\n",
    "#    return (11.3*sin2*(T_RH/5)**3*np.pi**2*2*T_wf**3/30)/((T_wf**4/4)-(T_RH**4/4))\n",
    "#C_RHT=C_reheat(sin2,7,1)\n",
    "#def rho_nus_rehet(T,C_reheat,eps):\n",
    "#    return eps*T*C_reheat*((T**4/4)-(T_RH**4/4))\n",
    "######################################################33\n",
    "#Part2:\n",
    "#Mass is equal to 0.1MeV\n",
    "T=np.linspace(0.2348*10**(-2),7)#, dtype=np.float128)\n",
    "T=np.logspace(-3,1, 1000)#, dtype=np.float128)\n",
    "m = .01\n",
    "\n",
    "#integral definition\n",
    "#rhoint = lambda x,T: ((x**2*T**2-0.1**2)**(1/2)/(np.exp(x)+1))*x**2*T**3\n",
    "\n",
    "def fermiint(x):\n",
    "    inttop = (x )**3 \n",
    "    intbot = np.exp(x)+1\n",
    "#    intbot = np.exp(x)+1\n",
    "#    print(x, intbot)\n",
    "    intfinal = (\n",
    "        inttop\n",
    "        / intbot\n",
    "    )\n",
    "\n",
    "    return intfinal\n",
    "\n",
    "def rhoint(x, T, m):\n",
    "    inttop = ((x * T)**2 - (m**2))**(1/2)\n",
    "    intbot = np.exp(x)+1\n",
    "#    intbot = np.exp(x)+1\n",
    "#    print(x, intbot)\n",
    "    rho = (\n",
    "        inttop\n",
    "        / intbot\n",
    "        * x**2\n",
    "        * T**3\n",
    "    )\n",
    "\n",
    "    return rho\n",
    "\n",
    "    \n",
    "#evaluate the integral\n",
    "#print(0.1/T)\n",
    "y = np.zeros_like(T,dtype=object)\n",
    "err = np.zeros_like(T,dtype=object)\n",
    "#for count, value in enumerate(values, start=1):\n",
    "#for i,v in enumerate(0.1/T):\n",
    "\n",
    "plt.figure()\n",
    "for i, v in enumerate(m/T):\n",
    "#    rhonu_int=integrate.quad(rhoint, v, np.inf, args=(T,))\n",
    "    rhonu_int=integrate.quad(rhoint, v, 100, args=(T[i],m))#, epsrel=1e-10)\n",
    "    y[i]=rhonu_int[0]\n",
    "    err[i]=rhonu_int[1]\n",
    "#    yy[i]=\n",
    "#    print(rhonu_int[0])\n",
    "#    plt.scatter(T[i], rhonu_int, color='blue\n",
    "    #print(v)\n",
    "\n",
    "S=rho_relnu(0.1)/max(rho_relnu(T))-n_relnu(0.1)/max(n_relnu(T))\n",
    "ST=10**S\n",
    "#plt.plot(T,y/np.pi**2)\n",
    "#plt.plot(T,y*decaym(T)/max(y),'blue')\n",
    "plt.plot(T,y/max(y),'red', label = 'numerical')\n",
    "#plt.plot(T,y/max(y)*decaym(T),'blue', label = 'decay')\n",
    "T_rad=np.linspace(0.1,10)\n",
    "T_mat=np.linspace(0.2348*10**(-3),0.1)\n",
    "plt.plot(T_rad,rho_relnu(T_rad)/max(rho_relnu(T_rad)),'green', label='analytic')\n",
    "plt.plot(T_mat,n_relnu(T_mat)/max(n_relnu(T_mat)*10**8),'green')\n",
    "#plt.plot(T_mat,n_relnu(T_mat)/max(n_relnu(T_mat)*8.3**8),'green')\n",
    "plt.xlim(max(T), min(T))\n",
    "plt.xscale(\"log\")\n",
    "plt.yscale(\"log\")\n",
    "plt.title('Energy density time evolution of sterile neutrinos', fontsize=15)\n",
    "plt.xlabel('Temperature (MeV)')\n",
    "plt.ylabel(r'Density, $\\rho_{\\nu_S}$')\n",
    "plt.legend()\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f7e2d24c",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2152c2ea",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7a640c4e",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8b020800",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "af130bc8",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6d965bf7",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a8569a18",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "64912cdd",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c0d4a8d1",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2a19a813",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b3bede47",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ff10018a",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4bffc803",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "31ca7fa1",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9c842312",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "64159608",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
