from collections import defaultdict
#PATH_INPUT = '/Users/hardikmehta/Documents/hash_code/Wanderlust-HashCode21/main/'
input_file = open('test_input.txt','r')
output_file = open('result.txt','w')

line = input_file.readline().split()
simulationTime = int(line[0])
intersectionCount = int(line[1])
streetCount = int(line[2])
numCars = int(line[3])
scorePerCar = int(line[4])

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


var = 0
dic_street = {}
# name -> (start, end, weight)
dic_rev_street = {}
Graph = defaultdict()
for n in range(0,intersectionCount):
    Graph[n] = []
    
while var<streetCount:
    line = input_file.readline().split()
    dic_street[line[2]] = ( int(line[0]), int(line[1]), int(line[3] ) )
    dic_rev_street[ (int(line[0]), int(line[1]) ) ] = line[2]
    Graph[int(line[1])].append(int(line[0]))
    var += 1

var = 0
cars = []
# carID -> Car Object
while var<numCars:
    line = input_file.readline().split()
    cur = Car(line[1:])
    cur.setIntersections(dic_street)
    cars.append(cur) 
    var += 1

print(Graph)
