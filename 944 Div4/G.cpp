#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n;
    cin >> n;
    vector<int> a(n);
    map<int, priority_queue<int> > mp;

    for (int i = 0; i < n; i++) {
        cin >> a[i];
        mp[a[i] >> 2].push(-a[i]);
    }

    for (int i = 0; i < n; i++) {
        cout << -mp[a[i] >> 2].top() << " ";
        mp[a[i] >> 2].pop();
    }
    cout << endl;
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
}