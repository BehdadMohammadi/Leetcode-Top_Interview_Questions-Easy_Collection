class Solution:
    def firstUniqChar(self, s: str) -> int:
        

        my_dict = {}
        flag = 0

        for letter in s:

            if letter in my_dict:
                my_dict[letter] = my_dict[letter] + 1
            else:
                my_dict[letter] = 1


        for key, value in my_dict.items():
            if value == 1:
                # print(key)
                flag = 1
                break
        if flag == 0:
            return -1

        i = 0
        while True:
            if s[i] == key:
                return i
                break

            i = i + 1
        
