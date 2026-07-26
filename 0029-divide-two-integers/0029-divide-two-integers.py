class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        cdd=abs(dividend)
        cdv=abs(divisor)
        if (dividend>0 and divisor<0) or (dividend<0 and divisor>0) :
            print("h1111")
            ans= floor(cdd/cdv)*(-1)
        else:
            print("h22222")
            ans= floor(cdd/cdv)
        if ans>2**(31)-1:
            return 2**(31)-1
        if ans<(2**(31)*(-1)):
            return 2**(31)*(-1)
        return ans


        