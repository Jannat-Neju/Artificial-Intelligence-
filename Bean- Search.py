def beam_search(start, goal, graph, heuristic, beam_width):
    beam = [start] 
    path = {start: [start]}  

    while beam: 
        candidates = []  
        for node in beam:  
            for neighbor in graph.get(node, []):  
                if neighbor not in path:  
                    candidates.append((neighbor, heuristic.get(neighbor, float('inf'))))  
                    path[neighbor] = path[node] + [neighbor] 

        if not candidates: 
            break 

        
        candidates.sort(key=lambda x: x[1])

        
        beam = [node for node, _ in candidates[:beam_width]]

        if goal in beam: 
            return path[goal]  

    return None 

# --- ইউজার ইনপুট ---

graph = {} 
heuristic = {}  

n = int(input("How many nodes: "))  

for _ in range(n):
    node = input("\nNode name: ")  
    heuristic[node] = int(input(f"Heuristic value of {node}: ")) 
    neighbors = input(f"Neighbors of {node} (use comma ): ").split(",")  
    graph[node] = [neighbor.strip() for neighbor in neighbors]  
    
start = input("\nStart node: ") 
goal = input("Goal node: ")
beam_width = int(input("Beam width: "))  


result = beam_search(start, goal, graph, heuristic, beam_width)


if result:
    print("\nBeam Search Path:", " -> ".join(result)) 
else:
    print("\nNo solution found.") 
