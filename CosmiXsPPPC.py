import numpy as np
import scipy as sp
import os
from scipy.ndimage import gaussian_filter1d
import matplotlib.pyplot as plt
from matplotlib.ticker import LogLocator, MultipleLocator
import matplotlib.ticker as ticker
from pylab import rcParams

mp = 0.938 #GeV
mD = 1875.613*1e-3 #GeV

###############################################################################################
################# Inputs ########################
###############################################################################################
species = 'pbar'         #'pbar' #'dbar' 

DM_interaction = 'Annihilation'   #'Annihilation' #'Decay'

sv0 = 3.e-26      ###in unit cm^3.s^-1
Gamma0 = 1.e-28   ###in unit s^-1

mdm0_arr = np.array([1e2, 1e3, 1e4, 1e5])    #np.array([1e2, 1e3, 1e4, 1e5])    ###in unit GeV

channel_list = ['bb']  #['ee', 'mumu', 'tautau', 'nu_e_nu_e', 'nu_mu_nu_mu', 'nu_tau_nu_tau', 'uu', 'dd', 'ss', 'cc', 'bb', 'tt', 'AA', 'gg', 'WW', 'ZZ', 'hh', 'AZ', 'hZ']

prop_scheme_list = ['QUAINT']        #['QUAINT', 'BIG', 'SLIM']

DM_profile_list = ['NFW']          #['NFW', 'Einasto', 'Burkert']

PhiF_GV = 0.0  ###in unit GV

K_print = np.array([1.e-1, 1., 1.e+1, 1.e+2, 1.e+3, 1.e+4, 1.e+5])  ###(in range 0.1 GeV -- 10^5 GeV)

Fig_folder = 'Figs'
###############################################################################################
################# Inputs ########################
###############################################################################################



##=================================================================
## average solar modulation
##=================================================================
def SolarModul(K_GeV_arr, dPhipdK_arr, species0): 
    if species0 == 'pbar':
       msp0 = mp
    if species0 == 'dbar':
       msp0 = mD
    K_Earth = K_GeV_arr - (1.0)*PhiF_GV  #GeV
    K_Earth = np.where(K_Earth<0., 0., K_Earth)
    p_arr = np.sqrt(2.*msp0*K_GeV_arr + K_GeV_arr**2)
    p_Earth = np.sqrt(2.*msp0*K_Earth + K_Earth**2)
    dPhipdK_arr_Earth = dPhipdK_arr * (p_Earth/p_arr)**2
    dPhipdK_arr_Earth = np.where(K_Earth<0., 0., dPhipdK_arr_Earth)
    #print(K_Earth)
    return K_Earth, dPhipdK_arr_Earth
##=================================================================


if species == 'pbar':
   msp, n_val, sigma_Gauss = mp, 1., 0.1
if species == 'dbar':
   msp, n_val, sigma_Gauss = mD, 2., 1


#########################################################################################################################
def get_main_readplot(speciesFlux_folder, prop_scheme, prop_set, DM_profile, mdm0, channel): 
    
    ##=============================================================    
    speciesFlux_filename = str(speciesFlux_folder) + "/" + str(species) + "_flux_" + str(prop_scheme) + "_" + str(prop_set) + "_" + str(DM_profile) + ".dat" 

    if channel == 'ee':
       N_ch = 0
    if channel == 'mumu':
       N_ch = 1
    if channel == 'tautau':
       N_ch = 2
    if channel == 'nu_e_nu_e':
       N_ch = 3
    if channel == 'nu_mu_nu_mu':
       N_ch = 4
    if channel == 'nu_tau_nu_tau':
       N_ch = 5
    if channel == 'uu':
       N_ch = 6
    if channel == 'dd':
       N_ch = 7
    if channel == 'ss':
       N_ch = 8
    if channel == 'cc':
       N_ch = 9
    if channel == 'bb':
       N_ch = 10
    if channel == 'tt':
       N_ch = 11
    if channel == 'AA':
       N_ch = 12
    if channel == 'gg':
       N_ch = 13
    if channel == 'WW':
       N_ch = 14
    if channel == 'ZZ':
       N_ch = 15
    if channel == 'hh':
       N_ch = 16
    if channel == 'AZ':
       N_ch = 17
    if channel == 'hZ':
       N_ch = 18

    mdm, log10K, species_ch = np.loadtxt(speciesFlux_filename, usecols=(0, 1, N_ch+2), skiprows=1, unpack=True)  #GeV, log10(GeV), GeV^-1.m^-2.s^-1.sr^-1

    m_ann_arr = np.array([5.000e+00, 1.000e+01, 1.500e+01, 2.000e+01, 2.500e+01, 3.000e+01, 4.000e+01, 5.000e+01, 6.000e+01, 7.000e+01, 7.500e+01, 8.000e+01, 8.500e+01, 9.000e+01, 9.500e+01, 1.000e+02, 1.100e+02, 1.200e+02, 1.300e+02, 1.400e+02, 1.500e+02, 1.600e+02, 1.625e+02, 1.800e+02, 2.000e+02, 2.200e+02, 2.400e+02, 2.600e+02, 2.800e+02, 3.000e+02, 3.300e+02, 3.600e+02, 4.000e+02, 4.500e+02, 5.000e+02, 5.500e+02, 6.000e+02, 6.500e+02, 7.000e+02, 7.500e+02, 8.000e+02, 9.000e+02, 1.000e+03, 1.100e+03, 1.200e+03, 1.300e+03, 1.500e+03, 1.700e+03, 2.000e+03, 2.500e+03, 3.000e+03, 4.000e+03, 5.000e+03, 6.000e+03, 7.000e+03, 8.000e+03, 9.000e+03, 1.000e+04, 1.200e+04, 1.500e+04, 2.000e+04, 3.000e+04, 5.000e+04, 1.000e+05])

    m_length = len(m_ann_arr) 
    K_length = int(len(mdm)/m_length)

    log10K_arr = log10K[0:K_length]
    K_arr_out_IS = 10.**log10K_arr   #GeV

    species_ch_tab = np.zeros((m_length, K_length))

    for m in range(0, m_length):
        species_ch_tab[m,:] = species_ch[m*K_length:(m+1)*K_length]
    ##=============================================================

    ##============ IS flux =================================================
    species_ch_interp = np.zeros(K_length)

    for k in range(0, K_length): 
        if DM_interaction == 'Annihilation': 
           species_ch_interp[k] = (sv0/3.e-26) * np.interp(mdm0, m_ann_arr, species_ch_tab[:,k])        #GeV^-1.m^-2.s^-1.sr^-1 
        if DM_interaction == 'Decay': 
           species_ch_interp[k] = (Gamma0/1.e-28) * np.interp(mdm0, 2.*m_ann_arr, species_ch_tab[:,k])  #GeV^-1.m^-2.s^-1.sr^-1
    ##============ IS flux =================================================
    
    ##============ TOA flux =================================================
    Kout_TOA_full, species_ch_TOA = SolarModul(K_arr_out_IS, species_ch_interp, species)            #GeV vs. GeV^-1.m^-2.s^-1.sr^-1
    Kout_TOA = Kout_TOA_full[(Kout_TOA_full>0.)]
    species_ch_TOA = species_ch_TOA[(Kout_TOA_full>0.)]
    ##============ TOA flux =================================================
    
    
    return K_arr_out_IS, species_ch_interp, Kout_TOA, species_ch_TOA      ## GeV vs. GeV^-1.m^-2.s^-1.sr^-1
#########################################################################################################################



if os.path.isdir(str(Fig_folder)) == False:
   os.system('mkdir ' + str(Fig_folder))


#########################################################################################################################
##----------------------------------------------------------------------
speciesFlux_folder0 = str(species) + "_flux_" + str(DM_interaction) + "_tab"
    
if os.path.isdir(str(speciesFlux_folder0)) == False:
   os.system('unzip -q ' + str(speciesFlux_folder0) + '.zip')
##----------------------------------------------------------------------
    

for i in range(0, len(prop_scheme_list)): 
    prop_scheme0 = prop_scheme_list[i]
    
    for j in range(0, len(DM_profile_list)):
        DM_profile0 = DM_profile_list[j] 
        
        for mi in range(0, len(mdm0_arr)):
            mdm_val = mdm0_arr[mi]
            
            for ci in range(0, len(channel_list)):
                channel0 = channel_list[ci] 
                
                #----------------------------------------------------------------------------
                ## GeV vs. GeV^-1.m^-2.s^-1.sr^-1
                #----------------------------------------------------------------------------
                K_out, species_ch_out_MIN, K_out_TOA, species_ch_out_MIN_TOA = get_main_readplot(speciesFlux_folder0, prop_scheme0, 'MIN', DM_profile0, mdm_val, channel0)
                K_out, species_ch_out_MED, K_out_TOA, species_ch_out_MED_TOA = get_main_readplot(speciesFlux_folder0, prop_scheme0, 'MED', DM_profile0, mdm_val, channel0)
                K_out, species_ch_out_MAX, K_out_TOA, species_ch_out_MAX_TOA = get_main_readplot(speciesFlux_folder0, prop_scheme0, 'MAX', DM_profile0, mdm_val, channel0)
                #---------------------------------------------------------------------------- 
                
                
                ##**************************************
                ## Print CR Flux (TOA flux if PhiF_GV =/= 0)
                ##**************************************
                print("====== ", species, ", ", prop_scheme0, ",", DM_profile0, ",", "mDM/GeV =", "%1.2e" % (mdm_val), ",", channel0, ",", DM_interaction, " =================")
                for ki in range(0, len(K_print)): 
                    print("%1.3e" % (K_print[ki]), "%1.3e" % (np.interp(K_print[ki], K_out_TOA, species_ch_out_MIN_TOA)), "%1.3e" % (np.interp(K_print[ki], K_out_TOA, species_ch_out_MED_TOA)), "%1.3e" % (np.interp(K_print[ki], K_out_TOA, species_ch_out_MAX_TOA)))
                print("===================================================================================")

                
                
                ##**************************************
                ## Plot CR Flux (TOA flux if PhiF_GV =/= 0)
                ##**************************************
                ##=======================================================================
                rcParams['figure.figsize'] = 8., 6.
                fig, ax1 = plt.subplots()
                fig.subplots_adjust(left=0.185, bottom=0.145, right=0.94, top=0.9, wspace=0.3, hspace=None)

                ax1.set_xscale('log')
                ax1.set_yscale('log')
                
                xmin, xmax = 0.1, 1.e5
                
                if species == 'pbar':
                   ax1.set_xlabel('$K_{\\bar{p}}$ $(\\rm GeV)$', fontsize=19, labelpad=10)
                   ax1.set_ylabel('$K^2_{\\bar{p}} \\, \\, \\frac{d\\Phi_{\\bar{p}}}{dK_{\\bar{p}}} (\\vec{{r}}_\\odot)$ $(\\rm GeV.m^{-2}.s^{-1}.sr^{-1})$', fontsize=21)
                   ymin, ymax = 3.e-8, 10.
                if species == 'dbar':
                   ax1.set_xlabel('$K_{\\bar{D}}/n$ $(\\rm GeV)$', fontsize=19, labelpad=10)
                   ax1.set_ylabel('$K^2_{\\bar{D}} \\, \\, \\frac{d\\Phi_{\\bar{D}}}{dK_{\\bar{D}}} (\\vec{{r}}_\\odot)$ $(\\rm GeV.m^{-2}.s^{-1}.sr^{-1})$', fontsize=21)
                   ymin, ymax = 3.e-11, 1.e-3
                
                ax1.set_xlim(xmin, xmax)
                ax1.set_ylim(ymin, ymax) 
                
                ax2 = ax1.twinx()
                ax2.set_xscale('log')
                ax2.set_yscale('log')
                ax2.set_xlim(xmin, xmax)
                ax2.set_ylim(ymin, ymax)
                ax2.set_ylabel('Created by CosmiXsPPPC', fontsize=10)
                
                ##----------------------------------------------------------------------------------------
                ax1.plot(K_out_TOA[0:np.argmin(species_ch_out_MAX_TOA)]/n_val, (gaussian_filter1d(K_out_TOA**2*species_ch_out_MAX_TOA, sigma_Gauss))[0:np.argmin(species_ch_out_MAX_TOA)], lw=2.6, dashes=[4,2], color='b', alpha=1, label="MAX") 
                
                ax1.plot(K_out_TOA[0:np.argmin(species_ch_out_MED_TOA)]/n_val, (gaussian_filter1d(K_out_TOA**2*species_ch_out_MED_TOA, sigma_Gauss))[0:np.argmin(species_ch_out_MED_TOA)], lw=2.6, ls='-', color='b', alpha=1, label="MED") 
                
                ax1.plot(K_out_TOA[0:np.argmin(species_ch_out_MIN_TOA)]/n_val, (gaussian_filter1d(K_out_TOA**2*species_ch_out_MIN_TOA, sigma_Gauss))[0:np.argmin(species_ch_out_MIN_TOA)], lw=2.8, dashes=[1,2], color='b', alpha=1, label="MIN") 
                
                plt.fill_between(K_out_TOA[0:np.argmin(species_ch_out_MAX_TOA)]/n_val, (gaussian_filter1d(K_out_TOA**2*species_ch_out_MIN_TOA, sigma_Gauss))[0:np.argmin(species_ch_out_MAX_TOA)], (gaussian_filter1d(K_out_TOA**2*species_ch_out_MAX_TOA, sigma_Gauss))[0:np.argmin(species_ch_out_MAX_TOA)], facecolor='b', edgecolor='None', alpha=0.4)
                ##----------------------------------------------------------------------------------------
                
                ax1.tick_params('x', direction="in", top=True, length=6, width=2.5, which='major', labelsize=19)
                ax1.tick_params('y', direction="in",  right=True, length=6, width=2.5, which='major', labelsize=21)
                ax1.tick_params('both', direction="in", top=True, right=True, length=4, width=1.5, which='minor', labelsize=0) 
                
                ax2.tick_params('both', direction="in", top=True, length=6, width=2.5, which='major', labelcolor='w', labelsize=0)
                ax2.tick_params('both', direction="in", top=True, right=True, length=4, width=1.5, which='minor', labelcolor='w', labelsize=0) 

                ax1.yaxis.set_major_locator(ticker.LogLocator(base=10, numticks=30))
                #locmin = ticker.LogLocator(base=10.0,subs=(0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9),numticks=30)
                locmin = ticker.LogLocator(base=10.0,subs=(0.2,0.4,0.6,0.8),numticks=15)
                ax1.yaxis.set_minor_locator(locmin)
                ax1.yaxis.set_minor_formatter(ticker.NullFormatter())
                
                ax2.yaxis.set_major_locator(ticker.LogLocator(base=10, numticks=30))
                #locmin = ticker.LogLocator(base=10.0,subs=(0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9),numticks=30)
                locmin = ticker.LogLocator(base=10.0,subs=(0.2,0.4,0.6,0.8),numticks=15)
                ax2.yaxis.set_minor_locator(locmin)
                ax2.yaxis.set_minor_formatter(ticker.NullFormatter())
                
                if mdm_val<1000.:
                      plt.title(str(prop_scheme0) + ", " + str(DM_profile0) + ", " + str(channel0) + ", $m_{\\rm DM} = $" + str("%0.1f" % (mdm_val)) + " GeV", color='k', size="19", pad=10, rotation=0)
                if mdm_val>=1000.:
                      plt.title(str(prop_scheme0) + ", " + str(DM_profile0) + ", " + str(channel0) + ", $m_{\\rm DM} = $" + str("%0.1f" % (mdm_val*1e-3)) + " TeV", color='k', size="19", pad=10, rotation=0)
                
                if species == 'pbar':
                   if DM_interaction == 'Annihilation': 
                      plt.text(0.13e3, 3e-2, "$\\langle \\sigma v \\rangle$ = " + str("%1.e" % (sv0)) + " $\\rm cm^3 s^{-1}$", color='k', size="17", rotation=0)
                   if DM_interaction == 'Decay': 
                      plt.text(0.13e4, 3e-2, "$\\Gamma$ = " + str("%1.e" % (Gamma0)) + " $\\rm s^{-1}$", color='k', size="17", rotation=0)
                
                if species == 'dbar':
                   if DM_interaction == 'Annihilation': 
                      plt.text(0.13e3, 5e-6, "$\\langle \\sigma v \\rangle$ = " + str("%1.e" % (sv0)) + " $\\rm cm^3 s^{-1}$", color='k', size="17", rotation=0)
                   if DM_interaction == 'Decay': 
                      plt.text(0.13e4, 5e-6, "$\\Gamma$ = " + str("%1.e" % (Gamma0)) + " $\\rm s^{-1}$", color='k', size="17", rotation=0)
                
                ax1.legend(loc=2, ncol=1, fontsize=16, frameon=True)
                
                fig.savefig(str(Fig_folder) + "/" + str(species) + "_" + str(prop_scheme0) + "_" + str(DM_profile0) + "_" + str("%1.3e" % (mdm_val)) + "_" + str(channel0) + "_" + str(DM_interaction) + ".pdf", format='pdf', dpi=80)
                ##=======================================================================


##----------------------------------------------------------------------
os.system('rm -r ' + str(speciesFlux_folder0))
##----------------------------------------------------------------------
#########################################################################################################################

















