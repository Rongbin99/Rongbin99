class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int i = digits.size() - 1;
        digits[i] = digits[i] + 1;
        for (int j{0}; j < i; j++) {
            if (digits[i - j] == 10) {
                digits[i - j] = 0;
                digits[i - (j + 1)] = digits[i - (j + 1)] + 1;
            }
        }
        if (digits[0] == 10) {
            digits[0] = 0;
            digits.insert(digits.begin(), 1);
        }

        return digits;
    }
};
