#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> P;
int main(void){
	int n;
	cin >> n;
	P f[n];
	for(int i = 0; i < n; i++){
		int a;
		cin >> a;
		f[i] = P(a, i + 1);
	}
	sort(f, f + n);
	cout << f[0].second;
	for(int i = 1; i < n; i++) cout << ' ' << f[i].second;
	cout << endl;
	return 0;
}