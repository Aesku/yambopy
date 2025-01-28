save_path='.'
bse_path ='./diagos'
from yambopy import *
from qepy import *
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":

    # Plot on top of the band structure
    
    ## [1.] Define path in crystal coordinates using class Path

    npoints = 20
    path = Path([ [[  0.0,  0.0,  0.0],'$\Gamma$'],
                  [[  0.0,  0.5,  0.0],'M'],
                  [[1./3.,1./3.,  0.0],'K'],
                  [[  0.0,  0.0,  0.0],'$\Gamma$']], 
                  [int(npoints*2),int(npoints),int(sqrt(5)*npoints)] )

    ## [2.] Read electron energies
    ## NB:  A YamboQPDB object containing QP corrections is also accepted
    ylat = YamboLatticeDB.from_db_file(filename=save_path+'/SAVE/ns.db1')

    # Read exciton data at Q=iQ
    ymagn = YamboMagnonDB.from_db_file(ylat,filename=bse_path+'/ndb.BS_diago_Q1')
    yel = YamboElectronsDB.from_db_file(folder=save_path+'/SAVE')
    states = [1]    
    
    fig = plt.figure(figsize=(4,6))
    ax  = fig.add_axes( [ 0.15, 0.15, 0.80, 0.80 ])

    # In case of problems with the interpolation, try to increase lpratio
    magn_on_bands = ymagn.interpolate(yel,path,states,lpratio=10,f=None,verbose=True)

    # The 'size' argument controls the weight widths
    magn_on_bands.plot_ax(ax,c_bands='k',c_weights='red',size=1.,alpha_weights=0.5)

    ax.set_ylim(-7.5,12.)
    plt.show()
    
    #                  #
    # End Yambopy part #
    #                  #
