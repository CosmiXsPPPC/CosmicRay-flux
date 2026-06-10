# Main purpose 

The repository provides the weak-scale dark matter (DM)-induced cosmic-ray (CR) fluxes of $\bar{p}$ and $\bar{d}$ calculated in arxiv:2606.10017, to be used for DM indirect searches in the era of high precision CR measurements. 
The main purpose is to allow the users to study the DM phenomenology based on cosmic-rays in an *efficient*, *fast* and *effortless* way without going into the involved calculations for the fluxes. 
The computation of the CR fluxes connects the updated primary spectra from **CosmiXs** and their Galactic propagation under the **_new propagation models_** which are now much more constraining, thanks to precision CR measurements. 


# Description

The DM induced primary spectra for $\bar{p}$ and $\bar{d}$ are taken from **CosmiXs** for the same DM mass bins (5 GeV - 100 TeV (10 GeV - 200 TeV) for DM annihilation (decay)) provided there and for 19 annihilation/decay channels:  $e^+ e^-$, $\mu^+ \mu^-$, $\tau^+ \tau^-$, $\nu_{\ell} \bar{\nu}_{\ell}$ (for $\ell =e, \mu, \tau$), $u \bar{u}$, $d \bar{d}$, $s \bar{s}$, $c \bar{c}$, $b \bar{b}$, ${t \bar{t}}$, $\gamma \gamma$, $g g$, $W^+ W^-$, $Z Z$, $H H$, $Z \gamma$, $H Z$.

Each of the spectra is then propagated through the Galaxy using the **MIN**, **MED** and **MAX** sets under the **_new_** propagation schemes: 
**SLIM**, **BIG** and **QUAINT** to obtain the CR flux ($d\phi/dK$) at the Solar position. 
The fluxes are computed using a semi-analytic approach and considering different effects including energy-losses and re-acceleration.

For the DM distribution in the Galaxy, we consider the *NFW*, *Einasto* and *Burkert* profiles which are normalized in order to have a DM density $\rho_{\odot} = 0.4~\rm GeV\ cm^{-3}$. 

The final CR fluxes are provided in a tabulated format (described below), which can be used independently or can be loaded using the python script (described below). 


## Format of the tables

We sample the final CR flux (for all cases) in the kinetic-energy ($K$) range $0.1 {\rm GeV} \le K \le 10^5 {\rm GeV}$, with 20 bins per decade in energy.
All these fluxes are provided in the tabulated format in four `zip` files for $\bar{p}$ and $\bar{d}$ produced by DM annihilation and decay. 

Inside each `zip` file the user can find a set of `dat` files, each one containing the columns: 
{ mDM/GeV, Log10(K/GeV) and the corresponding interstellar (IS) flux $d\phi/dK$ for the 19 primary channels }. 
The fluxes are in  units of $\rm{GeV^{-1}m^{-2}s^{-1}sr^{-1}}$ and normalized at a benchmark annihilation cross-section (decay rate) of $\langle \sigma v \rangle = 3\times10^{-26}$ $\rm{cm^3s^{-1}}$ 
($\Gamma = 10^{-28}$ $\rm{s^{-1}}$). Each `dat` file corresponds to a particular propagation model (e.g., BIG-MED) and a given DM profile. 
In each case, the flux in a given channel can be interpolated for the desired DM masses and energies. 


## About the python script

The provided python script can be run (keeping it in the same directory containing the four `zip` files) using a command in the terminal:  
`python3 CosmiXsPPPC.py`.

The script takes the user's inputs for the DM and propagation models and returns:

(a) the CR fluxes at the user specified kinetic energies ($K$'s) and

(b) the corresponding plots for the fluxes.

It reads the tabulated CR fluxes that we provide separately for the independent users in four `zip` files.

In the "Inputs" section of the script, user can choose:

* The CR species, i.e., $\bar{p}$ or $\bar{d}$.

* The DM interaction type, i.e., Annihilation or Decay, and the corresponding value of $\langle \sigma v \rangle$ or $\Gamma$. \
  The default value is $\langle \sigma v \rangle = 3\times10^{-26}$ $\rm{cm^3s^{-1}}$ and $\Gamma = 10^{-28}$ $\rm{s^{-1}}$.

* The value of DM mass in GeV.

* The Annihilation/Decay channel.

* The propagation scheme: **QUAINT**, **BIG** or **SLIM**.

* The galactic DM profile: *NFW*, *Einasto* or *Burkert*.

* The values of $K$ in GeV to print the CR fluxes (in the range 0.1 GeV - $10^5$ GeV).

* The value for the Fisk potential ($\Phi_F$) in GV.

* The name of the folder to save the outcome flux plots.

The present version of the script will plot, inside the figure folder, the CR Top-of-Atmosphere (ToA) for the user provided inputs.
The plots will be similar to those presented in Figs. 2 - 8 of our paper. In each case, the shaded band will represent the MIN - MAX variation. 
(NB: For $\bar{d}$, the fluxes are plotted as a function of $K/n$.)


The script will also print the corresponding values of the ToA fluxes under MIN, MED and MAX setups respectively, for the user provided $K$'s.
The printed fluxes are in units of $\rm{GeV^{-1}m^{-2}s^{-1}sr^{-1}}$. 


# Citations

If you use this repository please cite: M. Cirelli, M. Di Mauro, A. Kar, {arXiv:2606.10017} 


# Contact 

If you have any questions, comments or suggestions, please contact: 

* Marco Cirelli (marco.cirelli@gmail.com)
* Mattia Di Mauro (dimauro.mattia@gmail.com)
* Arpan Kar (arpankarphys@gmail.com)
  
