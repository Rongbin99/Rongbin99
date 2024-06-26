/*
 * @lc app=leetcode id=13 lang=cpp
 *
 * [13] Roman to Integer
 */

// @lc code=start
class Solution {
public:
    int romanToInt(string s) {
        unordered_map<char, int> r;

        r['I'] = 1;
        r['V'] = 5;
        r['X'] = 10;
        r['L'] = 50;
        r['C'] = 100;
        r['D'] = 500;
        r['M'] = 1000;
        int output = 0;

        for (int i = 0; i < s.length(); i++) {
            if (r[s[i]] < r[s[i + 1]]) {
                output = output - r[s[i]];
            } else {
                output = output + r[s[i]];
            }
        }
        return output;
    }
};
// @lc code=end

