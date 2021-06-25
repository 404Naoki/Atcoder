#include<bits/stdc++.h>
#define rep(i, n) for(int i = 0; i < (n); ++i)
using namespace std;
using ll = long long;

int main(void){
    rep(i, 5){
        ll x;
        cin >> x;
        if(x == 0) cout << i + 1 << endl;
    }
    return 0;
}