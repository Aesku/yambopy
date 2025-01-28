save_path='.'
bse_path ='./diagos'
from yambopy import *
from qepy import *
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":

    # Customly chosen Q-point
    iQ=1 # 0-> Gamma point, i.e., optical absorption limit
    # States to be merged together (because they are degenerate)
    #
    # You may try the following states:
    # 
    # [1,2], [3,4], [5], [6,7]
    #
    states = [2]

    #                    #
    # Start Yambopy part #
    #                    #

    # Create "lattice" object by reading the ns.db1 database inside the yambo SAVE
    ylat = YamboLatticeDB.from_db_file(filename=save_path+'/SAVE/ns.db1')

    # Read exciton data at Q=iQ
    ymagn = YamboMagnonDB.from_db_file(ylat,filename=bse_path+'/ndb.BS_diago_Q1')

    # Plot of exciton weights in k-space
    fig = plt.figure(figsize=(6,6))
    ax  = fig.add_axes( [ 0.15, 0.15, 0.80, 0.80 ])
    ymagn.plot_exciton_2D_ax(ax,states,mode='hexagon',limfactor=0.8,scale= 320)
    plt.show()
