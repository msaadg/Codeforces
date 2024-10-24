#include <bits/stdc++.h>
using namespace std;

const int dx[] = {-1, 1, 0, 0};
const int dy[] = {0, 0, -1, 1};

pair<int, int> bfs(int n, int m, vector<pair<int, int>>& lst) {
  vector<vector<int>> burnTime(n, vector<int>(m, INT_MAX));
  queue<pair<int, int>> q;

  for (auto point : lst) {
    int x = point.first - 1;
    int y = point.second - 1;
    q.push({x, y});
    burnTime[x][y] = 0;
  }

  while (!q.empty()) {
    auto [x, y] = q.front();
    q.pop();
    
    for (int i = 0; i < 4; ++i) {
      int nx = x + dx[i];
      int ny = y + dy[i];

      if (nx >= 0 && nx < n && ny >= 0 && ny < m && burnTime[nx][ny] == INT_MAX) {
        burnTime[nx][ny] = burnTime[x][y] + 1;
        q.push({nx, ny});
      }
    }
  }

  int mx = 0;
  pair<int, int> ans = {1, 1};

  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < m; ++j) {
      if (burnTime[i][j] > mx) {
        mx = burnTime[i][j];
        ans = {i + 1, j + 1}; 
      }
    }
  }

  return ans;
}

int main() {
  ifstream inFile("input.txt");
  ofstream outFile("output.txt");

  if (!inFile || !outFile) {
    cerr << "Error opening file!" << endl;
    return 1;
  }

  int n, m;
  inFile >> n >> m;
  int k;
  inFile >> k;

  vector<pair<int, int>> lst(k);
  for (int i = 0; i < k; ++i) {
    inFile >> lst[i].first >> lst[i].second;
  }

  pair<int, int> result = bfs(n, m, lst);
  outFile << result.first << " " << result.second << endl;

  return 0;
}
