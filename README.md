******************************************************
Run the python script using:  "python3 CR_flux.py" 
******************************************************

The script takes the user's inputs for the DM and propagation related models 
and returns the CR fluxes at the user specified kinetic energies (K.E.) and the corresponding plots for the fluxes. 
It reads the tabulated CR fluxes that we provide separately for the independent users in '.zip' files (four .zip files for pbar/Dbar produced by DM annihilation/decay)    

In the "Inputs" section of the script, user can choose: 

(.) the CR species, i.e., pbar or Dbar, 
(.) DM interaction type, i.e., Annihilation or Decay, and the corresponding value of <sigmaV> or $\Gamma$. The default value is <sigmaV> = 3e-26 cm^3.s^-1 and Gamma = 1e-28 s^-1. 
(.) values of DM mass (as an array)
(.) Annihilation/Decay channels (as a list) 
(.) propagation schemes: QUAINT, BIG or SLIM (as a list) 
(.) DM profiles: NFW, Einasto or Burkert (as a list)
(.) values of K.E. to print the CR fluxes (as an array) 
(.) a value for the Fisk potential 
(.) the name of the folder to save the outcome flux plots. 

The present version of the script will plot inside the figure folder the CR IS fluxes (ToA fluxes if Fisk =/= 0) for the user provided inputs. 
The plots will be similar to those presented in Figs. 2 -- 8 of our paper. In each case, the shaded band will represent the MIN--MAX variation. 

The script will also print the corresponding values of the IS fluxes (ToA fluxes if Fisk =/= 0) under MIN, MED and MAX setups respectively, for the user provided K.E.'s. 
The printed fluxes are in units of GeV^-1.m^-2.s^-1.sr^-1. 
