#include<bits/stdc++.h>
#define rep(i, n) for(int i = 0; i < (n); ++i)
using namespace std;
using ll = long long;

int main(void){
    int n;
    cin >> n;
    vector<int> cnt(1e5 + 1);
    ll sum = 0;
    rep(i, n){
        int a;
        cin >> a;
        sum += a;
        ++cnt[a];
    }
    int q;
    cin >> q;
    rep(i, q){
        int b, c;
        cin >> b >> c;
        sum += (cnt[b] * (c - b));
        cout << sum << endl;
        cnt[c] += cnt[b];
        cnt[b] = 0;
    }
    return 0;
}