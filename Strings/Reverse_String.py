class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l_index = 0
        r_index = len(s) - 1

        while True:

            dummy = s[r_index]
            s[r_index] = s[l_index]
            s[l_index] = dummy

            l_index = l_index + 1
            r_index = r_index - 1

            if l_index >= r_index:
                break
