******************************************************
Run the python script using:  "python3 CR_flux.py" 
******************************************************

The script takes the user's inputs for the DM and propagation related models and returns 

(a) the cosmic-ray (CR) fluxes at the user specified kinetic energies (K.E.'s) and 

(b) the corresponding plots for the fluxes. 

It reads the tabulated CR fluxes that we provide separately for the independent users in '.zip' files (four .zip files for $\bar{p}$ and $\bar{D}$ produced by DM annihilation and decay). 

In the "Inputs" section of the script, user can choose: 

(1) the CR species, i.e., $\bar{p}$ or $\bar{D}$, 

(2) DM interaction type, i.e., Annihilation or Decay, and the corresponding value of $\langle \sigma v \rangle$ or $\Gamma$. 
The default value is $\langle \sigma v \rangle = 3\times10^{-26}$ $\rm{cm^3s^{-1}}$ and $\Gamma = 10^{-28}$ $\rm{s^{-1}}$. 

(3) values of DM mass 

(4) Annihilation/Decay channels 

(5) propagation schemes: QUAINT, BIG or SLIM 

(6) DM profiles: NFW, Einasto or Burkert 

(7) values of K.E. to print the CR fluxes (in the range 0.1 GeV - $10^5$ GeV)

(8) a value for the Fisk potential ($\Phi_F$)

(9) the name of the folder to save the outcome flux plots. 

The present version of the script will plot inside the figure folder the CR IS fluxes (ToA fluxes if $\Phi_F \not= 0$) for the user provided inputs. 
The plots will be similar to those presented in Figs. 2 - 8 of our paper. In each case, the shaded band will represent the MIN - MAX variation. 

The script will also print the corresponding values of the IS fluxes (ToA fluxes if $\Phi_F \not= 0$) under MIN, MED and MAX setups respectively, for the user provided K.E.'s. 
The printed fluxes are in units of $\rm{GeV^{-1}m^{-2}s^{-1}sr^{-1}}$. 
