/*
两数之和 = 不考虑进位之和 + 只考虑进位之和 = 异或 + 与
*/
class Solution {
public:
    int getSum(int a, int b) {
        if(b == 0)
            return a;
        int sum = a ^ b;
        int carry = (a & b) << 1;
        return getSum(sum, carry);
    }
};
