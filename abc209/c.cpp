#include <bits/stdc++.h>
#define rep(i, n) for(int i = 0; i < (n); ++i)
#define MOD 1000000007
using namespace std;
using ll = long long;
using P = pair<int, int>;

int main(void){
  int n;
  cin >> n;

  vector<int> a(n);
  rep(i, n) cin >> a[i];

  sort(a.begin(), a.end());

  ll ans = a[0];
  for(int i = 1; i < n; i++) {
    ans = (ans * (a[i] - i)) % MOD;
  }

  cout << ans << endl;

  return 0;
}