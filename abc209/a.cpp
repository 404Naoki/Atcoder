#include <iostream>
#define rep(i, n) for(int i = 0; i < (n); ++i)
using namespace std;

int main(void){
  int a, b;
  cin >> a >> b;

  int ans = b - a + 1;

  cout << max(0, ans) << endl;

  return 0;
};