#include<bits/stdc++.h>
#define rep(i,n) for(int i = 0; i < (n); i++)
using namespace std;
using ll = long long;
using P = pair<int, int>;

int main(void){
    int n;
    cin >> n;
    set<string> str;
    rep(i, n){
        string s;
        cin >> s;
        str.insert(s);
    }
    cout << str.size() << endl;
    return 0;
}