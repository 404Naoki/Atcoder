#include<bits/stdc++.h>
#define rep(i, n) for(int i = 0; i < (n); ++i)
using namespace std;
using ll = long long;

int main(void){
    int n;
    cin >> n;
    vector<int> a(n), v(1e6 + 1);
    rep(i, n) cin >> a[i];
    sort(a.begin(), a.end());
    int cnt = 0;
    rep(i, n){
        if(v[a[i]] == 0){
            if(!(i != n - 1 && a[i] == a[i + 1])) cnt++;
            for(int j = a[i]; j < 1e6 + 1; j += a[i]) v[j] = 1;
        }
    }
    cout << cnt << endl;
    return 0;
}