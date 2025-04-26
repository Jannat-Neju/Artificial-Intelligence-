# AO* Algorithm (User Input সহ)
# AO* Algorithm (User Input সহ)

def ao_star(node):  
    print(f"\nNode এক্সপান্ড করা হচ্ছে: {node}")  

    if not graph[node]:  
        return 0  

    min_cost = float('inf')  
    best_children = [] 
    for children, cost in graph[node]:  
        total_cost = cost  
        for child in children:  
            total_cost += heuristics.get(child, 0) 

        if total_cost < min_cost:  
            min_cost = total_cost  
            best_children = children  

    heuristics[node] = min_cost  
    solution_path[node] = best_children  

    for child in best_children: 
        ao_star(child)  

    return heuristics[node] 

def print_solution(node, indent=""):  
    print(indent + node) 
    if node in solution_path: 
        for child in solution_path[node]:  
            print_solution(child, indent + "  ") 


# ----- ইউজার ইনপুট -----
graph = {}  
heuristics = {} 
solution_path = {} 

n = int(input("how many nodes: "))  

for _ in range(n):  
    node = input("Node Name: ")  
    heuristics[node] = int(input(f"{node}  heuristic Value : ")) 

    choices = [] 
    m = int(input(f"{node} Child Group (AND/OR group) : "))  
    for _ in range(m):  
        group_input = input(f"Child nodes and  cost (format: A,B:3): ")  
        parts = group_input.split(":") 
        children = parts[0].split(",")  
        cost = int(parts[1])  # ":" 
        choices.append((children, cost))  

    graph[node] = choices  

start_node = input("Start node name: ")  

ao_star(start_node) 

print("\nAO* solution path:")  
print_solution(start_node)  
