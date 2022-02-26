import random

prompt='name a food_'
import tkinter.filedialog

# define an empty list
a = []

# open file and read the content in a list
with open(r"E:\backup 2019-09-22\Python knowledge\LTP 2 Crafting Quality code\food.txt", 'r') as filehandle:  
    for line in filehandle:
        a.append(line.strip('\n'))
b=[]
t='Thank you for using "kia pkaoun aj"'
print('How this works: write the name of food that you would like to cook and press enter \n keep writing more names and press enter \n once you are done writing names of foods then type exit and press enter, if you want a random suggestion then type "show" without quotes and press enter \n it will show you a random name from your list to cook.')
b=input(prompt)
while not b=='exit':
    if b=='show':
        r=random.randint(1,(len(a)))
        r=random.randint(0,(len(a)-1))    
        print('you can cook','**',a[r],'**')
    a.append(b)

    if 'show' in a:
        a.remove('show')
    b=input(prompt)
with open(r"E:\backup 2019-09-22\Python knowledge\LTP 2 Crafting Quality code\food.txt", 'w') as filehandle:  
    for listitem in a:
        filehandle.write('%s\n' % listitem)


