def dfs(graph, start, goal, visited=None, path=None):
    if visited is None: visited = set()  
    if path is None: path = []  

    visited.add(start)  
    path.append(start)  

    if start == goal: return path  

    for neighbor in graph.get(start, []): 
        if neighbor not in visited:  
            result = dfs(graph, neighbor, goal, visited, path.copy())  
            if result: return result 

    return None 

# --- ইউজার ইনপুট ---

graph = {}
for _ in range(int(input("how many Nodes: "))):  
    node = input("Node name: ")
    graph[node] = input(f"Enter neighbors of {node} separated by commas: ").split(",") 

start = input("Start node: ") 
goal = input("Goal node: ")

result = dfs(graph, start, goal)  

print("DFS Path:", result if result else "Path not found") 
