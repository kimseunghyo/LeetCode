class Solution(object):
    def allPathsSourceTarget(self, graph):
        res = []
        
        def dfs(cur_node, path):
            if cur_node == len(graph) - 1:
                res.append(path)
                
                return
            
            for node in graph[cur_node]:
                dfs(node, path + [node])
            
            
        dfs(0 ,[0])
        
        return res