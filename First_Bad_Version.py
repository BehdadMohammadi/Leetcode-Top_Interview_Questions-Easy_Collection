class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        list_n = list(range(1, n+1))
        j = 0
        
        if isBadVersion(1) == True:
            return 1


        while True:

            if len(list_n)%2 == 0:
                index = len(list_n)//2 - 1
            else:
                index = len(list_n)//2

            if index == 0 and len(list_n) == 2:
                j = 1

            if len(list_n) == 2:
                if isBadVersion(list_n[0]) == True:
                    return list_n[0]
                    break
                else:
                    return list_n[1]
                    break




            if isBadVersion(list_n[index]) == False:
                list_n = list_n[index+1:]

            elif isBadVersion(list_n[index]) == True:
                list_n = list_n[0:index+1+j]
                j = 0


            if len(list_n) == 1:
                break

        return list_n[0]
