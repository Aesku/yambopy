save_path='.'
bse_path ='./diagos'
from yambopy import *
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":

    # Customly chosen Q-point
    iQ=1 # 1-> Gamma point, i.e., optical absorption limit

    #                    #
    # Start Yambopy part #
    #                    #

    # Create "lattice" object by reading the ns.db1 database inside the yambo SAVE
    ylat = YamboLatticeDB.from_db_file(filename=save_path+'/SAVE/ns.db1')

    # Read exciton data at Q=iQ
    ymagn = YamboMagnonDB.from_db_file(ylat,filename=bse_path+'/ndb.BS_diago_Q%d'%iQ)

    #
    # Spectrum of the dielectric function (optical absorption at q=0)
    #
    # In order to customise your plot, try to test with different values of: 
    #
    #  * emin, emax, estep
    #  * broad
    #  * nexcitons
    #  * iQ
    #
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.set_xlim(0,7)

    w, chi = ymagn.plot_chi_ax(ax,nexcitons='all',emin=0,emax=7,estep=0.005,broad=0.04)
    ax.set_ylim(0,np.max(chi.imag)*1.1)
    plt.show()

    # In order to get the eps(w) data we use the function get_chi
    w, eps = ymagn.get_chi(emin=0,nexcitons='all',emax=7,estep=0.005,broad=0.04)
    print('Epsilon array: ',eps.shape, eps.dtype)

    #                  #
    # End Yambopy part #
    #                  #
