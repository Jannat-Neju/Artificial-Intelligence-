import heapq  # Priority queue ব্যবহারের জন্য heapq ইমপোর্ট

# Best-First Search ফাংশন
def best_first_search(graph, heuristics, start, goal):
    queue = [(heuristics[start], [start])] 

    visited = set() 

    while queue:
        _, path = heapq.heappop(queue) 
        node = path[-1] 

        if node == goal: return path  

        if node in visited: continue  
        visited.add(node) 

        for neighbor in graph.get(node, []):  
            if neighbor not in visited:
                new_path = path + [neighbor] 
                heapq.heappush(queue, (heuristics[neighbor], new_path)) 

    return None # 
graph = {}
heuristics = {}

n = int(input("How many nodes: "))
for _ in range(n):
    node = input("Node Name: ")
    graph[node] = input(f"Enter neighbors of {node} separated by commas: ").split(",")
    heuristics[node] = int(input(f"{node} Heuristics Value: "))

start = input("Start node: ")
goal = input("Goal node: ")

result = best_first_search(graph, heuristics, start, goal)

print("Best-First Path:", result if result else "Path not found")

