/*
Solution 1: DP
dp[0][i] = max{dp[1][j]} + 1;
dp[1][i] = max{dp[0][j]} + 1;
*/
class Solution {
public:
    int wiggleMaxLength(vector<int>& nums) {
        long long len = nums.size();
        if(len <= 1)
            return len;
        vector<vector<int> > dp(2, vector<int>(len, 0));
        dp[0][0] = 1;
        dp[1][0] = 1;
        for(int i = 0; i < len; i++){
            long long a = LONG_MIN;
            long long b = LONG_MIN;
            for(int j = 0; j < i; j++){
                if(nums[i] > nums[j]){
                    a = dp[1][j] > a ? dp[1][j] : a;
                } else if(nums[i] < nums[j]){
                    b = dp[0][j] > b ? dp[0][j] : b;
                }
            }
            dp[0][i] = a+1;
            dp[1][i] = b+1;
        }
        return dp[0][len-1] > dp[1][len-1] ? dp[0][len-1] : dp[1][len-1];
    }
};

/*
Solution 2: Greedy
*/
class Solution {
public:
    int wiggleMaxLength(vector<int>& nums) {
        // solution 2
        int len = nums.size();
        if(len <= 1)
            return len;

        int pre = nums[0] > nums[1] ? -1 : (nums[0] < nums[1] ? 1 : 0);
        int res = pre == 0 ? 1 : 2;
        for(int i = 2; i < len; i++){
            if(nums[i] > nums[i-1]){
                if(pre == -1)
                    res++;
                pre = 1;
            } else if(nums[i] < nums[i-1]){
                if(pre == 1)
                    res++;
                pre = -1;
            }
        }
        return res;
    }
}
