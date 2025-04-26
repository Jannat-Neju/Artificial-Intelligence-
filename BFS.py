from collections import deque 

def bfs(graph, start, goal):
    visited = set() 
    queue = deque([[start]])  

    while queue: 
        path = queue.popleft()  
        node = path[-1]  

        if node == goal: return path  

        if node not in visited: 
            visited.add(node) 
            for neighbor in graph.get(node, []):  
                queue.append(path + [neighbor])  

    return None  

# --- ইউজার ইনপুট ---

graph = {}
for _ in range(int(input(" how many Nodes : "))): 
    node = input("Node name: ")
    graph[node] = input(f"Enter neighbors of {node} separated by commas: ").split(",") 
start = input("Start node: ") 
goal = input("Goal node: ") 

result = bfs(graph, start, goal)  

print("BFS Path:", result if result else "Path not found")  
