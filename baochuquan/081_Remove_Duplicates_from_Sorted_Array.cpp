class Solution {
public:
    bool search(vector<int>& nums, int target) {
        if(nums.size() == 0)
            return false;
        int l = 0;
        int r = nums.size()-1;
        while(l <= r){
            int m = (l+r)/2;
            if(nums[m] == target)
                return true;
            if(nums[l] < nums[m]){
                if(nums[l] <= target && target < nums[m]){
                    r = m - 1;
                } else {
                    l = m + 1;
                }
            } else if(nums[l] > nums[m]){
                if(nums[m] < target && target <= nums[r]){
                    l = m + 1;
                } else {
                    r = m - 1;
                }
            } else {
                l++;
            }
        }
        return false;
    }
};
