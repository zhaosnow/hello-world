/*
 solution 1: DP
 dp[i][j] = min(dp[i][j], x + max(dp[i][x-1], dp[x+1][j]));
*/
class Solution {
public:
    int min(int a, int b){
        return a < b ? a : b;
    }
    int max(int a, int b){
        return a > b ? a : b;
    }
    int getMoneyAmount(int n) {
        // solution 1
        int res = 0;
        vector<vector<int> > dp(n+1, vector<int>(n+1, 0));
        for(int i = n-1; i > 0; i--){
            for(int j = i+1; j <= n; j++){
                int ans = INT_MAX;
                for(int x = i; x < j; x++){
                    ans = min(ans, x+max(dp[i][x-1], dp[x+1][j]));
                }
                dp[i][j] = ans;
            }
        }

        return dp[1][n];
    }
};
