#include<bits/stdc++.h>
#define rep(i, n) for(int i = 0; i < (n); ++i)
using namespace std;
using ll = long long;

int main(void){
    int n;
    cin >> n;
    string c;
    cin >> c;
    string ans = c;
    sort(ans.begin(), ans.end());
    int cnt = 0;
    rep(i, n) if(c[i] != ans[i]) ++cnt;
    cout << cnt / 2 << endl;
    return 0;
}