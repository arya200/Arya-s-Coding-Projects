#include <iostream>
using namespace std;

int main()
{
	int n;
	cin >> n;
	int factorial;
	int i=2;
	int check = 1;
	if(n=0)
	{

	}

	while(check!=0)
	{


		int value = n%i;


		cout << "the value is " << n << endl;
		if(n%i==0 && n!=1)
		{

			cout << "im here" << endl;

			factorial = n;
			n = n/i;
		}
		else
		{

			cout << "Not a factorial" << endl;
			break;
		}

		i++;		
	}

	cout << "the factorial is " << factorial << endl;
}

else if ()
{
	 
}