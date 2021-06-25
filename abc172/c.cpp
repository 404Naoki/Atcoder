#include<bits/stdc++.h>
#define rep(i, n) for(int i = 0; i < (n); ++i)
using namespace std;
using ll = long long;

int main(void){
    int n, m, k;
    cin >> n >> m >> k;
    vector<ll> a(n), b(m);
    rep(i, n) cin >> a[i];
    rep(i, m) cin >> b[i];
    a.insert(a.begin(), 0); b.insert(b.begin(), 0);
    rep(i, n) a[i + 1] += a[i];
    rep(i, m) b[i + 1] += b[i];
    ll ans = 0;
    ll bp = m;
    rep(i, n + 1){
        if(a[i] > k) continue;
        while(a[i] + b[bp] > k) bp--;
        ans = max(ans, i + bp);
    }
    cout << ans << endl;
}