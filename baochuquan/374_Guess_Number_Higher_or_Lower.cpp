/*
 * 思路：二分法
 *
 */

// Forward declaration of guess API.
// @param num, your guess
// @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
int guess(int num);

class Solution {
public:
    int guessNumber(int n) {
        long long start = 1;
        long long end = n;
        long long middle = (1+n)/2;
        while(guess(middle) != 0){
            if(guess(middle) == -1){
                end = middle-1;
            } else {
                start = middle+1;
            }
            middle = (start+end)/2;
        }
        return middle;
    }
};
