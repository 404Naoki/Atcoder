#include<bits/stdc++.h>
#define rep(i, n) for(int i = 0; i < (n); ++i)
using namespace std;
using ll = long long;

int main(void){
    string s, t;
    cin >> s >> t;
    int mn = 1001;
    rep(i, s.size() - t.size() + 1){
        int cnt = 0;
        rep(j, t.size()){
            if(s[i + j] != t[j]) ++cnt;
        }
        mn = min(mn, cnt);
    }
    cout << mn << endl;
    return 0;
}