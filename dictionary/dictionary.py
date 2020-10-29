import json
from difflib import get_close_matches as gcm

# print(gcm('aka',['akash','aku','what','now'],cutoff = .5))
def getMean(inp):
    if inp in data:
        return data[inp]
    elif inp.upper() in data:
        return data[inp.upper()]
    elif inp.title() in data:
        return data[inp.title()]
    elif len(gcm(inp,data.keys())) > 0:
        print('did you mean %s instead'%gcm(inp,data.keys())[0])
        decide = input('Press Y for yes or N for no: ')
        if decide.lower() == 'y':
            return data[gcm(inp,data.keys())[0]]
        elif decide.lower() == 'n':
            print('can\'t find the meaning of this word')
        else:
            print('invalid input, enter Y or N')
    else: 
        print('can\'t find the meaning of this word')

data = json.load(open("data.json"))
inp = input('enter a word you want to search for: ')
mean = getMean(inp.lower())
if type(mean) == list:
    for item in mean:
        print(item)
else:
    if mean is not None:
        print(mean)