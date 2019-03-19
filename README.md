# StyleGAN - Modified to reproduce https://www.thiswaifudoesnotexist.net/ waifus' generation
This modification was tested on Archlinux with those specifications :
- Kernel: 5.0.2-arch1-1-ARCH
- CPU: Intel i7-6700 @ 4.000GHz
- GPU: NVIDIA GeForce GTX 1060 6GB
- RAM: 16GB
- Tensorflow: 1.14.1-dev20190319 (any after 1.10 should work)
- Cuda: 10.0.130 (any 10.0 will work but not 10.1)

## My python installation
`python --version`
```
Python 3.7.2
```
`python -m pip --version`
```
pip 18.1 from /usr/lib/python3.7/site-packages/pip (python 3.7)
```
Python modules used :
- os
- pickle
- numpy
- PIL/Image
- dnnlib
- config
- sys

## How I installed all of it
First, git clone the repo:
```
git clone https://github.com/LaurentBouchard/stylegan
```
Second, download [the model](https://mega.nz/#!aPRFDKaC!FDpQi_FEPK443JoRBEOEDOmlLmJSblKFlqZ1A1XPt2Y) in the repo directory.
This file was shared on [Gwern's blogpost about TWDNE](https://www.gwern.net/TWDNE#downloads).

Third, make sure python 3.7 is installed with pip. You can find info on how to do that [here](https://docs.python.org/3/using/index.html).

Fourth, run the following command from the repo directory :
```
python pretrained_example.py myfirstwAIfus 0.3 10
```
This command will start generating 10 images with a psi of 0.3 and it will store the results in ./results/myfirstwAIfus

This should work for you too. If not, you are missing some dependences. You need to have Cuda 10.0 and Tensorflow 1.10 or newer to be able to run the python script with success.

## Issues
If any of them is missing, you'll get an error at runtime. Just read the error and install the missing module with `python -m pip install <module>`.  

If an error is not documented, just open an issue and I'll try to help you. Just make sure to check if the issue is not already open.
