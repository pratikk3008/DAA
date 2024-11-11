INT_MAX = 2147483647

# A Dynamic Programming based function that calculates minimum cost of a Binary Search Tree.
def optimalSearchTree(keys, freq, n):
    # Create an auxiliary 2D matrix to store results of subproblems
    cost = [[0 for x in range(n)] for y in range(n)]
    
    # For a single key, cost is equal to frequency of the key
    for i in range(n):
        cost[i][i] = freq[i]
    
    # Now we need to consider chains of length 2, 3, ... up to n
    for L in range(2, n + 1):
        # i is the row in the cost table
        for i in range(n - L + 1):
            # j is the end of the chain in the cost table
            j = i + L - 1
            
            # Initialize with a large value
            cost[i][j] = INT_MAX
            
            # Calculate sum of frequencies from freq[i] to freq[j]
            offset_sum = calculate_sum(freq, i, j)
            
            # Try making each key in interval keys[i..j] the root
            for r in range(i, j + 1):
                # Cost when keys[r] is the root of this subtree
                c = 0
                if r > i:
                    c += cost[i][r - 1]
                if r < j:
                    c += cost[r + 1][j]
                # Add frequency sum to account for all accesses
                c += offset_sum
                
                # Update minimum cost for subtree [i...j]
                if c < cost[i][j]:
                    cost[i][j] = c
    
    # Return minimum cost for the entire tree
    return cost[0][n - 1]

def calculate_sum(freq, i, j):
    """Calculate sum of frequencies from index i to j."""
    return sum(freq[k] for k in range(i, j + 1))

# Test the function
if __name__ == '__main__':
    keys = [10, 12, 20]
    freq = [34, 8, 50]
    n = len(keys)
    print("Cost of Optimal BST is", optimalSearchTree(keys, freq, n))
