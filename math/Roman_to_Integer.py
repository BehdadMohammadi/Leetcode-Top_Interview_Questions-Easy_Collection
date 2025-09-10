    def romanToInt(self, s: str) -> int:
        
        output = 0
        flag = 0

        for i in range(len(s)):

            if flag == 1:
                flag = 0
                continue

            if i != len(s)-1:

                if s[i] == 'I' and s[i+1] == 'V':
                    output = output + 4
                    flag = 1
                    continue

                if s[i] == 'I' and s[i+1] == 'X':
                    output = output + 9
                    flag = 1
                    continue

                if s[i] == 'X' and s[i+1] == 'L':
                    output = output + 40
                    flag = 1
                    continue

                if s[i] == 'X' and s[i+1] == 'C':
                    output = output + 90
                    flag = 1
                    continue

                if s[i] == 'C' and s[i+1] == 'D':
                    output = output + 400
                    flag = 1
                    continue

                if s[i] == 'C' and s[i+1] == 'M':
                    output = output + 900
                    flag = 1
                    continue

            if s[i] == 'I':
                output = output + 1

            if s[i] == 'V':
                output = output + 5

            if s[i] == 'X':
                output = output + 10

            if s[i] == 'L':
                output = output + 50

            if s[i] == 'C':
                output = output + 100

            if s[i] == 'D':
                output = output + 500

            if s[i] == 'M':
                output = output + 1000

        return output
