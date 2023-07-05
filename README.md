# Tautomatic
Facile exploration and assessment of chemical tautomer space. 

In the world of chemical structure data management, the concept of tautomerism is one that represents a significant challenge to automation and to unambiguous data management. If you are not familiar with the concept then Wikipedia offers a helpful starting point:
https://en.wikipedia.org/wiki/Tautomer

In essence chemical compounds contain mobile protons, which can ‘hop’ from between different heavy atom positions, changing the chemical structure ‘drawing’ and also the bond orders. The question of which tautomer is ‘correct’ can often only be answered by experimentation, using methods such as NMR spectroscopy. However computational methods can often be well correlated with experiment, and do offer a systematic approach to addressing the issues. 

Here we introduce some utility code known as ‘Tautomatic’. This then supports the combination of some pre-existing open source tools  to provide a facile workflow for tautomer exploration and scoring. The existing tools that are combined are as follows: 

[1] Ambit-tautomers, created by Jeliazkova and co-workers and described here:

https://pubmed.ncbi.nlm.nih.gov/27481667/

This is used for enumerating possible tautomers but not for scoring them. 

[2] Open Babel created by O’Boyle and co-workers and described here:

https://jcheminf.biomedcentral.com/articles/10.1186/1758-2946-3-33

This is used for convenient file format manipulation.

[3] the density functional tight binding code (xtb) created by Grimme and co-workers and described here:

https://pubs.acs.org/doi/full/10.1021/acs.jctc.8b01176

This is used for re-scoring of the enumerated tautomers, in vacuo or in simulated solvents.

There are several ways to utilise the code.

* Simple command line usage, run separate scripts to (1) Enumerate tautomers (2) Rescore using xtb.
  This allows implicit solvent such as water, DMSO etc to be specified. (3) Find relative scores (as opposed to absolute scores).
* Run a bash 'wrapper' script called tautomerise.sh which simply links steps 1,2,3 above (solvent not added yet)
  It then also generates a helpful SVG image which can be loaded in your favourite browser.
* Run a Python Flask application, which runs a simple web server on the local machine on port 5000. Paste Smiles and Molecule name into the appropriate URL.
  This runs the 3 steps described above and loads the SVG image of the tautomer structures and relative scores into the browser.
* Download a Docker container from Docker Hub, this has the code and required dependencies already installed (Flask lacking - to be updated soon)
  You can then start a shell inside the container and execute the code there. 

Please now refer to the manual for installation and usage information using the Linux command line and Flask application.
If you wish to obtain and use a Docker container for the tautomatic application - see the docker_usage documentation. 
