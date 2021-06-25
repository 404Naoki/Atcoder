#include<bits/stdc++.h>
using namespace std;
int main(void){
    int a, b, c, d;
    cin >> a >> b >> c >> d;
    while(a > 0){
        c -= b;
        if(c <= 0) break;
        a -= d;
    }
    if(a > 0) cout << "Yes" << endl;
    else cout << "No" << endl;
    return 0;
}