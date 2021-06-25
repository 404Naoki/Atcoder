#include<bits/stdc++.h>
using namespace std;
using ll = long long;
const ll M = 1000000000000000000;
int main(void){
    ll n;
    cin >> n;
    vector<ll> a(n);
    int zf = 0;
    for(int i = 0; i < n; i++) cin >> a[i];
    sort(a.begin(), a.end());
    ll ans = 1;
    for(int i = 0; i < n; i++){
        ans *= a[i];
        if(ans > 1e18){
            ans = -1;
            break;
        }
    }
    cout << ans << endl;
    return 0;
}