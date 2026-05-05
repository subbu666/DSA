class Solution:
    def isPalindrome(self, x: int) -> bool:
        num=x
        l=len(str(num))
        reverse_num=0
        if num<0:
            return False
        else:
            while(num>0):
                last_digit=num%10
                reverse_num+=last_digit*(10**(l-1))
                l-=1
                num//=10
            return reverse_num==x