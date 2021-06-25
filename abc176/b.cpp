#include<bits/stdc++.h>
#define rep(i, n) for(int i = 0; i < (n); ++i)
using namespace std;
using ll = long long;

int main(void){
    string n;
    cin >> n;
    int sum = 0;
    rep(i, n.size())
        sum = (sum + n[i] - '0') % 9;
    if(sum == 0) cout << "Yes" << endl;
    else cout << "No" << endl;
    return 0;
}