# pypif 
![status](https://travis-ci.org/CitrineInformatics/pypif.svg?branch=master)
![PyPI version](https://badge.fury.io/py/pypif.svg)

## About

Tools to serialize and deserialize to and from the [PIF](http://citrine.io/pif) schema.
This package provides python objects for each object in the PIF schema and methods
for serialization and deserialization.

There is a companion Java library called [JPIF](https://github.com/CitrineInformatics/jpif).

## Installation

### Requirements

* Python >= 2.7 or >= 3.3

### Setup

`pypif` is published on [PyPI](https://pypi.python.org/pypi/pypif), so it can be installed with `pip`:
```shell
$ pip install pypif
```

## Example

The following example creates a PIF record that saves the band gap of MgO2 as equal to 7.8 eV.

```python
from pypif import pif
from pypif.obj import *


chemical_system = ChemicalSystem()
chemical_system.chemical_formula = 'MgO2'

band_gap = Property()
band_gap.name = 'Band gap'
band_gap.scalars = 7.8
band_gap.units = 'eV'

chemical_system.properties = band_gap

print(pif.dumps(chemical_system, indent=4))
```

This example will serialize to the following JSON representation:

```json
{
    "category": "system.chemical",
    "chemicalFormula": "MgO2",
    "properties": {
        "units": "eV",
        "name": "Band gap",
        "scalars": [
            {
                "value": 7.8
            }
        ]
    }
}
```

# Schema

A detailed discussion of the PIF schema and usage are available at [http://citrine.io/pif](http://citrine.io/pif).