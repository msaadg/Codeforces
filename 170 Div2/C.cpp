#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;

int main() {
    int t;
    cin >> t;
    for (int _ = 0; _ < t; ++_) {
        int n, k;
        cin >> n >> k;
        vector<int> a(n);
        for (int i = 0; i < n; ++i) {
            cin >> a[i];
        }
        map<int, int> counts;
        for (int i = 0; i < n; ++i) {
            counts[a[i]]++;
        }
        vector<int> nums;
        for (auto it = counts.begin(); it != counts.end(); ++it) {
            nums.push_back(it->first);
        }
        sort(nums.begin(), nums.end());
        int max_counts = 0;
        int left = 0;
        int total_counts = 0;
        for (int right = 0; right < nums.size(); ++right) {
            if (right > 0 && nums[right] - nums[right - 1] > 1) {
                left = right;
                total_counts = 0;
            }
            total_counts += counts[nums[right]];
            while (right - left + 1 > k) {
                total_counts -= counts[nums[left]];
                left++;
            }
            max_counts = max(max_counts, total_counts);
        }
        cout << max_counts << endl;
    }
    return 0;
}