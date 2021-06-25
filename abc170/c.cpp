#include<bits/stdc++.h>
#define rep(i, n) for(int i = 0; i < (n); ++i)
using namespace std;
using ll = long long;
using P = pair<int, int>;

int main(void){
    vector<bool> flg(102);
    int x, n;
    cin >> x >> n;
    rep(i, n){
        int p;
        cin >> p;
        flg[p] = true;
    }
    int ans = 102, mn = 102;
    rep(i, 102){
        if(!flg[i]){
            if(abs(x - i) < mn){
                mn = abs(x - i);
                ans = i;
            }
        }
    }
    cout << ans << endl;
    return 0;
}