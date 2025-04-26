from collections import deque  # queue ব্যবহারের জন্য deque ইমপোর্ট করা হয়েছে

# Bidirectional Search ফাংশন
def bidirectional_search(graph, start, goal):
    if start == goal: return [start]  

   
    front_visited = {start: [start]}
    back_visited = {goal: [goal]}  

    front_queue = deque([start])  
    back_queue = deque([goal])  

    while front_queue and back_queue:
       
        result = expand_layer(graph, front_queue, front_visited, back_visited)
        if result: return result  

        
        result = expand_layer(graph, back_queue, back_visited, front_visited, reverse=True)
        if result: return result 
        
    return None 


def expand_layer(graph, queue, visited, other_visited, reverse=False):
    node = queue.popleft()  
    neighbors = graph.get(node, [])  

    for neighbor in neighbors:
        if neighbor not in visited: 
            visited[neighbor] = visited[node] + [neighbor]
            queue.append(neighbor)  

            if neighbor in other_visited:  
                if reverse:
                    return other_visited[neighbor] + visited[neighbor][::-1][1:]  
                else:
                    return visited[neighbor] + other_visited[neighbor][::-1][1:]
    return None  

# --- ইউজার ইনপুট ---

graph = {}
for _ in range(int(input("How many nodes: "))):  
    node = input("Node Name: ")
    graph[node] = input(f"Enter neighbors of {node} separated by commas: ").split(",")

start = input("Start node: ")  
goal = input("Goal node: ")  

result = bidirectional_search(graph, start, goal)  

print("Bidirectional Path:", result if result else "Path not found")  
