import json

with open("test.json") as configFile:

    config = json.load(configFile)
    configFile.close()
    
axiom = config["axiom"]
variablesList = config["variables"]
rules = dict(config["rules"])
iters = config["iterations"]

currentString = axiom 

print("0", currentString)

for i in range(iters):
    newList = []
    
    for item in currentString:
        if item in rules.keys():
            newList.append(rules[item])
        
    currentString = ''.join(newList)
    
    print(i+1, currentString)
        
    




