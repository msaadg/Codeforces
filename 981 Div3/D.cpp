#include <bits/stdc++.h>
using namespace std;

int main() {
  int t;
  cin >> t;
  while (t--) {
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }
    
    long long s = 0;
    int ans = 0, last_cut = 0;
    unordered_map<long long, int> pos;
    pos[0] = 0;
    
    for (int i = 1; i <= n; ++i) {
      s += a[i - 1];
      if (pos.count(s) && pos[s] >= last_cut) {
        ++ans;
        last_cut = i;
        pos.clear();
        pos[s] = i;
      } else {
        pos[s] = i;
      }
    }
    cout << ans << endl;
  }
  return 0;
}
