#include<bits/stdc++.h>
#define rep(i, n) for(int i = 0; i < (n); ++i)
using namespace std;
using ll = long long;

vector<pair<long long, long long> > prime_factorize(long long N) {
    vector<pair<long long, long long> > res;
    for (long long a = 2; a * a <= N; ++a) {
        if (N % a != 0) continue;
        long long ex = 0; // 指数

        // 割れる限り割り続ける
        while (N % a == 0) {
            ++ex;
            N /= a;
        }

        // その結果を push
        res.push_back({a, ex});
    }

    // 最後に残った数について
    if (N != 1) res.push_back({N, 1});
    return res;
}

int main(void){
    ll n;
    cin >> n;
    ll cnt = 1;
    ll ans = 0;
    for(ll i = 2; i <= n; ++i){
        auto p = prime_factorize(i);
        ll y = 1;
        for(auto x : p)
            y *= x.second() + 1;
        ans += y;
    }
    cout << ans << endl;
    return 0;
}