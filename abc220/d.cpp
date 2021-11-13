#include <bits/stdc++.h>
#define rep(i, n) for(int i = 0; i < (n); ++i)
using namespace std;
using ll = long long;
using P = pair<int, int>;

int main(void){
  ll n;
  ll mod = 998244353;
  cin >> n;
  vector<ll> a(n);
  rep(i, n){
    cin >> a[i];
  }
  ll dp[n][10];
  fill(dp[0], dp[n], 0);
  dp[0][(a[0] + a[1]) % 10] = 1;
  dp[0][(a[0] * a[1]) % 10] = 1;
  rep(i, n - 2){
    ll x = a[2 + i];
    rep(y, 10){
      if (dp[i][y] == 0)
        continue;
      dp[i + 1][(x + y) % 10] = (dp[i + 1][(x + y) % 10] + dp[i][y]) % mod;
      dp[i + 1][(x * y) % 10] = (dp[i + 1][(x * y) % 10] + dp[i][y]) % mod;
    }
  }

  rep(i, 10){
    cout << dp[n -2][i] << endl;
  }
  return 0;
}