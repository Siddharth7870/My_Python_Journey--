''' 

Q.   A file contains a word “Donkey” multiple times. You need to write a program 
,    which replace this word with ##### by updating the same file.

'''

# open file reading mode
with open("donkey/donkey.txt","r") as f:
    reading = f.read()
    print(reading)

# Replace donkey to #####
Replace = reading.replace("Donkey","#####")

# Open file written mode
with open("donkey/donkey.txt","w") as f:
    done = f.write(Replace)
    print(done)



