## TODO: define the convolutional neural network architecture

import torch
from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F
# can use the below import should you choose to initialize the weights of your Net
import torch.nn.init as I


class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        
        ## TODO: Define all the layers of this CNN, the only requirements are:
        ## 1. This network takes in a square (same width and height), 3-colour image as input
        ## 2. It ends with a linear layer that represents the keypoints
        ## it's suggested that you make this last layer output 136 values, 2 for each of the 68 keypoint (x, y) pairs
        
        # As an example, you've been given a convolutional layer, which you may (but don't have to) change:
        # 1 input image channel (grayscale), 32 output channels/feature maps, 5x5 square convolution kernel
        
        self.conv1 = nn.Conv2d(3, 32, 5)    #  224 x 224 # this time we left the colour channels in 
        self.conv1_bn = nn.BatchNorm2d(32)
        self.conv2 = nn.Conv2d(32, 64, 3)  
        self.conv2_bn = nn.BatchNorm2d(64)
        self.conv3 = nn.Conv2d(64, 128, 3)
        self.conv3_bn = nn.BatchNorm2d(128)
        
        self.maxPool = nn.MaxPool2d(2, 2)         

        self.fc3 = nn.Linear(128 * 26 * 26 , 10)
        self.fc4 = nn.Linear(10 , 1)
        
        # sigmoid returns a value between 0 -> 1
        self.sigmoid = nn.Sigmoid()
        
    def forward(self, x):

        ## x is the input image and, as an example, here you may choose to include a pool/conv step:

        x = self.maxPool(F.relu(self.conv1_bn(self.conv1(x)))) # 220 x 220 / 2 = 110 x 110
        x = self.maxPool(F.relu(self.conv2_bn(self.conv2(x)))) # 108 x 108 / 2 = 54 x 54
        x = self.maxPool(F.relu(self.conv3_bn(self.conv3(x)))) # 52  x 52  / 2 = 26 x 26
  
        x = F.relu(self.fc3(x.view(x.size(0), -1)))
        x = self.sigmoid(self.fc4(x))

        return x

