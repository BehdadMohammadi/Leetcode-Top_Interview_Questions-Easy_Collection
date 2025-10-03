class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        i = 0
        j = 0
        count = 0
        flag = 0

        while i < len(haystack):

            if haystack[i] == needle[j]:

                k = i
                count = 0
                j = 0
                while j < len(needle) and k < len(haystack):

                    if haystack[k] == needle[j]:
                        count = count + 1
                    k = k + 1
                    j = j + 1


                if count == len(needle):
                    print("found")
                    print(i)
                    flag = 1
                    break
                else:
                    i = i + 1
                    j = 0
                    continue

            i = i + 1


        if flag == 1:
            return i
        else:
            return -1
