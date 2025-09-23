class Solution:
    def reverse(self, x: int) -> int:
        
        if x < 0:
            IsNagative = True
        else:
            IsNagative = False

        x_list = list(str(abs(x)))

        l_index = 0
        r_index = len(x_list) - 1

        while l_index < r_index:

            dummy = x_list[r_index]
            x_list[r_index] = x_list[l_index]
            x_list[l_index] = dummy

            l_index = l_index + 1
            r_index = r_index - 1


        separator = ""
        my_string = separator.join(x_list)




        if IsNagative == False and int(my_string) > (2**31 - 1):
            return 0

        if IsNagative == True and int(my_string) > 2**31:
            return 0


        if IsNagative == True:
            return -int(my_string)
        else:
            return int(my_string)

        
