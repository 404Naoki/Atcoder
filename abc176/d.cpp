#include<bits/stdc++.h>
#define rep(i, n) for(int i = 0; i < (n); ++i)
using namespace std;
using ll = long long;
using P = pair<int, int>;
using Pi = pair<P, int>;
#define FF first.first
#define FS first.second


int main(void){
    int h, w;
    cin >> h >> w;
    int map[h][w];
    fill(map[0], map[h], 1e6 + 1);
    int ch, cw, dh, dw;
    cin >> ch >>  cw >> dh >> dw;
    --ch; --cw; --dh; --dw;
    string s[h];
    rep(i, h) cin >> s[i];
    queue<Pi> dfs;
    dfs.push(Pi(P(ch, cw), 0));
    map[ch][cw] = 0;
    int ans = 1e6 + 1;
    while(!dfs.empty()){
        auto v = dfs.front(); dfs.pop();
        int x = v.FF, y = v.FS, c = v.second;
        if(x == dh && y == dw) ans = min(ans, c);
        for(int i = x - 2; i <= x + 2; ++i){
            if(i < 0) continue;
            if(i > h - 1) break;
            for(int j = y - 2; j <= y + 2; ++j){
                if(j < 0) continue;
                if(j > w - 1) break;
                if(s[i][j] == '#') continue;
                if(abs(i - x) + abs(j - y) >= 2){
                    if(map[i][j] > c + 1){
                        map[i][j] = c + 1;
                        dfs.push(Pi(P(i, j), c + 1));
                    }
                }
                else {
                    if(map[i][j] > c){
                        map[i][j] = c;
                        dfs.push(Pi(P(i, j), c));
                    }
                }
            }
        }
    }
    if(map[dh][dw] == 1e6 + 1) cout << -1 << endl;
    else cout << ans << endl;
    return 0;
}