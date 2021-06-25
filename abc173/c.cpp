#include<bits/stdc++.h>
#define rep(i, n) for(int i = 0; i < (n); ++i)
using namespace std;
using ll = long long;

int main(void){
    int h, w, k;
    cin >> h >> w >> k;
    int m[h][w];
    rep(i, h){
        string s;
        cin >> s;
        rep(j, w){
            if(s[j] == '.') m[i][j] = 0;
            else m[i][j] = 1; 
        }
    }
    int sum = 0;
    vector<int> ch(h), cw(w);
    rep(i, h){
        rep(j, w){
            ch[i] += m[i][j];
            cw[j] += m[i][j];
            sum += m[i][j];
        }
    }
    ll cnt = 0;
    int hp = 1 << h, wp = 1 << w;
    rep(i, hp){
        rep(j, wp){
            int hs = 0, ws = 0;
            for(int ki = 0; 1 << ki <= i; ++ki){
                if(1 << ki & i) hs += ch[ki];
            }
            for(int ki = 0; 1 << ki <= j; ++ki){
                if(1 << ki & j) ws += cw[ki];
            }
            int hws = hs + ws;
            if(sum - hws == k) ++cnt;
        }
    }
    cout << cnt << endl;
    return 0;
}