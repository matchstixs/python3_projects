#dictionaries work using key:value pairs in arrays

##import external dictionary file, in this case we will use JSON dictionary file 

#1. interface: user input word
#2. word matching -> meaning
#3. print output
#4. error handling, cap case & lower case, 

##import and load
import json
data = json.load(open('INPUT DIRECT PATH'))

#1 & 4
usrinput = input("Color to Hex ").lower()

#2 script testing
# print(data["greenyellow"])

#3
print(data[usrinput])

### 4 steps, 4 lines of code