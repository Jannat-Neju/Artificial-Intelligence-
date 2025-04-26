# Depth-Limited Search (DLS) ফাংশন, নির্দিষ্ট depth পর্যন্ত DFS চালায়
def dls(graph, node, goal, depth):
    if node == goal: return [node] 
    if depth == 0: return None  

    for neighbor in graph.get(node, []):  
        path = dls(graph, neighbor, goal, depth - 1)  
        if path: return [node] + path  

    return None 


def ids(graph, start, goal, max_depth):
    for depth in range(max_depth):  
        path = dls(graph, start, goal, depth)  
        if path: return path 
    return None 

# --- ইউজার ইনপুট ---

graph = {}
for _ in range(int(input(" how many Nodes: "))):
    node = input("Node Name : ")
    graph[node] =  input(f"Enter neighbors of {node} separated by commas: ").split(",") 

start = input("Start node: ")  
goal = input("Goal node: ") 
max_depth = int(input("Max depth: ")) 

result = ids(graph, start, goal, max_depth)

print("IDS Path:", result if result else "Path not found")
