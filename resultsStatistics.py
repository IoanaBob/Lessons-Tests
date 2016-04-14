import ast
import json

#JSON NEEDS TO BE IN THE FORMAT: {"username":{"test1":"[6,7,8]","test2":"[3,4,6]"}}

with open('results.json', 'r') as data:
    json_decode = json.load(data)

username = (input("input name:"))
def test1results(username, jsonfile):
       
    for test1 in jsonfile:
        usernames = test1
        if usernames == username:
            test1data = json_decode['username']['test1']
    test1data = ast.literal_eval(test1data)
    averagescore= sum(test1data)/len(test1data)
    topscore = max(test1data)
    print("\nScores for Test 1:", test1data)    
    print("\nAverage Score for Test 1:",averagescore)
    print("\nTop Score for Test 1:",topscore)  
    amountattempts = list(range(0,len(test1data)))    
    plt.plot(amountattempts, test1data, 'ro')
    plt.ylabel("Score")
    plt.xlabel("Attempts")
    plt.axis([-1,len(test1data)+1,0,10])
    plt.show()
    return test1data
    
def test2results(username, jsonfile):
        
    for test2 in jsonfile:
        usernames = test2
        if usernames == username:
            test2data = json_decode['username']['test2']
    test2data = ast.literal_eval(test2data)
    averagescore= sum(test2data)/len(test2data)
    topscore = max(test2data)
    print("\nScores for Test 2:", test2data)    
    print("\nAverage Score for Test 2:",averagescore)
    print("\nTop Score for Test 2:",topscore)
    amountattempts = list(range(0,len(test2data)))    
    plt.plot(amountattempts, test2data, 'ro')
    plt.ylabel("Score")
    plt.xlabel("Attempts")
    plt.axis([-1,len(test2data)+1,0,10])
    plt.show()
    return test2data


        
test1results(username,json_decode)
test2results(username,json_decode)

