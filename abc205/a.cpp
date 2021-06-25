#include <bits/stdc++.h>
#define rep(i, n) for(int i = 0; i < (n); ++i)
using namespace std;
using ll = long long;
using P = pair<int, int>;

int main(void){
  double a, b;
  cin >> a >> b;

  b /= 100;

  cout << a * b << endl;
  return 0;
}