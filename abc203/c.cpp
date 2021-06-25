#include <bits/stdc++.h>
#define rep(i, n) for(int i = 0; i < (n); ++i)
using namespace std;
using ll = long long;
using P = pair<ll, ll>;

int main(void){
  ll n, k;
  cin >> n >> k;

  vector<P> d;

  ll a, b;
  for(int i = 0; i < n; i++) {
    cin >> a >> b;
    d.push_back(P(a, b));
  }

  sort(d.begin(), d.end());

  ll ans = 0;
  ll now = 0;
  for(int i = 0; i < n; i++) {
    P p = d[i];

    if(p.first - now > k){
      now += k;
      cout << now << endl;
      return 0;
    }
    k -= p.first - now;
    now = p.first;
    k += p.second;
  }

  cout << now + k << endl;

  return 0;
}