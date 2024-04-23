/*
 * @lc app=leetcode id=709 lang=cpp
 *
 * [709] To Lower Case
 */

// @lc code=start
class Solution {
public:
    string toLowerCase(string s) {
        string final = s;
        transform(s.begin(), s.end(), final.begin(), ::tolower);
        return final;
    }
};
// @lc code=end

