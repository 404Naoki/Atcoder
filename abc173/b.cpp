#include<bits/stdc++.h>
#define rep(i, n) for(int i = 0; i < (n); ++i)
using namespace std;
using ll = long long;

int main(void){
    int n;
    cin >> n;
    vector<int> cnt(4);
    string ja[4] = {"AC", "WA", "TLE", "RE"};
    rep(i, n){
        string s;
        cin >> s;
        rep(j, 4) if(s == ja[j]) ++cnt[j];
    }
    rep(i, 4) cout << ja[i] << " x " << cnt[i] << endl;
    return 0;
}