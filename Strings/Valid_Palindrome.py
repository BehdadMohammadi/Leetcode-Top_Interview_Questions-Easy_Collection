class Solution:
    def isPalindrome(self, s: str) -> bool:

        forward_list = []
        backward_list = []

        for letter in s:

            if ord(letter) >= 97 and  ord(letter) <= 122:
                forward_list.append(letter)
            elif ord(letter) >= 65 and  ord(letter) <= 90:
                forward_list.append(chr(ord(letter)+32))
            elif ord(letter) >= 48 and  ord(letter) <= 57:
                forward_list.append(letter)


        backward_list = forward_list.copy()
        forward_list.reverse()

        if backward_list == forward_list:
            return True
        else:
            return False

        
