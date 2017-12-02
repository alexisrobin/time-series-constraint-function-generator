# time-series-constraint-function-generator

This repository contains an engine module aiming to generate time series pattern constraint functions.<br/>
The process used is described in the following publication: [master_oro_automata_synthesis](./res/master_oro_automata_synthesis.pdf)

<strong>The generated functions file is right here: [constraint_function.py](./src/test/constraint_function.py)</strong>

## Environment

Tested and validated using <strong>Python 3.6.2</strong>

## HOW TO

### Generating function

The process uses [seed transducers input file](./input/seed.pl) and [decoration tables input file](./input/tables.pl) and generates the [constraint functions output file](./src/test/constraint_function.py).

```
cd src
python -m test.test_gen
```

### Testing function

The testing file times and validates some random generated functions based on data found in the following publication: [Global Constraint Catalog, Volume II, Time-Series Constraints](https://arxiv.org/abs/1609.08925)

```
cd src
python -m test.test_func
```