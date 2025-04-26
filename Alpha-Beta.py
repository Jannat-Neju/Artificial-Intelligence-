# --- Alpha-Beta Pruning (সহজ ভার্সন) ---

def alpha_beta(depth, index, maximizingPlayer, values, alpha, beta):
    if depth == 0:  
        return values[index] 

    if maximizingPlayer:  
        best = float('-inf')  
        for i in range(2):  
            val = alpha_beta(depth-1, index*2+i, False, values, alpha, beta) 
            best = max(best, val)  
            alpha = max(alpha, best)  
            if beta <= alpha:  
                break
        return best  
    else:  
        best = float('inf')  
        for i in range(2):  
            val = alpha_beta(depth-1, index*2+i, True, values, alpha, beta) 
            best = min(best, val)  
            beta = min(beta, best)  
            if beta <= alpha:  
                break
        return best  


# --- ইউজার ইনপুট ---

import math  

values = list(map(int, input("Leaf node values (Give space ): ").split()))  
depth = int(math.log2(len(values)))  
alpha = int(input("Starting Alpha value (like -1000 ): "))  
beta = int(input("Starting Beta value (1000 ): "))  


best_value = alpha_beta(depth, 0, True, values, alpha, beta)


print(f"\nBest possible score (Alpha-Beta pruning): {best_value}")
