/*
 * @lc app=leetcode id=47 lang=cpp
 *
 * [47] Permutations II
 */

// @lc code=start
class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        if (nums.size() == 2) {
            if (nums[0] == nums[1]) {
                return {{nums[0], nums[1]}};
            } else {
                return {{nums[0], nums[1]}, {nums[1], nums[0]}};
            }
        }
        if (nums.size() == 1) {
            return {{nums[0]}};
        }
        bool duplicate = true;
        for (int d = 0; d < nums.size(); d++) {
            if (nums[0] != nums[d]) {
                duplicate = false;
            }
        }
        if (duplicate) {
            return {{nums}};
        }
        else {
            vector<vector<int>> output;
            for (int i = 0; i < nums.size(); i++) {
                vector<int> nums_copy = nums;
                nums_copy.erase(nums_copy.begin() + i);
                vector<vector<int>> temp = permuteUnique(nums_copy);
                for (int j = 0; j < temp.size(); j++) {
                    temp[j].insert(temp[j].begin(), nums[i]);
                    output.push_back(temp[j]);
                }
            }
            for (int x = 0; x < output.size(); x++) {
                for (int y = 0; y < output.size(); y++) {
                    if ((output[x] == output[y]) && (x != y)) {
                        output.erase(output.begin() + y);
                    }
                }
            }
            return output;
        }
    }
};
// @lc code=end

