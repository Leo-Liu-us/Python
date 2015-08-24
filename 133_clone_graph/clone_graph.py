# Definition for a undirected graph node
#class UndirectedGraphNode(object):
#    def __init__(self, x):
#        self.label = x
#       self.neighbors = []

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        if node is None:
            return None
        
        #use dict to record the "processed" nodes
        #key is the node's label
        #value is the copied node
        copied_nodes = {}
        #use a queue to do BFS
        bfs_que = []
        
        #put node into queue
        bfs_que.append(node)
        
        while bfs_que:
            head = bfs_que.pop(0)
            label = head.label
            if label not in copied_nodes:
                #generating the head
                new_node = UndirectedGraphNode(label)
                copied_nodes[label] = new_node
            #deal with its neighbors
            for neighbor in head.neighbors:
				#if neighbor has not been copied yet, copy it and put the original into queue
                if neighbor.label not in copied_nodes:
                    new_neighbor = UndirectedGraphNode(neighbor.label)
                    copied_nodes[neighbor.label] = new_neighbor
                    bfs_que.append(neighbor)
                #update its neighbor
                copied_nodes[label].neighbors.append(copied_nodes[neighbor.label])

        return copied_nodes[node.label]