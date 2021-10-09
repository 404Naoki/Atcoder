#include <bits/stdc++.h>
#define rep(i, n) for(int i = 0; i < (n); ++i)
using namespace std;
using ll = long long;
using P = pair<int, int>;

int main(void){
  int n, x, y;
  cin >> n >> x >> y;
  vector<P> box;
  rep(i, n){
    int a, b;
    cin >> a >> b;
    box.push_back(P(a, b));
  }
  int dp[301][301][301];
  rep(i, 301){
    rep(j, 301){
      rep(k, 301){
        dp[i][j][k] = 301;
      }
    }
  }
  dp[0][0][0] = 0;
  int mn = 301;
  rep(i, n){
    P p = box[i];
    int a = p.first, b = p.second;
    rep(j, 301){
      rep(k, 301){
        if(dp[i][j][k] >= mn) continue;
        int to_j = j + a, to_k = k + b, af_val = dp[i][j][k] + 1;
        if(j + a >= x && k + b >= y){
          mn = min(mn, af_val);
        }
        else {
          dp[i + 1][to_j][to_k] = min(dp[i + 1][to_j][to_k], af_val);
        }
      }
    }
  }

  cout << mn << endl;

  return 0;
}