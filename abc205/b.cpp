#include <bits/stdc++.h>
#define rep(i, n) for(int i = 0; i < (n); ++i)
using namespace std;
using ll = long long;
using P = pair<int, int>;

int main(void){
  int n;
  cin >> n;

  vector<int> arr(n);
  for (int i = 0; i < n; i++){
    cin >> arr[i];
  }

  sort(arr.begin(), arr.end());

  for (int i = 1; i <= n; i++) {
    if(arr[i - 1] != i){
      cout << "No" << endl;
      return 0;
    }
  }

  cout << "Yes" << endl;
  return 0;
}