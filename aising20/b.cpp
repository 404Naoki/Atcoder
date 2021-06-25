#include<bits/stdc++.h>
#define rep(i, n) for(int i = 0; i < (n); ++i)
using namespace std;
using ll = long long;

int main(void){
    int n;
    cin >> n;
    int cnt = 0, a;
    rep(i, n){
        cin >> a;
        if(a % 2 == 1 && i % 2 == 0) ++cnt;
    }
    cout << cnt << endl;
    return 0;
}