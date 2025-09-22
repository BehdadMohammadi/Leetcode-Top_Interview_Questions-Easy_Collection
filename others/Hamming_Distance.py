class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        
        result = x ^ y

        result_bin = bin(result)

        return result_bin.count("1")
        
