#include<bits/stdc++.h>
#define rep(i, n) for(int i = 0; i < (n); ++i)
using namespace std;
using ll = long long;

int main(void){
    int n;
    cin >> n;
    int xa = 0;
    vector<int> a(n);
    rep(i, n){
        cin >> a[i];
        xa ^= a[i]; 
    }
    rep(i, n){
        int ans = xa ^ a[i];
        cout << ans << endl;
    }
    return 0;
}