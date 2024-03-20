# -*- coding: utf-8 -*-
"""Maya  Lab 5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LPs_GkdVHNp9OoTxOBYNc3JulXmvKi4y
"""

#importing libraries
import matplotlib.pyplot as plt #to generate plots of images or graphs
from PIL import Image # for image manipulation
import imageio.v2 as imageio #to read and write images

def plot(x):
    fig, ax = plt.subplots() #a figure and a single subplot

    #to dsiplay image x on subplot ax (in grayscale)
    im = ax.imshow(x,cmap='gray') #cmap to spefciy color map
    ax.axis('off') #focus is only on image content(focus is not on axis lines, etc.)
    fig.set_size_inches(20, 20) #figure size 20x20 inches
    plt.show() #display figure containing the image

#image url #storing the image url in "im"
im = imageio.imread('https://lospec.com/palette-list/st-64-natural-1x.png')

plot(im) #display image using the url

im.shape #image shape array (to understand its dimensions)

plot(im[:,40:41,:]) #displays a single coloumn from the image above (demonstrates slicing) #[all rows, coloumn 40:41, all color channels]

im[:,40:41,:]

im = imageio.imread('https://lospec.com/palette-list/waverator-1x.png') #image url #stored in "im"

plot(im) #display image using the url

im



import numpy as np #for numerical operations
import matplotlib.pyplot as plt #to generate plots

# Binary image - 3x3 matrix black and white
binary_image = np.array([
    [0, 1, 0], #0 is for black and 1 is for white
    [1, 1, 1],
    [0, 1, 0]
])

binary_image

plt.imshow(binary_image, cmap='gray') #(plot image, in grayscale)

# Grayscale image
grayscale_image = np.array([
    [50, 100, 150],
    [200, 255, 200],
    [150, 100, 50]
])
plt.imshow(grayscale_image, cmap='gray', vmin=0, vmax=255) #0-black, 255-white

# Grayscale image
grayscale_image = np.array([
    [0.2, 0.4, 0.6], #closer to zero is black, closer to 1 is white
    [0.8, 1.0, 0.8],
    [0.6, 0.4, 0.2] #here it's light --> dark
])
plt.imshow(grayscale_image, cmap='gray')

# RGB image
rgb_image = np.array([
    [[255, 0, 0], [0, 255, 0], [0, 0, 255]],
    [[255, 255, 0], [0, 255, 255], [255, 0, 255]],
    [[128, 128, 128], [255, 255, 255], [0, 0, 0]]
])

rgb_image

plt.imshow(rgb_image) #display colored 3x3 array

"""Red = [1,0,0],  
Green = [0,1,0],
Blue = [0,0,1]

likewise: Yellow = red+green= [1,1,0]
, Cyan = green+blue = [0,1,1]
, and magenta = red+blue = [1,0,1]
"""

# RGB image
rgb_image = np.array([ #array from 0 to 1
    [[1, 0, 0], [0, 1, 0], [0, 0, 1]],
    [[1, 1, 0], [0, 1, 1], [1, 0, 1]],
    [[0.5, 0.5, 0.5], [1, 1, 1], [0, 0, 0]]
])

# RGB image
rgb_image = np.array([
    [[1, 0, 0], [0, 1, 0], [0, 0, 1]],
    [[1, 1, 0], [0, 1, 1], [1, 0, 1]],

])

rgb_image

#plotting second version of the RGB image
plt.imshow(rgb_image*255) #the range is from 0 to 255



x = np.zeros((2,2,3)) #initialize array with zeros
x[:,:,0] = 1 #red pixles
plt.imshow(x)

x = np.zeros((2,2,3)) #initial array with zeros
x[:,:,1] = 1 #green pixles
plt.imshow(x)

x = np.zeros((2,2,3)) #initial array with zeros
x[:,:,2] = 1 #blue pixles
plt.imshow(x)

x = np.zeros((2,2,3)) #initial array with zeros
x[:,:,0] = 1 #red pixels
x[:,:,1] = 1 #green pixles
plt.imshow(x) #display red+green = yellow (in RGB model)

x = np.zeros((2,2,3)) #initial array with zeros (zero means black)
x[:,:,1] = 1 #green pixels
x[:,:,2] = 1 #blue pixles
plt.imshow(x) ##display cyan pixles i.e. green+blue

x = np.zeros((2,2,3)) #initial array with zeros
x[:,:,0] = 1 #red pixles
x[:,:,2] = 1 #blue pixels
plt.imshow(x) #display magneta pixles i.e. red+blue

x = np.zeros((2,2,3)) #initial array with zeros
x[:,:,0] = 0.5
x[:,:,1] = 0.5 # 0 to 1 in rgb
x[:,:,2] = 0.5
plt.imshow(x) #gray pixles

x = np.zeros((2,2,3)) #initial array with zeros
x[:,:,0] = 1
x[:,:,1] = 1
x[:,:,2] = 1
plt.imshow(x) #display white pixels (1 in rgb = white)

x = np.zeros((2,2,3)) #initial array with zeros
x[:,:,0] = 0
x[:,:,1] = 0 #black pixels (0 is black in rgb)
x[:,:,2] = 0 #red blue and green channels are set to o
plt.imshow(x)



r = np.random.rand() #generates random number from 0 to 1

r #show random number



r = np.random.rand()
g = np.random.rand()
b = np.random.rand()

#initializing array with zeros (black)
x = np.zeros((2,2,3))

x[:,:,0] = r #red
x[:,:,1] = g #green
x[:,:,2] = b #blue


plt.imshow(x) #display the random color



for i in range(5):

    #initializing array with one's (white)
    z = np.ones((10,10,3))

    r = np.random.rand()
    g = np.random.rand()
    b = np.random.rand()

    print(r,g,b)
#assign their values to red green and blue
    z[:,:,0] = r
    z[:,:,1] = g
    z[:,:,2] = b

    plt.imshow(z); #show 5 random colors
    plt.show()





for i in range(5):

    z1 = np.ones((10,10,3)) #initialize z1 with ones (white)
    z2 = np.ones((10,10,3)) #initialize z2 with ones (white)

#random values for RGB
    r = np.random.rand()
    g = np.random.rand()
    b = np.random.rand()
#z1 with RGB values
    z1[:,:,0] = r
    z1[:,:,1] = g
    z1[:,:,2] = b
#fills z2 with the complementary color
    z2[:,:,0] = 1-r
    z2[:,:,1] = 1-g
    z2[:,:,2] = 1-b

    z3 = np.hstack((z1,z2)) #combine colors to form z3

    plt.imshow(z3);
    plt.show()



z1 = np.ones((10,10,3)) #initialize array with ones
z1[:,:,0] = np.random.rand() #z1 is filled with random RGB values
z1[:,:,1] = np.random.rand()
z1[:,:,2] = np.random.rand()

z2 = np.ones((10,10,3)) #z2 is filled with random RGB values
z2[:,:,0] = np.random.rand()
z2[:,:,1] = np.random.rand()
z2[:,:,2] = np.random.rand()

zavg = (z1+z2)/2 #average RGB values between z1 and z2

z3 = np.hstack((z1,zavg,z2)) #plotting (z1, average RGB values between z1 and z2, z2)

plt.imshow(z3);
plt.show()



z1 = np.ones((10,10,3)) #initialize array with ones (white)
#z1 is filled with random RGB values
z1[:,:,0] = np.random.rand()
z1[:,:,1] = np.random.rand()
z1[:,:,2] = np.random.rand()

z2 = np.ones((10,10,3)) #initialize arrat with ones (white)
#z2 is filled with random RGB values
z2[:,:,0] = np.random.rand()
z2[:,:,1] = np.random.rand()
z2[:,:,2] = np.random.rand()

zavg = (z1+z2)/2 #average between z1 and z2

z1a = (z1+zavg)/2 #gradient
z2a = (z2+zavg)/2

z3 = np.hstack((z1,z1a,zavg,z2a,z2))

plt.imshow(z3); #show z3
plt.show()





for i in range(100): #loop 100 times

    z1 = np.ones((10,10,3)) #initialize z1 with ones
#z1 is filled with random RGB values
    z1[:,:,0] = np.random.rand()
    z1[:,:,1] = np.random.rand()
    z1[:,:,2] = np.random.rand()

    z2 = np.ones((10,10,3))#initialize arrat with ones (white)
#z2 is filled with random RGB values
    z2[:,:,0] = np.random.rand()
    z2[:,:,1] = np.random.rand()
    z2[:,:,2] = np.random.rand()

    zavg = (z1+z2)/2 #average between z1 and z2

    z1a = (z1+zavg)/2 #gradient
    z2a = (z2+zavg)/2

    z3 = np.hstack((z1,z1a,zavg,z2a,z2))

    plt.imshow(z3); #show z3
    plt.show()



import numpy as np #for numerical operations
import matplotlib.pyplot as plt #to generate plots

def recursive_average(colors):
    """
    Compute the recursive average of the given list of colors.

    Parameters:
    - colors: List of color arrays

    Returns:
    - A new list of color arrays containing the recursive averages.
    """
    new_colors = [colors[0]]
    for i in range(1, len(colors)):
        avg_color = (colors[i] + new_colors[-1]) / 2.0
        new_colors.extend([avg_color, colors[i]])
    return new_colors

def generate_recursive_colors_v2(passes):
    """
    Generate a visualization of 2 random colors and their recursive averages for a number of passes.

    Parameters:
    - passes: Number of times to apply the recursive averaging process

    Returns:
    - An image showing the 2 endpoint colors and their recursive averages.
    """
    # Start with 2 random colors
    colors = [np.ones((10,10,3)) for _ in range(2)]
    for color in colors:
        color[:,:,0] = np.random.rand()
        color[:,:,1] = np.random.rand()
        color[:,:,2] = np.random.rand()

    # Apply the recursive averaging for the specified number of passes
    for _ in range(passes):
        colors = recursive_average(colors)

    # Horizontally stack the colors
    result = np.hstack(colors)

    return result

for i in range(5):
    img = generate_recursive_colors_v2(i)
    plt.imshow(img)
    plt.axis('off')
    plt.tight_layout()
    plt.show()

import numpy as np #for numerical operation
import matplotlib.pyplot as plt #to generate plots

def recursive_average(colors):

    new_colors = [colors[0]]
    for i in range(1, len(colors)):
        avg_color = (colors[i] + new_colors[-1]) / 2.0
        new_colors.extend([avg_color, colors[i]])
    return new_colors

def generate_recursive_colors_v2(passes, initial_colors):

    colors = initial_colors.copy()

    for _ in range(passes):
        colors = recursive_average(colors)

    result = np.hstack(colors)

    return result

initial_colors = [np.ones((10, 10, 3)) for _ in range(2)]
for color in initial_colors:
    color[:,:,0] = np.random.rand()
    color[:,:,1] = np.random.rand()
    color[:,:,2] = np.random.rand()

passes_values = [0,1,2,3,4]
imgs = [generate_recursive_colors_v2(p, initial_colors) for p in passes_values]

fig, axs = plt.subplots(1, len(passes_values), figsize=(15, 5))

for ax, img, p in zip(axs, imgs, passes_values):
    ax.imshow(img)
    ax.axis('off')
    ax.set_title(f'Passes={p}')

plt.tight_layout()
plt.show()

"""https://lospec.com/palette-list"""

import numpy as np #for numerical operations
import matplotlib.pyplot as plt #to generate plots
import matplotlib.colors as mcolors
import matplotlib
import imageio.v2 as imageio
from PIL import Image

def get_colors_lospec(url):
    im = imageio.imread(url)
    rgb_list = (im/255)[0,:,0:3]
    float_list = list(np.linspace(0,1,len(rgb_list)))
    cdict = dict()
    for num, col in enumerate(['red', 'green', 'blue']):
        col_list = [[float_list[i], rgb_list[i][num], rgb_list[i][num]] for i in range(len(float_list))]
        cdict[col] = col_list
    cmp = mcolors.LinearSegmentedColormap('my_cmp', segmentdata=cdict, N=256)
    return cmp

url = 'https://lospec.com/palette-list/agb-32x.png'
im =imageio.imread(url)
plt.imshow(im);

url = 'https://lospec.com/palette-list/agb-1x.png'
im =imageio.imread(url)
plt.imshow(im);

url = 'https://lospec.com/palette-list/moondrom-1x.png'
im = imageio.imread(url)
plt.imshow(im);

z = np.random.randint(0,255,size=(10,10))

plt.imshow(z, cmap=get_colors_lospec(url)) #choose colors here
plt.colorbar();

x, y = np.mgrid[-5:5:0.05, -5:5:0.05]
z = np.sqrt(x**2 + y**2)

z.shape

x

y

z = np.sqrt(x**2 + y**2)

z.shape

plt.imshow(x)

plt.imshow(y)

z

plt.imshow(z, cmap=get_colors_lospec(url));
plt.show()



x, y = np.mgrid[-5:5:0.05, -5:5:0.05]

z = np.sin(3*y)

plt.imshow(z, cmap=get_colors_lospec(url));
plt.show()

x, y = np.mgrid[-5:5:0.05, -5:5:0.05]

z = np.sin(3*x)

plt.imshow(z, cmap=get_colors_lospec(url));
plt.show()

x, y = np.mgrid[-5:5:0.05, -5:5:0.05]

z = np.sin(3*y)*np.sin(3*x)

plt.imshow(z, cmap=get_colors_lospec(url));
plt.show()

paste a url in here to show shape