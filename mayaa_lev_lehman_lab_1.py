# -*- coding: utf-8 -*-
"""Mayaa Lev Lehman Lab 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sMC1Jf3Iy8zxr7Gfr2ED_TORdxi3tGwY

## Python Basics

### Calculator
"""

# Comments with hashtag, python ignores this

#how to add and subtract
30.34321 + 9.12313 - 3.5567

#how to multiply
2*2

#how to raise numbers to the power of (in this case) to the power of 8
2**8

2**123 #2 to the power of 123

2**12345 #2 to the power of 12345

import sys #importing sys module to provide access to varaibles that are used/maintained in python
sys.set_int_max_str_digits(100000) #setting max numbers of digits for integer string representation
2**45678 # 2 raised to 45678

#how to do division
8/4

#one more way for division
8//4

6//2

#modular arithmetic
8%12

13%12

22%12

24%12

"""### How many apples/oranges, total, cost for each, total cost"""

apples = 5 #5 apples

oranges = 8 #8 oranges

total = apples + oranges #5+8

total

apples**2 #square the number of apples (i.e 5**2)

cost_per_apple = 0.25

total_apple_costs = cost_per_apple * apples #cost of all 5 apples

total_apple_costs #0.25*5

"""### Vectors"""

#numpy for numerical operations
import numpy as np
# matplotlib.pyplot for plots
import matplotlib.pyplot as plt

# creating an array of integers
np.arange(10) #starting from 0 and going up to 10 but not including 10

x = np.arange(10)

x #printing the array

y = 3 * x + 5 #plugging in the values of array x to y

y #printing the new array (y)

# x = np.array([133,24,333,4,5,6])
# y = np.array([11,22,33,44,55,66])

x,y #the x and y coordinates (array coordinates)

"""### Plotting"""

#plotting (x,y) using the values above for x and for y
plt.plot(x,y)

#plotting same function but in blue dots
plt.plot(x,y,'.')

#plotting same function but in red dots
plt.plot(x,y,'r.')

#plotting same function in dashed blue line
plt.plot(x,y,'b--')

#to generate plots
import matplotlib.pyplot as plt

plt.plot(x,y)

"""### Creating a curve"""

# creating an array of 10 numbers
x = np.linspace(0,5,10) #from 0 to 5

x #array x

y = x**2 #squaring the values in array x to get array y

y #array y

#plotting the array of x,y
plt.plot(x,y)

plt.plot(x,y)
plt.title("New Graph of x**2"); #adding title to the graph
plt.xlabel("x"); #labeling the x axis as "x"
plt.ylabel("y"); #lableing the y axis as "y"

plt.plot(x,y,label="x squared") #plotting the graph of x squared, and labeling it so that it would show up as "x squared" in the legend
plt.title("Graph of x**2"); #plot title
plt.xlabel("x"); #labeling x axis
plt.ylabel("y"); #labeling y axis
plt.legend() #legend i.e. key to the plot

"""### How to plot; linear curve, quadratic curve, and cubic curve"""

#creating an array of 100 numbers between 0 and 2
x = np.linspace(0, 2, 100)

#plotting the functions:
plt.plot(x, x, label='linear')
plt.plot(x, x**2, label='quadratic')
plt.plot(x, x**3, label='cubic')

plt.xlabel('x label') #labeling the x axis
plt.ylabel('y label') #labeling the y axis

plt.title("Simple Plot") #plot title

plt.legend() #display the legend

"""### How to make a pie chart"""

labels = 'Frogs', 'Dogs', 'Cats', 'Birds' #labeling each slice
sizes = [15, 30, 40, 15] #size in percentages
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Dogs') #i.e. the orange slice

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show() #display the chart

"""### Graph of Sin function"""

import numpy as np #for numerical operations
import matplotlib.pyplot as plt #for creating plots

#array 't' with values from 0.0 to 2.0, with a step of 0.01
t = np.arange(0.0, 2.0, 0.01) #(start, stop, step)

s = np.sin(2*np.pi*t) #to compute the sine of 2*pi*t for each element in t

#plotting t vs s
plt.plot(t, s) #t is the x axis, s is the y axis
plt.title(r'$\alpha_i > \beta_i$', fontsize=20) #title of the plot, its font size
plt.text(1, -0.6, r'$\sum_{i=0}^\infty x_i$', fontsize=20) #summation that will be displayed in the plot
plt.text(0.5, 0.6, r'$\mathcal{A}\mathrm{sin}(2 \omega t)$',fontsize=15) #more text to be displayed in the plot
plt.xlabel=('time (s)') #time in seconds
plt.ylabel=('volts (mV)') #volts in mV
plt.grid(True) #show grid lines (just like in a math notebook)
plt.show() #show plot

"""Plot the following functions from $x = -10$ to $x = 10$

(Hint: np.sin, np.exp)

$y = 10x+7$

$y = -3x-12$

$y=\sin(x)$

$y=e^x$

$y=e^{-x^2}$
"""

#importing libraries
import numpy as np #for numerical operations
import matplotlib.pyplot as plt #to create plots
import math #for mathmatical operations
#range of x (from -10 to 10 in this example)
x=np.linspace(-10,10)

#varius y's
y1 = 10*x +7
y2 = -3*x -12
y3 = np.sin(x)
y4 = np.exp(x)
y5 = np.exp(-x**2)

#plotting the functions:
plt.plot(x, y1, label='y = 10x + 7')
plt.plot(x, y2, label='y = -3x - 12')
plt.plot(x, y3, label='y = sin(x)')
plt.plot(x, y4, label='y = e^x')
plt.plot(x, y5, label='y = e^(-x^2)')

plt.xlabel='x' #labeling the x axis
plt.ylabel='y' #labling the y axis
plt.title("Varius Functions on the xy Plane") #plot title
plt.legend() #the legend
plt.grid(True) #show grid
plt.show #display the plot

"""### Same five functions but plotted separately"""

import numpy as np
import matplotlib.pyplot as plt
import math
#the range of x (from -10 to 10 in this example)
x=np.linspace(-10,10)

y1 = 10*x +7
plt.title('y = 10x + 7') #title for y1
plt.xlabel='x' #label x axis
plt.ylabel='y' #label y axis
plt.plot(x, y1, label='y = 10x + 7') #plot the y1 function
plt.grid(True) #show grid
plt.show() #display the plot

y2 = -3*x -12
plt.title('y = -3x - 12') #title for y2
plt.xlabel='x' #label x axis
plt.ylabel='y' #label y axis
plt.plot(x, y2, label='y = -3x - 12') #plot the y2 function
plt.grid(True) #show grid
plt.show() #display the plot

y3 = np.sin(x)
plt.title('y = sin(x)') #title for y3
plt.xlabel='x' #label x axis
plt.ylabel='y' #label y axis
plt.plot(x, y3, label='y = sin(x)') #plot the y3 function
plt.grid(True) #show grid
plt.show() #display the plot

y4 = np.exp(x)
plt.title('y = e^x') #title for y4
plt.xlabel='x' #label x axis
plt.ylabel='y' #label y axis
plt.plot(x, y4, label='y = e^x') #plot the y4 function
plt.grid(True) #show grid
plt.show() #display the plot

y5 = np.exp(-x**2)
plt.title('y = e^(-x^2)') #title for y5
plt.xlabel='x' #label x axis
plt.ylabel='y' #label y axis
plt.plot(x, y5, label='y = e^(-x^2)') #plot the y5 function
plt.grid(True) #show grid
plt.show() #display the plot

"""### Plotting Success Levels

Pick out a plot of your choice from [here](https://matplotlib.org/stable/gallery/index.html), copy the code to this notebook, run, and document to the best of your abilities.
"""

#importing libraries
import matplotlib.pyplot as plt #to create plots
import numpy as np #for numerical operations

from matplotlib.colors import Normalize #normalizing color scale
from matplotlib.markers import MarkerStyle #costum marker styles
from matplotlib.text import TextPath #creating text based paths
from matplotlib.transforms import Affine2D #for applying affine transformations to objects

#symbols for plotting
SUCCESS_SYMBOLS = [
    TextPath((0, 0), "☹"),
    TextPath((0, 0), "😒"),
    TextPath((0, 0), "☺"),
]

N = 25 # N data points
skills = np.random.uniform(5, 80, size=N) * 0.1 + 5 #random (scaled) skill levels
takeoff_angles = np.random.normal(0, 90, N) #random takeoff angles (normal distribution)
thrusts = np.random.uniform(size=N) # random thrust values (uniform distribution)
successful = np.random.randint(0, 3, size=N) #random mood indices (0, 1, or 2)
positions = np.random.normal(size=(N, 2)) * 5 #random 2D positions (normal distribution)
data = zip(skills, takeoff_angles, thrusts, successful, positions) #zipping data together

cmap = plt.colormaps["jet"]
fig, ax = plt.subplots()
fig.suptitle("Throwing success", size=14) #figure title
#plotting the data
for skill, takeoff, thrust, mood, pos in data:
    t = Affine2D().scale(skill).rotate_deg(takeoff) #transforming the marker based on skill and takeoff angle
    m = MarkerStyle(SUCCESS_SYMBOLS[mood], transform=t) #using the transromed text path to create a costum marker style
    ax.plot(pos[0], pos[1], marker=m, color=cmap(thrust)) #plotting each point with a costum marker


plt.show()







"""### Graphics Output"""

#importing functions from python to display HTML content
from IPython.core.display import display, HTML

display(HTML('<h1>Hello World!</h1>')) #display of "Hello World!" (the HTML content)



"""### Numpy - Numerical Python

### Print random numbers
"""

import numpy as np #for numerical operations

#generating random number between 0 and 1
np.random.random() #[0.0, 1.0)

#generating another random number
np.random.random() > 0.5; #comparing the random number to 0.5

"""True or False"""

#generating a random number r and comparing it to 0.5
r = np.random.random(); print(r); r >0.5

#print r
r

r > 0.5 #is r greater than 0.5?







"""### Heads or Tails"""

#simulating a coin flip
def flip_coin(): #50-50 chance
    if np.random.random() > 0.5: #generating random number between 0 and 1 and comparing it to 0.5
        print("Heads") #if the number is greater than 0.5 print "Heads"
    else:
        print("Tails") #if the number is less than or equal to 0.5 print "Tails"

flip_coin()

np.random.randint(15,20) #random integer (15,19]

def coin():
  return np.random.randint(2) #generates either 0 or 1

coin()

def coin():
  return np.random.randint(3) #generates either 0, 1 or 2
  #simulating a three sided coin (in reality this doesn't exist because a coin has only two sides to it)

coin()

"""### Display of Coins: Heads or Tails"""

#display of a quarter
display(HTML('<img src="https://random-ize.com/coin-flip/us-quarter/us-quarter-front.jpg">'))

#display of Heads
heads = 'https://random-ize.com/coin-flip/us-quarter/us-quarter-front.jpg'
#display of Tails
tails = 'https://random-ize.com/coin-flip/us-quarter/us-quarter-back.jpg'

def show_img(img): #to display the image of either heads or tails
  display(HTML('<img src=' + img + '>'))

show_img(heads) #show heads

show_img(tails) #show tails

def flip_coin(): #play game Heads or Tails

    if coin(): #if coin returns true show heads
        show_img(heads)
    else: #else show tails
        show_img(tails)

flip_coin()

for i in range(5): #show five coins and randomly display them as heads or tails
    flip_coin()





"""### Play with Deck of Cards"""



# Base URL components for card images
card_url_head = "https://www.improvemagic.com/wp-content/uploads/2020/11/" #I dont have access to it
card_url_tail = ".png"

#arrays of suits and cards
suit = ['k','p','s','l'] #clubs,spades,hearts,diamonds
card = ['a','2','3','4','5','6','7','8','9','10','j','q','k']

i = np.random.randint(4) #random integer 'suit'
j = np.random.randint(13) # random integrer 'card'

i,j #suit,card

suit[i] #print random suit

card[j] #print random card

# Defining a function that will return a Card image URL
def card_image(card_number):

    i = card_number//13
    j = card_number%13

    return suit[i]+card[j]

card_image(3)

from IPython.display import Image, display #to show image

def show_img(img_url): #using the url of the card images
    display(Image(url=img_url))
img = card_url_head + card_image(3) + card_url_tail

img

show_img(img)

for i in range(52): #range of 52 cards
    img = card_url_head + card_image(i) + card_url_tail #print the deck of cards (in order)
    show_img(img)

import random

def initialize_deck():
    #Create and shuffle a deck of 52 cards represented by numbers 0-51.
    deck = list(range(52))
    random.shuffle(deck)
    return deck

def draw_cards(deck, top_index, num=5): #simulating draw of cards from the deck
    drawn_cards = deck[top_index:top_index + num]
    return drawn_cards, top_index + num

# Initialize and shuffle the deck
deck = initialize_deck()
top_index = 0  # Start at the beginning of the deck

deck

# Draw 5 cards for a poker hand
hand, top_index = draw_cards(deck, top_index, 5) #draw five cards from deck

hand #print cards in hand

hand, top_index = draw_cards(deck, top_index, 5) #draw five cards from deck

hand #print cards in hand

# Display the hand
for card_number in hand:
    img_url = card_url_head + card_image(card_number) + card_url_tail #show cards in a column
    show_img(img_url) #display the five cards in hand

from IPython.core.display import display, HTML
def show_hand(hand):
    #show cards in a row (since we drew five cards there is going to be 2 rows)
    images_html = ''.join([f'<img src="{card_url_head + card_image(card_number) + card_url_tail}" style="display:inline-block; margin:5px;" />' for card_number in hand])
    display(HTML(images_html))

show_hand(hand) #display the five cards





"""# Rank Hand"""

def evaluate_hand(hand):
    #to map card ranks to their values
    rank_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'j': 11, 'q': 12, 'k': 13, 'a': 14}
    #represent the suits as characters
    suits = ['k', 'p', 's', 'l']  # clubs, spades, hearts, diamonds

    # Convert the hand to a list of (rank, suit) tuples
    converted_hand = [(rank_values[card[card_number % 13]], suits[card_number // 13]) for card_number in hand]
    converted_hand.sort()

    #counting the occurrences of each rank and suit in the hand
    rank_counts = {rank: 0 for rank in rank_values.values()}
    suit_counts = {suit: 0 for suit in suits}
    for rank, suit in converted_hand:
        rank_counts[rank] += 1
        suit_counts[suit] += 1

    # Check for flush
    is_flush = max(suit_counts.values()) == 5

    # Check for straight and royal flush
    rank_sequence = [rank for rank, _ in converted_hand]
    is_straight = all(rank_sequence[i] - rank_sequence[i - 1] == 1 for i in range(1, 5))
    is_royal = is_straight and rank_sequence[0] == 10

    # Check for other hand types
    pairs = sum(1 for count in rank_counts.values() if count == 2)
    three_of_a_kind = 3 in rank_counts.values()
    four_of_a_kind = 4 in rank_counts.values()

    # determining the best hand type in order of rank
    if is_royal and is_flush:
        return "Royal Flush"
    elif is_straight and is_flush:
        return "Straight Flush"
    elif four_of_a_kind:
        return "Four of a Kind"
    elif three_of_a_kind and pairs == 1:
        return "Full House"
    elif is_flush:
        return "Flush"
    elif is_straight:
        return "Straight"
    elif three_of_a_kind:
        return "Three of a Kind"
    elif pairs == 2:
        return "Two Pair"
    elif pairs == 1:
        return "One Pair"
    else:
        return "High Card" #defult hand type if none of the above conditions are met



"""Shuffle cards"""

# Initialize and shuffle the deck
deck = initialize_deck()
top_index = 0  # Start at the beginning of the deck

hand, top_index = draw_cards(deck, top_index, 5) #five cards


print(evaluate_hand(hand))
show_hand(hand)



for i in range(10): #looping 10 times
    # Initialize and shuffle the deck
    deck = initialize_deck()
    top_index = 0  # Start at the beginning of the deck

    hand, top_index = draw_cards(deck, top_index, 5) #draw five cards each time


    print(evaluate_hand(hand))
    show_hand(hand)



for i in range(100): #looping 100 times
    # Initialize and shuffle the deck
    deck = initialize_deck()
    top_index = 0  # Start at the beginning of the deck

    hand, top_index = draw_cards(deck, top_index, 5) #draw 5 cards each time

    if evaluate_hand(hand) == "Two Pair":
        print("Winner!") #if it's "Two Pair" you win!
        show_hand(hand)



for i in range(1000): #looping 1000 times
    # Initialize and shuffle the deck
    deck = initialize_deck()
    top_index = 0  # Start at the beginning of the deck

    hand, top_index = draw_cards(deck, top_index, 5) #draw five cards each time

    if evaluate_hand(hand) == "Flush":
        print("Winner!")
        show_hand(hand)

# Commented out IPython magic to ensure Python compatibility.
# #how much time does it take to get winning cards
# %%timeit
# # Initialize and shuffle the deck
# deck = initialize_deck()
# top_index = 0  # Start at the beginning of the deck
# 
# hand, top_index = draw_cards(deck, top_index, 5) #draw five cards every time
# 
# if evaluate_hand(hand) == "Royal Flush":
#     print("Winner!")
#     show_hand(hand)

for i in range(1000000): #looping 1000000 times
    # Initialize and shuffle the deck
    deck = initialize_deck()
    top_index = 0  # Start at the beginning of the deck

    hand, top_index = draw_cards(deck, top_index, 5)

    if evaluate_hand(hand) == "Royal Flush":
        print("Winner!")
        show_hand(hand)

"""The above is first try!!!!! yay"""



#reset the wins to zero, initialize a counter for wins
wins = 0
N = 10000000   # N trials

for i in range(N): #looping it N times
    # Initialize and shuffle the deck
    deck = initialize_deck()
    top_index = 0  # Start at the beginning of the deck

    hand, top_index = draw_cards(deck, top_index, 5)

    if evaluate_hand(hand) == "Royal Flush":
        wins += 1
        print("Winner!")
        show_hand(hand) #display the cards in the hand

#the probability of drawing a Royal Flush
wins/N

