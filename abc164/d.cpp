#include<bits/stdc++.h>
#define rep(i,n) for(int i = 0; i < (n); i++)
using namespace std;
using ll = long long;
using P = pair<int, int>;

int main(void){
    string s;
    cin >> s;
    reverse(s.begin(), s.end());
    vector<int> cnt(2019);
    int x = 1, tot = 0;
    ll ans = 0;
    rep(i, s.size()){
        cnt[tot]++;
        tot = (tot + (s[i] - '0') * x) % 2019;
        ans += cnt[tot];
        x = x * 10 % 2019;
    }
    cout << ans << endl;
    return 0;
}