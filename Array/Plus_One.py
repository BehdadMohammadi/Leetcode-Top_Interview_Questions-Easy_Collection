class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        digits.reverse()

        carry_on = 0
        
        if len(digits) == 1 and digits[0] == 9:
            return [1,0]

        for i in range(len(digits)):

            if i == len(digits)-1:
                if digits[i] + carry_on == 10:
                    digits[i] = 0
                    digits.append(1)
                    continue



            if i == 0:
                if digits[i] + 1 == 10:
                    digits[i] = 0
                    carry_on = 1
                    continue
                else:
                    digits[i] = digits[i] + 1
                    continue


            if digits[i] + carry_on == 10:
                digits[i] = 0
                carry_on = 1
            else:
                digits[i] = digits[i] + carry_on
                carry_on = 0


        digits.reverse()
        
        return digits





        
