#include<bits/stdc++.h>
using namespace std;
int main(void){
	long a, b;
	cin >> a >> b;
	long c = __gcd(a, b);
	long t = 0;
	for(long i = 2; i * i <= c; i++){
		if(c % i == 0){
			t++;
			while(c % i == 0) c /= i;
		}
	}
	if(c != 1) t++;
	cout << t + 1 << endl;
	return 0;
}