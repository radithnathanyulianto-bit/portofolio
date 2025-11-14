#include <iostream>
using namespace std;

int main(){
	int m;
	
	cout << "menggambar mengunakan c++\n";
	cout << "masukan pola \n" ;
	cin >> m;
		cout << endl;
		cout << endl;
	
	for(int i = 1; i <= m; i++){
		for(int k = m; k >= i; k--){
			cout << " ";
		}
		for(int j = 1; j < i; j += 1){
			if(j==1){
				cout << "♡";
			}else if(j>=1){
				cout << "♡";
				cout << "♡";
			}
		}
		cout << endl;
		//cout << endl;
		//cout << endl;
		//cout << " ";
	}
	//cout << " ";
	for(int i = 1; i <= m; i++){
		for(int k = 1; k <= i; k++){
			cout << " ";
		}
		for(int j = m; j >= i; j -= 1){
			if(j>=m){
				cout << "♡";
			}else if(j>=1){
				cout << "♡";
				cout << "♡";
			}
		}
		cout << endl;
		//cout << i;
	}
	cin.get();
}