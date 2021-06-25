#include<bits/stdc++.h>
using namespace std;
using ll = long;
const ll M = 1000000000000000000;
int main(void){
    ll n;
    cin >> n;
    vector<ll> a(n);
    int zf = 0;
    for(int i = 0; i < n; i++){
        cin >> a[i];
        if(a[i] == 0) zf = 1;
    }
    if(zf) cout << 0 << endl;
    else {
        ll ans = 1, at = 0;
        for(int i = 0; i < n; i++){
            at = ans;
            ans *= a[i];
            if(ans * a[i] > M || ans < at){
                ans = -1;
                break;
            }
        }
        cout << ans << endl;
    }
    return 0;
}