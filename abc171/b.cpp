#include<bits/stdc++.h>
#define rep(i, n) for(int i = 0; i < (n); ++i)
using namespace std;
using ll = long long;

int main(void){
    int n, k;
    cin >> n >> k;
    vector<int> p(n);
    rep(i, n) cin >> p[i];
    int sum = 0;
    sort(p.begin(), p.end());
    rep(i, k) sum += p[i];
    cout << sum << endl;
    return 0;
}