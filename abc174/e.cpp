#include<bits/stdc++.h>
#define rep(i, n) for(int i = 0; i < (n); ++i)
using namespace std;
using ll = long long;

int main(void){
    int n, k;
    cin >> n >> k;
    vector<int> a(n);
    rep(i, n) cin >> a[i];
    int l = 0, h = 1e9;
    while(h - l > 1){
        int mid = (l + h) / 2, cnt = 0;
        rep(i, n) cnt += (a[i] - 1) / mid;
        if(cnt <= k) h = mid;
        else l = mid;
    }
    cout << h << endl;
    return 0;
}