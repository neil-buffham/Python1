# List of "random" colors to suggest to user
import random
color_list = ['Red', 'Green','Blue','Orange','Yellow','Purple','Teal','Brown','Grey','Hazel','Salmon','Pink','Tan'] 

# Generated value to pick the suggestion
consider = random.choice(color_list)

# Pop the question
color = input('What is your favorite color?')

# Deflection
print('You mentioned your favorite color is ',color,'. Have you considered the virtues of ',consider,'?',sep='')