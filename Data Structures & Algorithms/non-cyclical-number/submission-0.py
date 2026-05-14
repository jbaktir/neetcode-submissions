class Solution:
    def isHappy(self, n: int) -> bool:
        visited = []
        while n not in visited:
            visited.append(n)
            total = 0
            for i in str(n):
                total += int(i) ** 2
            n = total
        return n == 1