# Graph Lattice

SAT models for generating geometric lattices.

## Overview

The folders SGS and Codish contain models for geometric lattices with different approaches for symmetry breaking. The folder BaseModel does not implemenet any symmetry breaking. The file *SATGeoLattice.pdf* has more information about the model.

## Required Packages

The repository contains a python virtual environment, however all packages used are standard python packages. Python3 is assumed.

To run the solver, a working installation of [Savile Row](https://savilerow.cs.st-andrews.ac.uk/), [Conjure](https://github.com/conjure-cp/conjure.git) and [Mini SAT](http://minisat.se/) are required. Other Solvers can also be used, such as Minion. All need to be inside your path.

The scripts use standard Linux commands and terminal tools. A Linux shell is assumed.

A working installation of GAP is also necessary for symmetry breaking. Please add *gap.sh* (which lives inside the bin folder in your GAP installation directory, ie: *path/to/GAP/bin/gap.sh*) inside your local path and rename it to *gap*. This will ensure that gap commands can be run inside the working directory. Additionally, the package [yags](http://xamanek.izt.uam.mx/yags/) is necessary, this package is not provided in a normal installation of GAP. Additionally, [Nauty and/or Traces](https://users.cecs.anu.edu.au/~bdm/nauty/) may be needed to install *yags*.

## How to use

To run the experiment, go either SGS, Codish or BaseModel for the different solving approaches and execute:

```console
bash make.sh
```

To change the solver, simply change it inside make.sh. Here we use *--solver=nbc_minisat_all*

```console
conjure solve -ac --number-of-solutions=all --solver=nbc_minisat_all geo_sym.essence n.param
```

This can be changed to:

```console
conjure solve -ac --number-of-solutions=all --solver=minion geo_sym.essence n.param
```

We can aslo ask the solver to find only one solution by removing the flag *--number-of-solutions=all*. Other options are also available, to learn more, please run:

```console
conjure --help
```

The results can be seen inside the *Output* folder. For each size *n* we have a folder *Resultn* that contains the solutions, as well as meta data which can be found in *conjure-output*. Of particular interest is the file *.eprime-info*. For more information go to [https://github.com/conjure-cp/conjure].
