# python-ipykernel

Add a kernel from a virtualenv to jupyter lab

### Create a virtual environment

```
python3 -m venv .venv
source .venv/bin/activate
```

### Install ipykernel

```
pip install ipykernel
```

### Add the kernel to jupyter

```
% python -m ipykernel install --user --name myenv --display-name "Python (myenv)"
Installed kernelspec test in /Users/edward/Library/Jupyter/kernels/myenv
```
