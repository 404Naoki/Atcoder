#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < (n); ++i)
using namespace std;
using ll = long long;
using P = pair<int, int>;

int main(void)
{
  ll a, b, c, d;
  cin >> a >> b >> c >> d;

  ll cSum = 0;
  ll cnt = 0;
  while (a > cSum * d) {
    a += b;
    cSum += c;
    cnt++;
    if(cnt > 1000000000){
      cout << -1 << endl;
      return 0;
    }
  }
  cout << cnt << endl;
  return 0;
}