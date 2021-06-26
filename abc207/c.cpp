#include <bits/stdc++.h>
#define rep(i, n) for(int i = 0; i < (n); ++i)
using namespace std;
using ll = long long;
using P = pair<double, double>;

int main(void){
  int n;
  cin >> n;
  vector<P> d;
  rep(i, n) {
    int t, l, r;
    cin >> t >> l >> r;
    if(t == 1)
      d.push_back(P(l, r));
    if(t == 2)
      d.push_back(P(l, r - 0.1));
    if(t == 3)
      d.push_back(P(l + 0.1, r));
    if(t == 4)
      d.push_back(P(l + 0.1, r - 0.1));
  }
  int cnt = 0;
  for(int i = 0; i < n - 1; i++) {
    for(int j = i + 1; j < n; j++) {
      double li = d[i].first, ri = d[i].second,
          lj = d[j].first, rj = d[j].second;
      if(li <= lj && rj <= ri) cnt++;
      else if(lj <= li && ri <= rj) cnt++;
      else if(li <= lj && lj <= ri && ri <= rj) cnt++;
      else if(lj <= li && li <= rj && rj <= ri) cnt++;
    }
  }
  cout << cnt << endl;
  return 0;
}