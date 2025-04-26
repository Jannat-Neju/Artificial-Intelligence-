# Heuristic Search Algorithm (User Input সহ)

# --- Heuristic Search ফাংশন ---
def heuristic_search(graph, heuristic, start, goal):
    visited = set() 
    queue = [(start, heuristic[start])]  

    while queue: 
       
        queue.sort(key=lambda x: x[1]) 
        current, _ = queue.pop(0)

        if current == goal:  
            return f"Reached the goal: {goal}"

        visited.add(current)

       
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                queue.append((neighbor, heuristic[neighbor])) 

    return "Goal not found."  


# --- ইউজার ইনপুট নিচ্ছি ---

graph = {}  
heuristic = {} 
n = int(input("How many nodes : "))  

for _ in range(n):
    node = input("Node name: ") 
    heuristic[node] = int(input(f"{node} heuristic value: "))
    neighbors = input(f"{node} neighbors (give comas) : ").split(",")  
    graph[node] = neighbors
start = input("Start Node: ")
goal = input("Goal Node: ")  


result = heuristic_search(graph, heuristic, start, goal)


print(result)
