[//]: # (Image References)

# Fruit Classifier

## Overview



### Local Environment Instructions

1. Clone the repository, and navigate to the downloaded folder. This may take a minute or two to clone due to the included image data.
```
git clone https://github.com/renatoSilvaAU/fruit.git
cd fruit
```

2. Create (and activate) a new environment, named `cv-nd` with Python 3.6. If prompted to proceed with the install `(Proceed [y]/n)` type y.

	- __Linux__ or __Mac__: 
	```
	conda create -n fruit python=3.6
	source activate fruit
	```
	- __Windows__: 
	```
	conda create --name fruit python=3.6
	activate fruit
	```

3. Install PyTorch and torchvision; this should install the latest version of PyTorch.
	
	- __Linux__ or __Mac__: 
	```
	conda install pytorch torchvision -c pytorch 
	```
	- __Windows__: 
	```
	conda install pytorch-cpu -c pytorch
	pip install torchvision
	```

4. Install a few required pip packages, which are specified in the requirements text file (including OpenCV).
```
pip install -r requirements.txt
```

5. Ensure your Kernel can be used in Jupyter.
```
conda install ipykernel
python -m ipykernel install --user --name fruit --display-name "Python (fruit)"
```



### Data

All of the data you'll need to train a neural network is in the, in the subdirectory `data`. In this folder are training and tests set of images


LICENSE: This project is licensed under the terms of the MIT license.
