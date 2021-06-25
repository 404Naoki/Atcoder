#include<bits/stdc++.h>
#define rep(i, n) for(int i = 0; i < (n); ++i)
using namespace std;
using ll = long long;

int main(void){
    ll n;
    cin >> n;
    string ans, AL = "zabcdefghijklmnopqrstuvwxy";
    while(n > 0){
        ll al = n % 26;
        ans += AL[al];
        if(al == 0) al = 26;
        n = (n - al) / 26;
    }
    reverse(ans.begin(), ans.end());
    cout << ans << endl;
    return 0;
}