#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < (n); ++i)
using namespace std;
using ll = long long;
using P = pair<int, int>;
vector<short> cnt(1000000001, 0);

int main(void)
{
  int n;
  cin >> n;

  vector<int> a(n);
  rep(i, n) cin >> a[i];
  reverse(a.begin(), a.end());

  ll sum = 0;
  cnt[a[0]]++;
  for (int i = 1; i < n; i++)
  {
    sum += i - cnt[a[i]];
    cnt[a[i]]++;
  }

  cout << sum << endl;

  return 0;
}