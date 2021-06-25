#include <bits/stdc++.h>
#define rep(i, n) for(int i = 0; i < (n); ++i)
using namespace std;
using ll = long long;
using P = pair<int, int>;

int main(void){
  ll n;
  cin >> n;
  ll day = 1, sum = 0;
  while(sum < n) {
    sum += day;
    day++;
  }
  cout << day - 1 << endl;
  return 0;
}