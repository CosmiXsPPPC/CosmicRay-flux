The repository provides the Galactic weak-scale dark matter (DM) induced cosmic-ray fluxes for $\bar{p}$ and $\bar{D}$ estimated under the updated models and are useful for DM indirect searches.

The DM induced $\bar{p}$ and $\bar{D}$ spectra at production are taken from *CosmiXs* for the same DM mass binns (in the range 5 GeV--100 TeV (10 GeV--200 TeV) for DM annihilation (decay)) provided in *CosmiXs* and *PPPC4DMID* and for 19 annihilation/decay channels: 

$e^+ e^-$, , $\mu^+ \mu^-$, $\tau^+ \tau^-$, $\nu_{l} \bar{\nu}_{l}$, $u \bar{u}$, $d \bar{d}$, $s \bar{s}$, $c \bar{c}$, $b \bar{b}$, ${t \bar{t}}$, $\gamma \gamma$, $g g$, $W^+ W^-$, $Z Z$, $H H$, $Z \gamma$, $H Z$.

Each of the spectra is then propagated through the Galaxy using the ```MIN```, ```MED``` and `MAX` sets under the {\it new} propagation schemes: \texttt{SLIM}, \texttt{BIG} and \texttt{QUAINT} to obtain the cosmic-ray flux ($d\phi/dK$) at the Solar position.
The fluxes are computed using a semi-analytic approach considering different effects including energy-losses and reacceleration.

For the DM distribution in the Galaxy we consider the NFW, Einasto and Burkert profiles which are normalized in order to have a DM density $\rho_\odot = 0.4~\rm GeV\,cm^{-3}$.

The inelastic interaction of the propagated $\bar{p}$ and $\bar{D}$ with the ISM gas is described by an analytic Glauber-eikonal framework,
which gives an estimate consistent with the {\sc Alice} measurement.

The final cosmic-ray (CR) fluxes are provided in a tabulated format (described below), which can be used independently or can be loaded using the python script (described below).


******************************************************
Format of the tables
******************************************************

We sample the final CR flux (for all cases) in the kinetic-energy ($K$) range $0.1 {\rm GeV} \le K \le 10^5 {\rm GeV}$, with 20 bins per decade in energy.
All these fluxes are provided in the tabulated format in four '.zip' files for $\bar{p}$ and $\bar{D}$ produced by DM annihilation and decay.

Inside each '.zip' file the user can find a set of '.dat' files, each one containing the columns:  mDM/GeV, Log10(K/GeV) and the corresponding flux $d\phi/dK$ for 19 primary channels. All the fluxes are in the unit of $\rm{GeV^{-1}m^{-2}s^{-1}sr^{-1}}$. Each '.dat' file corresponds to a particular propagation model (e.g., BIG-MED) and a DM profile.
The benchmark annihilation cross-section (decay rate) is $\langle \sigma v \rangle = 3\times10^{-26}$ $\rm{cm^3s^{-1}}$ ($\Gamma = 10^{-28}$ $\rm{s^{-1}}$).


******************************************************
About the python script
******************************************************

The python script can be run using a command in the terminal: "python3 CR_flux.py"

The script takes the user's inputs for the DM and propagation related models and returns

(a) the CR fluxes at the user specified kinetic energies ($K$'s) and

(b) the corresponding plots for the fluxes.

It reads the tabulated CR fluxes that we provide separately for the independent users in four '.zip' files.

In the "Inputs" section of the script, user can choose:

* the CR species, i.e., $\bar{p}$ or $\bar{D}$,

* DM interaction type, i.e., Annihilation or Decay, and the corresponding value of $\langle \sigma v \rangle$ or $\Gamma$. \
  The default value is $\langle \sigma v \rangle = 3\times10^{-26}$ $\rm{cm^3s^{-1}}$ and $\Gamma = 10^{-28}$ $\rm{s^{-1}}$.

* values of DM mass

* Annihilation/Decay channels

* propagation schemes: QUAINT, BIG or SLIM

* DM profiles: NFW, Einasto or Burkert

* values of $K$ to print the CR fluxes (in the range 0.1 GeV - $10^5$ GeV)

* a value for the Fisk potential ($\Phi_F$)

* the name of the folder to save the outcome flux plots.

The present version of the script will plot inside the figure folder the CR IS fluxes (ToA fluxes if $\Phi_F \not= 0$) for the user provided inputs.
The plots will be similar to those presented in Figs. 2 - 8 of our paper. N.B., for $\bar{D}$, the fluxes are plotted as a function of $K/n$.
In each case, the shaded band will represent the MIN - MAX variation.

The script will also print the corresponding values of the IS fluxes (ToA fluxes if $\Phi_F \not= 0$) under MIN, MED and MAX setups respectively, for the user provided $K$'s.
The printed fluxes are in units of $\rm{GeV^{-1}m^{-2}s^{-1}sr^{-1}}$. 
