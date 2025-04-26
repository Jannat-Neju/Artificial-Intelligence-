# Depth-Limited Search (DLS) ফাংশন
def dls(graph, node, goal, depth, path=None):
    if path is None: path = [node]  

    if node == goal: return path 

    if depth == 0: return None  

    for neighbor in graph.get(node, []): 
        if neighbor not in path: 
            result = dls(graph, neighbor, goal, depth - 1, path + [neighbor]) 
            if result: return result 

    return None  

# --- ইউজার ইনপুট ---

graph = {}
for _ in range(int(input("How many nodes: "))): 
    node = input("Node Name: ")
    graph[node] =input(f"Enter neighbors of {node} separated by commas: ").split(",")

start = input("Start node: ")  
goal = input("Goal node: ")  
depth = int(input("Maximum depth : "))

result = dls(graph, start, goal, depth)

print("DLS Path:", result if result else "Path not found")