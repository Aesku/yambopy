save_path='.'
bse_path ='./diagos'
from yambopy import *
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":

    #Customly chosen Q-point
    iQ=0 # 0-> Gamma point, i.e., optical absorption limit

    #                    #
    # Start Yambopy part #
    #                    #

    # Create "lattice" object by reading the ns.db1 database inside the yambo SAVE
    ylat = YamboLatticeDB.from_db_file(filename=save_path+'/SAVE/ns.db1')

    # Read exciton data at Q=iQ
    ymag = YamboMagnonDB.from_db_file(ylat,filename=bse_path+'/ndb.BS_diago_Q1')

    # Eigenvalues (exciton energies) and intensities (residuals squared)
    print('\nEquivalent of ypp -e s -b 1: ')
    energies    = ymag.eigenvalues.real
    intensities = ymag.get_intensities().real 
    for i_exc in range(6): print(i_exc+1,' %2.4f'%energies[i_exc],' %2.4f'%intensities[i_exc])
    print('...\n ')

    # Eigenvectors (exciton wave functions)
    print('Eigenvector shape (number of excitons, number of transitions): ')
    print(ymag.eigenvectors.shape,'\n ') 

    # Table (from transition basis to single particle basis)
    print('Transition index t = (kvc) -> Single-particle indices k, v, c ')
    for it, t in enumerate(ymag.table[:10]): print(it, ' -> ', t[0],t[1],t[2])
    print('...')

    #                    #
    # Start Yambopy part #
    #                    #
