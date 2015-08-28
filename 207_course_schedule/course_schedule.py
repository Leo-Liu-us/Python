class Solution(object):
    def canFinish(self, num_courses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        #use dict to store node and its predecessor
        #key: node label
        #value: list of predecessors
        pre_dict = {}
        
        for i in range(num_courses):
            pre_dict[i] = set([])
        
        #traverse prerequisites to set pre_dict
        for item in prerequisites:
            if item[1] not in pre_dict[item[0]]:
                pre_dict[item[0]].add(item[1])
            
        visited_num = 0
        zero_indegree_que = []
        
        while visited_num < num_courses:
            #trasver pre_dict and find all nodes whose indegree is 0
            for k, v in pre_dict.items():
                if not v:
                    #delete item k,v from pre_dict
                    del pre_dict[k]
                    #put it into queue
                    zero_indegree_que.append(k)
            
            #no zero_indegree node but still some node in pre_dict
            #there exists a cycle
            if not zero_indegree_que and pre_dict:
            	return False
            	
            while zero_indegree_que:
                predecessor = zero_indegree_que.pop()
                visited_num += 1
                
                #traverse and update pre_dict
                for k, v in pre_dict.items():
                    if predecessor in v:
                        pre_dict[k].remove(predecessor)
                        
        return True