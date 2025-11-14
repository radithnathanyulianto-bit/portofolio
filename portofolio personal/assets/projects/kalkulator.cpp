#include <iostream>
using namespace std;

int main(){
    
    float a, b, hasil;
    char di;
    
    cout << "Kalkulator sederhana" << endl;
    cout << "masukan angka: ";
    cin >> a;
    cout << "masukan operator (+ - * /): "; 
    cin >> di;
    cout << "masukan angka: ";
    cin >> b;
    
    switch(di){
        case '+':
            hasil = (a + b);
            cout << "hasil = " << hasil << endl;
            break;
        case '-':
            hasil = (a - b);
            cout << "hasil = " << hasil << endl;
            break;
        case '*':
            hasil = (a * b);
            cout << "hasil = " << hasil << endl;
            break;
        case '/':
            if (b == 0){
                cout << "error! Tidak bisa dibagi dengan nol." << endl;
            } else {
                hasil = (a / b);
                cout << "hasil = " << hasil << endl;
            }
            break;
        default:
            cout << "operator yang anda masukan salah" << endl;
            break;
    }
    
    cout << "selesai" << endl;
}
