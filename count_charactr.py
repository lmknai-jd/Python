message = 'Hello World!' # you can put literally anything here.
count = {}

for character in message.upper():#(or message.lower for lowercase.)
    count.setdefault(character, 0)
    count [character] = count [character] + 1

print (count)
    
