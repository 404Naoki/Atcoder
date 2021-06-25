#include<bits/stdc++.h>
#define rep(i, n) for(int i = 0; i < (n); ++i)
using namespace std;
using ll = long long;

int main(void){
    int k;
    cin >> k;
    int x = 7;
    int cnt = 1;
    while(cnt <= 1000000 + 7){
        if(x % k == 0){
            cout << cnt << endl;
            return 0;
        }
        x = (x % k) * 10 + 7;
        ++cnt;
    }
    cout << -1 << endl;
    return 0;
}