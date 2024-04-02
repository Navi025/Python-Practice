class Solution:
    def reverse(self, x: int) -> int:
        negative=False
        n = x
        if n<0:
            negative=True
            n=n*-1
        reversed_number = 0
        while n > 0:
            last_digit = n % 10
            reversed_number = (reversed_number * 10) + last_digit
            n = n // 10
        if negative==False:
            if reversed_number>(2**31-1):
                return 0
            return reversed_number
        reversed_number*=-1
        if reversed_number<(-2**31):
            return 0
        return reversed_number