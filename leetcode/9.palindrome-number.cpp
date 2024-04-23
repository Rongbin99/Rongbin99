/*
 * @lc app=leetcode id=9 lang=cpp
 *
 * [9] Palindrome Number
 */

// @lc code=start
class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0) {
            return false;
        }
        else {
            long long input = x;
            long long output = 0;
            while (input != 0) {
                int digit_value = input % 10;
                output = output * 10 + digit_value;
                input = input / 10;
            }
            return output == x;
        }
    }
};
// @lc code=end

