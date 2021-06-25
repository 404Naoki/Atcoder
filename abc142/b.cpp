#include<bits/stdc++.h>
using namespace std;
int main(void){
	int n, k;
	cin >> n >> k;
	int cnt = 0;
	for(int i = 0; i < n; i++){
		int h;
		cin >> h;
		if(h >= k) cnt++;
	}
	cout << cnt << endl;
	return 0;
}