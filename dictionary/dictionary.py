#dictionaries work using key:value pairs in arrays

#import external dictionary file, in this case we will use JSON dictionary file 

#1. interface: user input word
#2. word matching -> meaning
#3. print output
#4. error handling, cap case & lower case, 

import json

data = json.load(open('/home/matchstix/Desktop/PyWork/python3_projects/dictionary/data.json'))

print(data)