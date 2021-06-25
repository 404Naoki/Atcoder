#include<bits/stdc++.h>
#define rep(i, n) for(int i = 0; i < (n); ++i)
using namespace std;
using ll = long long;

int main(void){
    int n;
    cin >> n;
    if(n % 1000 == 0) cout << 0 << endl;
    cout << 1000 - (n % 1000) << endl;
    return 0;
}