"""
    edgeName: [startNode, endNode]
    (startNode, endNode): edgeName
    carID: [edgeNames],[nodeNames]

"""
"""
Get all the files 
get the input
comput the logic
get the output format
create a output file
and save it
#adJList
    #graph[endNode].append(startNode)

multi - score destination - (with weighted edges and waiting is changed as per our requirement)
"""
import os
import inputFile
import outputFile

if __name__=="__main__":
    print("main called maybe")
    currDir = os.getcwd()
    
    inputDir = os.path.join(currDir, "dataset")
    outputDir = os.path.join(currDir, "output")
    fileNames = list(os.listdir(inputDir))
    for fileName in fileNames:
        path = os.path.join(inputDir, fileName)
        simulationTime, intersectionCount, streetCount, scorePerCar, graph, edgeToNode, nodeToEdge, carIDMap = inputFile.getInput()
        #logic.Logic.computation(simulationTime, intersectionCount, streetCount, scorePerCar, graph, edgeToNode, nodeToEdge, carIDMap)
        s = outputFile.OutputFile.getOutput(simulationTime, intersectionCount, streetCount, scorePerCar, graph, edgeToNode, nodeToEdge, carIDMap)
        outputFileName = os.path.join(outputDir,fileName+"_output.txt")
        with open(outputFileName, 'w') as file:
            file.write(s)
    
        

        
        


