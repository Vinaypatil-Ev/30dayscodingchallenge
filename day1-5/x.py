dp = []

def F(n):
    if n == 1 or n == 2:
        dp[0] = dp[1] = 1
        return dp[1]
    if dp[n - 1] is not None:
        return dp[n - 1]
    dp[n - 1] = F(n - F(n - 1)) + F(n - F(n - 2))
    return dp[n - 1]


if __name__ == "__main__":
    n = 10
    dp = [None] * n
    # dp[0] = dp[1] = 1
    F(n)
    print(dp)