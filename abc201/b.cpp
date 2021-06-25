#include <bits/stdc++.h>
#define rep(i, n) for(int i = 0; i < (n); ++i)
using namespace std;
using ll = long long;
using P = pair<int, int>;

int main(void){
    int n;
    cin >> n;
    vector<pair<int, string>> arr(n);
    for(int i = 0; i < n; i++) {
      string s;
      int t;
      cin >> s >> t;
      arr[i] = pair<int, string>(t, s);
    }
    sort(arr.begin(), arr.end());

    cout << arr[n - 2].second << endl;

    return 0;
}