import json
import networkx as nx


def printDict(inDict):
    for k,v in inDict.items():
        if k != "pages" and k != "components":
            print(f"Key: {k}")
        if type(v) == dict:
            printDict(v)
        elif type(v) == list:
            if k == "components":
                print(f"Components: {v}\n")
            else:
                print(f"Pages: {v}")
        else:
            print(v, end="\n")

def getAdjacencyList(): 
    f = open('list.json')
    data = json.load(f)
    printDict(data)



def main():
    getAdjacencyList()

main()
