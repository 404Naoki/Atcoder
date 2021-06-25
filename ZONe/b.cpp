#include <bits/stdc++.h>
#define rep(i, n) for(int i = 0; i < (n); ++i)
using namespace std;
using ll = long long;
using P = pair<int, int>;

int main(void){
  int n, D, H;
  cin >> n >> D >> H;

  double mx = 0;
  for (int i = 0; i < n; i++) {
    double d, h;
    cin >> d >> h;

    double a = (h - H) / (d - D);
    double b = h - a * d;

    mx = max(mx, b);
  }

  cout << mx << endl;

  return 0;
}