#include <bits/stdc++.h>
#define rep(i, n) for(int i = 0; i < (n); ++i)
using namespace std;
using ll = long long;
using P = pair<int, int>;

int main(void){
  ll a, b, c;
  cin >> a >> b >> c;

  if((c - 1) & 1) {
    a *= a;
    b *= b;
  }

  if(a < b) {
    cout << "<" << endl;
  }
  else if(a > b) {
    cout << ">" << endl;
  }
  else {
    cout << "=" << endl;
  }

  return 0;
}