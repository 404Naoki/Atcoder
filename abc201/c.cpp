#include <bits/stdc++.h>
#define rep(i, n) for(int i = 0; i < (n); ++i)
using namespace std;
using ll = long long;
using P = pair<int, int>;

int main(void){
  string s;
  cin >> s;

  int dp[4][1024];
  fill(dp[0], dp[4], 0);

  int check = 0;
  rep(i, 10) {
    if(s[i] == 'x') continue;
    int to = 1 << i;
    if(s[i] == 'o') check += to;
    dp[0][to] = 1;
  }

  rep(i, 3) {
    rep(j, 1024) {
      if(dp[i][j] == 0) continue;
      rep(k, 10) {
        if(s[k] == 'x') continue;
        int to = j | (1 << k);
        dp[i + 1][to] += dp[i][j];
      }
    }
  }

  int ans = 0;
  rep(j, 1024) {
    if((j & check) == check) ans += dp[3][j];
  }

  cout << ans << endl;

  return 0;
}