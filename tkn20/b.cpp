#include<bits/stdc++.h>
using namespace std;
using ll = long long;
 
int main(void){
    ll a, v, b, w, t;
    cin >> a >> v >> b >> w >> t;
    ll sa = abs(a - b), ssa = v - w;
    if(sa - t * ssa <= 0) cout << "YES" << endl;
    else cout << "NO" << endl;  
    return 0;
}