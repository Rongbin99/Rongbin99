/*
 * @lc app=leetcode id=46 lang=cpp
 *
 * [46] Permutations
 */

// @lc code=start
class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        if (nums.size() == 2) {
            return {{nums[0], nums[1]}, {nums[1], nums[0]}};
        }
        if (nums.size() == 1) {
            return {{nums[0]}};
        }
        else {
            vector<vector<int>> output;
            for (int i = 0; i < nums.size(); i++) {
                vector<int> nums_copy = nums;
                nums_copy.erase(nums_copy.begin() + i);
                vector<vector<int>> temp = permute(nums_copy);
                for (int j = 0; j < temp.size(); j++) {
                    temp[j].insert(temp[j].begin(), nums[i]);
                    output.push_back(temp[j]);
                }
            }
            return output;
        }
    }
};
// @lc code=end

