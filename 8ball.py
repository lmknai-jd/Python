import random

def getAnswer (x):
    if x == 1:
        return 'It is certain.'
    elif x == 2:
        return 'I think so?'
    elif x == 3:
        return 'Why not.'
    elif x == 4:
        return 'Maybe...'
    elif x == 5:
        return 'Go away. I dont feel like answering you right now.'
    elif x == 6:
        return "Ask again when you've thought about it"
    elif x == 7:
        return 'Nope!'
    elif x == 8:
        return 'Ehhh...not really.'
    elif x == 9:
        return "Not likely."
    elif x == 10:
        return "Answer unclear. Try again."

print ('Think of a yes/no question, and press "ENTER" to see your result!')
input ()

print (getAnswer (random.randint (1,10)))



    
