#include<bits/stdc++.h>
#define rep(i, n) for(int i = 0; i < (n); ++i)
using namespace std;
using ll = long long;

int main(void){
    string s;
    cin >> s;
    int cnt = 0, mx = 0;
    s += 'S';
    rep(i, 4){
        if(s[i] == 'R') cnt++;
        else {
            mx = max(mx, cnt);
            cnt = 0;
        }
    }
    cout << mx << endl;
    return 0;
}