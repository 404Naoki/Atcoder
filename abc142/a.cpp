#include <iostream>
using namespace std;
int main(void){
	double n;
	cin >> n;
	double cnt = 0;
	for(int i = 1; i <= n; i += 2) cnt++;
	cout << cnt / n << endl;
	return 0;
}