class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers) - 2, -1, -1):
            j = i + 1
            while j < len(numbers):
                total = numbers[i] + numbers[j]
                if total == target:
                    return [i + 1, j + 1]
                j += 1
        return []