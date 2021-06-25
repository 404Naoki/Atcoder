#include<bits/stdc++.h>
#define rep(i, n) for(int i = 0; i < (n); ++i)
using namespace std;
using ll = long long;

int main(void){
    int n;
    cin >> n;
    vector<int> a(n);
    rep(i, n) cin >> a[i];
    int mx = a[0];
    ll sum = 0;
    for(int i = 1; i < n; i++){
        sum += max(0, mx - a[i]);
        mx = max(mx, a[i]);
    }
    cout << sum << endl;
    return 0;
}