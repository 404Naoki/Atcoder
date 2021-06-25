#include<bits/stdc++.h>
#define rep(i, n) for(int i = 0; i < (n); ++i)
using namespace std;
using ll = long long;

int main(void){
    int n;
    cin >> n;
    vector<int> l(n);
    rep(i, n) cin >> l[i];
    sort(l.begin(), l.end());
    int cnt = 0;
    for(int i = 0; i < n - 2; ++i){
        for(int j = i + 1; j < n - 1; ++j){
            if(l[i] == l[j]) continue;
            for(int k = j + 1; k < n; ++k){
                if(l[j] == l[k]) continue;
                if(l[i] + l[j] > l[k]) ++cnt;
            }
        }
    }
    cout << cnt << endl;
    return 0;
}