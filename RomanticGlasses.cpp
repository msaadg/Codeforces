#include <iostream>
#include <vector>
#include <unordered_map>
#define ll long long int
using namespace std;

void solve() {
    int n;
    cin >> n;

    vector<ll> a(n);
    for (int i = 0; i < n; ++i)
    cin >> a[i];
    
    ll s = 0;
    unordered_map<ll, ll> mp;
    for (int i = 0; i < n; ++i) {
        s += (i % 2) ? a[i] : -a[i];
        if (mp[s] || s == 0) {
            cout << "yes" << endl;
            return;
        }
        ++mp[s];
    }
    cout << "no" << endl;
}

int main() {
    int t;
    cin >> t;

    while (t--)
    solve();
    return 0;
}