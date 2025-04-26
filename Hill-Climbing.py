def hill_climbing(start, goal, graph, heuristic):
    current = start  
    path = [current]

    while current != goal:
        neighbors = graph.get(current, [])
        if not neighbors:  
            break  

        
        next_node = min(neighbors, key=lambda neighbor: heuristic.get(neighbor, float('inf')))

        if heuristic[next_node] >= heuristic[current]:  
            break  

        current = next_node  
        path.append(current)  

    if current == goal:  
        return path  
    else:
        return None  

# --- ইউজার ইনপুট ---

graph = {}  
heuristic = {}

n = int(input("How many nodes: "))  

for _ in range(n):
    node = input("\nNode name: ") 
    heuristic[node] = int(input(f"Heuristic value of {node}: "))  
    neighbors = input(f"Neighbors of {node} (Give comma): ").split(",")  
    graph[node] = [neighbor.strip() for neighbor in neighbors]

start = input("\nStart node: ")
goal = input("Goal node: ")  


result = hill_climbing(start, goal, graph, heuristic)


if result:
    print("\nHill Climbing Path:", " -> ".join(result))  
else:
    print("\nNo solution found (stuck at local maximum or no better neighbor).")  
