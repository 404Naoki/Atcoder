#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < (n); ++i)
using namespace std;
using ll = long long;
using P = pair<int, int>;

string Z = "ZONe";

int main(void)
{
  string s;
  cin >> s;
  int cnt = 0;

  for (int i = 0; i < s.size(); i++)
  {
    string t = s.substr(i, 4);
    if (t == Z)
      cnt++;
  }

  cout << cnt << endl;
  return 0;
}