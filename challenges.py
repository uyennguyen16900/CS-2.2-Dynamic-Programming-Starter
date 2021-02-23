class Memoize:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}

    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.fn(*args)
        return self.memo[args]


@Memoize
def lcs(strA, strB):
    if len(strA) == 0 or len(strB) == 0:
        return 0
    elif strA[-1] == strB[-1]: # if the last characters match
        return 1 + lcs(strA[:-1], strB[:-1])
    else: # if the last characters don't match
        return max(lcs(strA[:-1], strB), lcs(strA, strB[:-1]))


def lcs_dp(strA, strB):
    """Determine the length of the Longest Common Subsequence of 2 strings."""
    rows = len(strA) + 1
    cols = len(strB) + 1

    dp_table = [[0 for j in range(cols)] for i in range(rows)]

    # Fill in the table using a nested for loop.
    for r in range(1, rows):
        for c in range(1, cols):
            if strA[r-1] == strB[c-1]:
                dp_table[r][c] = 1 + dp_table[r-1][c-1]
            else:
                dp_table[r][c] = max(dp_table[r-1][c], dp_table[r][c-1])

    return dp_table[rows-1][cols-1]

def knapsack(items, capacity):
    """Return the maximum value that can be stored in the knapsack using the
    items given."""
    if len(items) == 0 or capacity == 0:
       return 0
    
    _, weight, value = items[0]
    value_with = 0
    if weight > capacity:
        return knapsack(items[1:], capacity)
    else:
        return max(value + knapsack(items[1:], capacity - weight), knapsack(items[1:], capacity))

def knapsack_dp(items, capacity):
    """Return the maximum value that can be stored in the knapsack using the
    items given."""
    rows = len(items) + 1
    cols = capacity + 1
    dp_table = [[0 for j in range(cols)] for i in range(rows)]

    # Fill in the table using a nested for loop.
    for r in range(1, rows):
        _, weight, value = items[r-1]
        for c in range(1, cols):
            if weight <= c:
                dp_table[r][c] = max(dp_table[r-1][c], dp_table[r-1][c-weight] + value)
            else:
                dp_table[r][c] = dp_table[r-1][c]            

    return dp_table[rows-1][cols-1]
    
def edit_distance(str1, str2):
    """Compute the Edit Distance between 2 strings."""
    if len(str1) == 0:
        return len(str2) 
    elif len(str2) == 0:
        return len(str1) 
    elif str1[-1] == str2[-1]:
        return edit_distance(str1[:-1], str2[:-1])
    else:
        return 1 + min(edit_distance(str1[:-1], str2[:-1]), 
                        edit_distance(str1[:-1], str2), 
                        edit_distance(str1, str2[:-1]))

def edit_distance_dp(str1, str2):
    """Compute the Edit Distance between 2 strings."""
    rows = len(str1) + 1
    cols = len(str2) + 1
    dp_table = [[0 for j in range(cols)] for i in range(rows)]

    # Fill the first row and first column with the edit distance between a substring and empty string
    for i in range(rows):
        dp_table[i][0] = i
    for j in range(cols):
        dp_table[0][j] = j

    # Fill in the table using a nested for loop.
    for r in range(1, rows):
        for c in range(1, cols):
            if str1[r-1] == str2[c-1]:
                dp_table[r][c] = dp_table[r-1][c-1]
            else:
                dp_table[r][c] = 1 + min(dp_table[r-1][c-1], dp_table[r-1][c], dp_table[r][c-1])

    return dp_table[rows-1][cols-1]
