#include<bits/stdc++.h>
#define rep(i, n) for(int i = 0; i < (n); ++i)
using namespace std;
using ll = long long;

int main(void){
    int n;
    cin >> n;
    for(ll i = 1; i <= n; ++i){
        int cnt = 0;
        for(ll x = 1; x * x <= i; ++x){
            ll a = x * x;
            for(ll y = 1;; ++y){
                ll b = a + y * y + x * y;
                if(b > i) break;
                for(ll z = 1;; ++z){
                    ll c = b + z * z + y * z + z * x;
                    if(c > i) break;
                    if(c == i) ++cnt;
                }
            }
        }
        cout << cnt << endl;
    }
    return 0;
}