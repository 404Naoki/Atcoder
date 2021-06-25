#include<bits/stdc++.h>
#define rep(i, n) for(int i = 0; i < (n); ++i)
using namespace std;
using ll = long long;

int main(void){
    int x, y;
    cin >> x >> y;
    rep(i, x + 1){
        int k = x - i;
        if(i * 2 + k * 4 == y){
            cout << "Yes" << endl;
            return 0;
        }
    }
    cout << "No" << endl;
    return 0;
}