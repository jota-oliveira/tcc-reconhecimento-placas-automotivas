#include <iostream>
using namespace std;
int main() {
	double numero1, numero2, media;
	std::cout << "Digite o primeiro número: ";
	std::cin >> numero1;
	std::cout << "Digite o segundo número: ";
	std::cin >> numero2;
	media = (numero1 + numero2) / 2.0;
	std::cout << "A média é " << media << endl;	 
	return 0;
}
