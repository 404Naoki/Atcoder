#include<bits/stdc++.h>
#define rep(i, n) for(int i = 0; i < (n); ++i)
using namespace std;
using ll = long long;

int main(void){
    ll x, k, d;
    cin >> x >> k >> d;
    if(x < 0) x *= -1;
    ll xpd = (x + d - 1) / d;
    if(xpd <= k){
        ll xd = x - xpd * d, kd = k - xpd;
        if(kd & 1) cout << abs(xd + d) << endl;
        else cout << abs(xd) << endl;
    }
    else cout << abs(x - k * d) << endl;
    return 0;
}