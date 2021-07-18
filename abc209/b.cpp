#include <iostream>
#define rep(i, n) for(int i = 0; i < (n); ++i)
using namespace std;

int main(void){
  int n, x;
  cin >> n >> x;

  int a, sum = 0;
  rep(i, n) {
    cin >> a;
    sum += a;
  }

  sum -= (n / 2);

  if(x >= sum) {
    cout << "Yes" << endl;
  } else {
    cout << "No" << endl;
  }

  return 0;
};