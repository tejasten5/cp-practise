class ReverseNumber:
    def reverse_number(self, value):
        i = 0
        rev = 0
        while(value != 0):
            tmp = value % 10
            rev = tmp + (rev * 10)
            value = value // 10
        return rev

num = 123
print(ReverseNumber().reverse_number(num))