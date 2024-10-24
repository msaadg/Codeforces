#include <iostream>
#include <unordered_map>
using namespace std;

int main () {
  int t;
  cin >> t;

  while (t--) {
    int n;
    cin >> n;
    int arr[n];
    for (int i = 0; i < n; i++) {
      cin >> arr[i];
    }

    unordered_map<int, int> d;
    for (int i = 0; i < n; i++) {
      d[arr[i]] = d[arr[i]] + 1;
    }

    int m = 0;
    for (auto i : d) {
      m = max(m, i.second);
    }

    int ans = 0;
    while (m < n) {
      ans += 1;
      ans += min(n - m, m);
      m *= 2;
    }
    cout << ans << endl;
  }
  return 0;
}