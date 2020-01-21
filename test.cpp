#include<iostream>
using namespace std;

int main()
{
	int number_entered;
	int check=0;
	int min;
	int check2;

	while (check == 0)
	{
		cin >> number_entered;

		if(number_entered == 0)
		{
			check2 = 1;
			break;
		}
		else if(number_entered < min)
		{
			min = number_entered;
		}
			
	}

	if(check2 == 1)
	{
		cout << "empty";
	}
	else
	{
		cout << "min: " << min;
	}
	
	
}
