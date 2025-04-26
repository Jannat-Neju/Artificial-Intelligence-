# Minimax Algorithm (User Input সহ)


def minimax(depth, node, is_maximizing_player):
    if depth == 0 or game_over(node):  
        return evaluate(node) 

    if is_maximizing_player:
        max_eval = float('-inf')  
        for child in generate_children(node):
            eval = minimax(depth-1, child, False) 
            max_eval = max(max_eval, eval) 
        return max_eval  
    else: 
        min_eval = float('inf') 
        for child in generate_children(node):  
            eval = minimax(depth-1, child, True)  
            min_eval = min(min_eval, eval) 
        return min_eval  



# ----- ইউজার ইনপুট -----

def game_over(node):
    
    
    return node == 'WIN' or node == 'DRAW'


def evaluate(node):
    if node == 'WIN':
        return 1  
    elif node == 'DRAW':
        return 0  
    return -1  


def generate_children(node):
    return ['WIN', 'DRAW', 'LOSE']  

# ----- ইউজার ইনপুট -----
start_node = input("( WIN, DRAW, LOSE): ")  
depth = int(input(" (depth) : ")) 

best_move = minimax(depth, start_node, True)


print(f"The maximum score or decision of the game: {best_move}")
