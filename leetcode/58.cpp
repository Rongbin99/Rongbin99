class Solution {
public:
    int lengthOfLastWord(string s) { 
        int length{0}, result{0};
        for (int i{0}; i < s.size(); i++) {
            if ((s[i] == ' ') && (s[i + 1] != ' ')) {
                length = 0;
            }
            else if (s[i] != ' ') {
                length++;
                result = length;
            }
            else {
                //do nothing
            }
        }
        return result;
    }
};
