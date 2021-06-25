#include<bits/stdc++.h>
#define rep(i, n) for(int i = 0; i < (n); ++i)
using namespace std;
using ll = long long;

int main(void){
    int n;
    cin >> n;
    string c;
    cin >> c;
    int cnt = 0, l = 0, r = n - 1;
    while(1){
        while(l < n && c[l] != 'W') ++l;
        while(r >= 0 && c[r] != 'R') --r;
        if(l < r){
            ++cnt;
            swap(c[l], c[r]);
        } 
        else break;
    }
    cout << cnt << endl;
    return 0;
}