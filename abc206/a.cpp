#include <bits/stdc++.h>
#define rep(i, n) for(int i = 0; i < (n); ++i)
using namespace std;
using ll = long long;
using P = pair<int, int>;

int main(void){
  double n;
  cin >> n;
  if(int(n * 1.08) > 206) {
    cout << ":(" << endl;
  } else if(int(n * 1.08) == 206) {
    cout << "so-so" << endl;
  } else {
    cout << "Yay!" << endl;
  }
  return 0;
}