def rob(nums):
    memo = {}

    def solve(i):
        if i >= len(nums):
            return 0

        if i in memo:
            return memo[i]

        # Choice 1: Rob current house
        take = nums[i] + solve(i + 2)

        # Choice 2: Skip current house
        skip = solve(i + 1)

        memo[i] = max(take, skip)

        return memo[i]

    return solve(0)


nums = list(map(int, input().split()))

print(rob(nums))