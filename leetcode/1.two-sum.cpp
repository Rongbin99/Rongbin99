/*
 * @lc app=leetcode id=1 lang=cpp
 *
 * [1] Two Sum
 */

// @lc code=start
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int num1;
        int num2;

        for (int i = 0; i < nums.size(); i++) {
            for (int j = 0; j < nums.size(); j++) {
                if (i == j) {
                    continue;
                } else {
                    if (nums[i] + nums[j] == target) {
                        num1 = j;
                        num2 = i;
                    }
                }
            }
        }
        return {num1, num2};
    }
};
// @lc code=end

