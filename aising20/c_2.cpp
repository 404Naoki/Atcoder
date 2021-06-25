#include<bits/stdc++.h>
#define rep(i, n) for(int i = 0; i < (n); ++i)
using namespace std;
using ll = long long;

int cal(int x, int y, int z){
    return x * x + y * y + z * z + x * y + y * z + z * x;
}

int main(void){
    int n;
    cin >> n;
    vector<int> cnt(n + 1);
    for(int x = 1; x * x <= n; ++x){
        for(int y = 1; y * y + x * x <= n; ++y){
            for(int z = 1;; ++z){
                int v = cal(x, y, z);
                if(v <= n) ++cnt[v];
                else break;
            }
        }
    }
    for(int i = 1; i <= n; ++i) cout << cnt[i] << endl;
    return 0;
}