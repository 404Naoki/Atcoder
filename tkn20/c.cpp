#include<bits/stdc++.h>
#define rep(i, n) for(int i = 0; i < (n); ++i)
using namespace std;
using ll = long long;

int main(void){
    int n, k;
    cin >> n >> k;
    vector<int> a(n);
    for(int i = 0; i < n; i++) cin >> a[i];
    rep(ki, k){
        vector<int> b(n + 1);
        rep(i, n){
            int l = max(0, i - a[i]), r = min(n, i + a[i] + 1);
            b[l]++; b[r]--;
        }
        rep(i, n) b[i + 1] += b[i];
        b.pop_back();
        if(a == b) break;
        a = b;
    }
    rep(i, n) cout << a[i] << endl;
    return 0;
}