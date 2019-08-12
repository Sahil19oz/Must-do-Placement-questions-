from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def addedge(self,u,v):
        self.graph[u].append(v)
    def show(self):
        print(self.graph)
    def dfs(self,v):
        visited=[0]*len(self.graph)
        stack=[]
        stack.append(v)
        #visited[v]=1
        while(len(stack)>0):
                v=stack[-1]
                if visited[v]==0:
                    print(v,end=" ")
                    visited[v]=1
                    stack=stack[:-1]
                    #print(stack)
                    
                for i in  self.graph[v]:
                    
                    if visited[i]==0:
                        stack.append(i)
                        visited[i]==1
                
                
        
g=Graph()
g.addedge(0,1)
g.addedge(0,2)
g.addedge(1,2)
g.addedge(2,0)
g.addedge(2,3)
g.addedge(3,3)
g.show()
g.dfs(0)
