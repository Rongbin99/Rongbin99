/*
 * @lc app=leetcode id=15 lang=cpp
 *
 * [15] 3Sum
 */

// @lc code=start
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> output;
        set<vector<int>> temp;
        int size = nums.size();
        sort(nums.begin(), nums.end());

        for (int i = 0; i < size-2; i++)  {
            for (int j = i+1; j < size-1; j++)  {
                for (int k = j+1; k < size; k++)  {

                    if (((nums[i] + nums[j] + nums[k]) == 0) && i != j && j!= k && k != i) {
                        temp.insert({nums[i], nums[j], nums[k]});
                    }
                }
            }
        }

        for (auto it : temp) {
            output.push_back(it);
        }

        return output;
    }
};
// @lc code=end

