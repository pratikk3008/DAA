def knapSack(W, wt, val, n):
    # Base Case
    if n == 0 or W == 0:
        return 0

    # If weight of the nth item is more than Knapsack of capacity W, 
    # then this item cannot be included in the optimal solution
    if (wt[n-1] > W):
        return knapSack(W, wt, val, n-1)

    # return the maximum of two cases: (1) nth item included (2) not included
    else:
        return max(val[n-1] + 
                   knapSack(W-wt[n-1], wt, val, n-1), 
                    knapSack(W, wt, val, n-1))
# end of function knapSack

# Driver Code
if __name__ == '__main__':
    profit = [60, 100, 120]
    weight = [10, 20, 30]
    W = 50
    n = len(profit)
    print ("The maximum Profit gained is : ",knapSack(W, weight, profit, n))
    
#o(n W) Time Complexity


#def knapsack(weights, values, capacity):
#    n = len(values)
#    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
#
#    # Build table dp[][] in a bottom-up manner
#    for i in range(1, n + 1):
#        for w in range(capacity + 1):
#            if weights[i - 1] <= w:
#                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
#            else:
#                dp[i][w] = dp[i - 1][w]
#
#    return dp[n][capacity]

# Example usage
#weights = [2, 3, 4, 5]
#values = [3, 4, 5, 6]
#capacity = 5
#max_value = knapsack(weights, values, capacity)
#print("Maximum value in knapsack:", max_value)
