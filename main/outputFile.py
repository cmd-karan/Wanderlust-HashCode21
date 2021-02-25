class OutputFile:
    
    def getOutput(self, simulationTime, intersectionCount, streetCount, scorePerCar, graph, edgeToNode, nodeToEdge, carIDMap):
        output_file = open('output.txt','w')
        content = self.getOutputv1(simulationTime, intersectionCount, streetCount, scorePerCar, graph, edgeToNode, nodeToEdge, carIDMap)
        output_file.write(content)

    def streetWeight(self):
        return '1'
    def getOutputv1(self, simulationTime, intersectionCount, streetCount, scorePerCar, graph, edgeToNode, nodeToEdge, carIDMap):
        """
        Node 
        startNodeCount
        for startNode in graph[endNode]:
            streetName -startNode, endNode
            T = 1 (always)

        node number is from 0 to N-1

        Output Format:
        3
        1
        2
        rue-d-athenes 2 rue-d-amsterdam 1 0
        1 rue-de-londres 2
        2
        1 rue-de-moscou 1
        """
        res = [str(intersectionCount)]

        for endNode in range(intersectionCount):
            res.append(endNode)
            res.append(len(graph[endNode]))
            for startNode in graph[endNode]:
                streetName = nodeToEdge[(startNode, endNode)]
                res.append(streetName+self.streetWeight())

        return "\n".join([str(elem) for elem in res])
        
        
