#!/bin/sh

set -xe
cd ..

# Show OT version
echo "Python interpreter"
echo `which python`
echo "OpenTURNS version"
python -c "import openturns; print(openturns.__version__); exit()"

# Notebooks in all subdirectories
cd examples
python ../tests/find-ipynb-files.py
cd ..

# Unit tests
cd tests
python demo_axialbeam.py
python demo_ishigami.py
python -m unittest discover .
cd ..


