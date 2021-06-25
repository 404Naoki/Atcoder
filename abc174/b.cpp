#include<bits/stdc++.h>
#define rep(i, n) for(int i = 0; i < (n); ++i)
using namespace std;
using ll = long long;

int main(void){
    int n;
    double d;
    cin >> n >> d;
    int cnt = 0;
    double x, y;
    rep(i, n){
        cin >> x >> y;
        if(d >= abs(sqrt(x * x + y * y))) ++cnt;
    }
    cout << cnt << endl;
    return 0;
}