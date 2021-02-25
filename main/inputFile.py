from collections import defaultdict
import os
os.getcwd()

class Car:
    def __init__(self, streets):
        self.streets = streets
        self.intersections = []
        self.intersection_count = 0
        self.street_count = len(self.streets)
    def setIntersections(self, dic_street):
        for street in self.streets:
            self.intersections.append(dic_street[street][0])
        self.intersections.append(dic_street[self.streets[-1]][1])
        self.intersection_count = len(self.intersections)

class InputFile:
    def __init__(self):
        self.simulationTime = 0
        self.intersectionCount = 0
        self.streetCount = 0
        self.numCars = 0
        self.scorePerCar = 0
        self.nodeToEdge = {}
        self.edgeToNode = {}
        self.graph = defaultdict()
        self.carIDMap = []

    def setInputs(self, current):
        input_file = open('dataset/'+current+'.txt','r')
        line = input_file.readline().split()
        self.simulationTime = int(line[0])
        self.intersectionCount = int(line[1])
        self.streetCount = int(line[2])
        self.numCars = int(line[3])
        self.scorePerCar = int(line[4])
        for n in range(0,self.intersectionCount):
            self.graph[n] = []
        var = 0
        while var<self.streetCount:
            line = input_file.readline().split()
            self.edgeToNode[line[2]] = ( int(line[0]), int(line[1]), int(line[3] ) )
            self.nodeToEdge[ (int(line[0]), int(line[1]) ) ] = line[2]
            self.graph[int(line[1])].append(int(line[0]))
            var += 1

        var = 0
        while var<self.numCars:
            line = input_file.readline().split()
            cur = Car(line[1:])
            cur.setIntersections(self.edgeToNode)
            self.carIDMap.append(cur) 
            var += 1

def getInput(current):
    obj = InputFile()
    obj.setInputs(current)
    return obj.simulationTime, obj.intersectionCount, obj.streetCount, obj.scorePerCar, obj.graph, obj.edgeToNode, obj.nodeToEdge, obj.carIDMap

#print(getInput())