#include <bits/stdc++.h>
#define rep(i, n) for(int i = 0; i < (n); ++i)
using namespace std;
using ll = long long;
using P = pair<int, int>;

int main(void){
  ll l, q;
  cin >> l >> q;

  set<ll> a;
  a.insert(0);
  a.insert(l);
  rep(i, q) {
    ll c, x;
    cin >> c >> x;
    if(c == 1)
      a.insert(x);
    if(c == 2) {
      auto it = a.lower_bound(x);
      cout << *it - *prev(it) << endl;
    }
  }

  return 0;
}