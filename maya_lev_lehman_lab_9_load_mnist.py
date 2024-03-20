# -*- coding: utf-8 -*-
"""Maya Lev Lehman Lab 9 Load MNIST.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11XbSnlpwF-E3FEyOyWZV5RiW8Vnn-ec-
"""

import torch
from torchvision import datasets, transforms
import numpy as np
# Define a transform to normalize the data
transform = transforms.Compose([transforms.ToTensor()])

# Download and load the MNIST training data
train_data = datasets.MNIST(root='./data', train=True, download=True, transform=transform)

# Extracting the data and targets as tensors
train_images = train_data.data
train_labels = train_data.targets

train_images.shape, train_labels.shape

import matplotlib.pyplot as plt #to generate plots

28*28

train_images[0,:,:] #selecting the image from the training dataset

x = train_images[0,:,:] #assgining to x

plt.imshow(x) #display x with its corresponding color values

train_labels[0]

x.shape

x.flatten()

x = x.flatten() #10 bits

x.shape #786 when it is falttened

x = x.reshape(28,28) #reshaping to 28x28

x.shape

m = torch.rand(10,784)

m

m.shape

x = x.flatten() #scaleing the matrix down because it was too big for matrix mult.

x = x/255.0

x

m.shape,x.shape #m and x shape

m@x #matrix mult.

y = torch.matmul(m,x) #y=m@x

y

torch.max(y) #or max(y)

torch.argmax(y) #second position in the array

x = train_images[0:25,:,:]/255.0

x.shape

x = x.reshape(25,784)

x.shape

x  = x.T #transpose

x.shape

y = m@x

y.shape

plt.imshow(y)

