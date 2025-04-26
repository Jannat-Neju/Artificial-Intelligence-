import heapq  # priority queue ব্যবহারের জন্য

# A* Search ফাংশন
def a_star_search(graph, heuristics, start, goal):
    queue = [(heuristics[start], 0, [start])]  

    visited = set()  

    while queue:
        f, g, path = heapq.heappop(queue) 
        node = path[-1]  

        if node == goal: return path  

        if node in visited: continue  

        visited.add(node)

        for neighbor, cost in graph.get(node, []): 
            if neighbor not in visited:
                new_g = g + cost  
                new_f = new_g + heuristics[neighbor]  
                new_path = path + [neighbor]
                heapq.heappush(queue, (new_f, new_g, new_path)) 

    return None  

graph = {}
heuristics = {}

n = int(input("How many nodes: "))
for _ in range(n):
    node = input("Node Name: ")
    neighbors = input(f"{node} neighbors and cost : ").split(",")
    graph[node] = [(nb.split(":")[0], int(nb.split(":")[1])) for nb in neighbors if nb]

    heuristics[node] = int(input(f"{node} Heuristics Value: "))

start = input("Start node: ")
goal = input("Goal node: ")

result = a_star_search(graph, heuristics, start, goal)

print("A* Path:", result if result else "Path not found")

