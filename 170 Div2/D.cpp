#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    vector<int> r(n);
    for (int i = 0; i < n; ++i) {
        cin >> r[i];
    }

    vector<int> attr_positions;
    for (int i = 0; i < n; ++i) {
        if (r[i] == 0) {
            attr_positions.push_back(i);
        }
    }
    attr_positions.push_back(n);

    vector<vector<int>> s_pass_counts(m), i_pass_counts(m);
    for (int idx = 0; idx < m; ++idx) {
        int start = attr_positions[idx];
        int end = attr_positions[idx + 1];
        vector<int> s_req_counts(m + 1, 0), i_req_counts(m + 1, 0);
        for (int j = start; j < end; ++j) {
            if (r[j] < 0) {
                int req = -r[j];
                s_req_counts[req]++;
            } else if (r[j] > 0) {
                int req = r[j];
                i_req_counts[req]++;
            }
        }
        vector<int> s_cumulative(m + 1, 0), i_cumulative(m + 1, 0);
        for (int l = 1; l <= m; ++l) {
            s_cumulative[l] = s_cumulative[l - 1] + s_req_counts[l];
            i_cumulative[l] = i_cumulative[l - 1] + i_req_counts[l];
        }
        s_pass_counts[idx] = s_cumulative;
        i_pass_counts[idx] = i_cumulative;
    }

    vector<vector<int>> dp(m + 1, vector<int>(m + 1, -1));
    dp[0][0] = 0;
    for (int i = 1; i <= m; ++i) {
        for (int s = 0; s <= i; ++s) {
            int s_level = s;
            int i_level = i - s;
            int s_count = s_pass_counts[i - 1][s_level];
            int i_count = i_pass_counts[i - 1][i_level];

            if (s > 0 && dp[i - 1][s - 1] != -1) {
                dp[i][s] = max(dp[i][s], dp[i - 1][s - 1] + s_count + i_count);
            }

            if (s <= i - 1 && dp[i - 1][s] != -1) {
                dp[i][s] = max(dp[i][s], dp[i - 1][s] + s_count + i_count);
            }
        }
    }

    int result = -1;
    for (int s = 0; s <= m; ++s) {
        result = max(result, dp[m][s]);
    }
    cout << result << endl;

    return 0;
}
