#include <iostream>
using namespace std;

int main()
{
	long n;
	cout << "Enter n >= 0:" <<endl;
	cin >> n;
	int factorial = 0;
	int i=2;
	int prime;
	
	if(n<0)
		cout << "Invalid input ";
	else if(n==0)
		cout << "Not a factorial ";
	else if(n==1)
		cout << "The number is 0! and 1! No prime factors";
	else if(n==2)
	{
		cout << "The number is 2! The largest prime factor is 2";
	}
	else
	{
		while(n!=0)
		{

			while(n%i==0 && n!=1)
			{
				factorial = n;
				n = n/i;
				prime = 1;
				
				i++;
			}
			if(n>1)
			{	
				cout << "Not a factorial";
				break;
			}
			break;
		}
		// if factorial != 0 ... need to add the code
		for(int x = factorial ; x > 0 ; x--)
		{
			if(x % 2 != 0)
			{
				prime = x;
				break;
			}
		}
		
		if(n==1){
			cout << "The number is " << factorial << "! The largest prime factor is " << prime << endl;
		}
		
	}
	return 0;
}

