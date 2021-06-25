#include<bits/stdc++.h>
#define rep(i, n) for(int i = 0; i < (n); ++i)
using namespace std;
using ll = long long;
 
 
 
int main(void){
    int n;
    cin >> n;
    string x;
    cin >> x;
    int c = 0;
    rep(i, n) if(x[i] == '1') ++c;
    rep(i, n){
        int b = c;
        if(x[i] == '0') ++b;
        else --b;
    }
    return 0;
}