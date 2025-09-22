class Solution:
    def isValid(self, s: str) -> bool:

        s_list = list(s)
        
        if len(s_list)%2 != 0:
            return False

        flag = 0


        while True:

            opened_cahr = s_list[0]
            index = 1

            while True:



                if s_list[index] == '(':
                    index = index + 1
                    opened_cahr = '('

                elif s_list[index] == '[':
                    index = index + 1
                    opened_cahr = '['

                elif s_list[index] == '{':
                    index = index + 1
                    opened_cahr = '{'

                if index + 1 > len(s_list):
                    return False

                if s_list[index] == ')':
                    if opened_cahr == '(':
                        s_list.pop(index)
                        s_list.pop(index - 1)
                        break
                    else:
                        flag = 1
                        break

                elif s_list[index] == ']':
                    if opened_cahr == '[':
                        s_list.pop(index)
                        s_list.pop(index - 1)
                        break
                    else:
                        flag = 1
                        break

                elif s_list[index] == '}':
                    if opened_cahr == '{':
                        s_list.pop(index)
                        s_list.pop(index - 1)
                        break
                    else:
                        flag = 1
                        break



            if flag == 1:
                break

            if len(s_list) == 0:
                break

        if flag == 0:
            return True
        if flag == 1:
            return False
        
