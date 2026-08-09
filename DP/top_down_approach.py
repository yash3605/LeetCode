# Template (Memoization)
def solve(state, memo = {}):
    if state in memo:
        return memo[state]
    if base_case(state):
        return base_value

    result = combine(solve(next_state1), solve(next_state2), ...)
    memo[state] = result

    return result

# Template (Tabulation - 1D)
def solve2():
    dp = [0] * (n + 1)
    dp[0] = base_value

    for i in range(1, n + 1):
        dp[i] = combine(dp[i - 1], dp[i - 2], ...)
    return dp[n]

# Template (Tabulation - 2D)
def solve3():
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if match_condition(i, j):
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[n][m]
