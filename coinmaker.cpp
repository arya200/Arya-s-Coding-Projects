#include<iostream>
using namespace std;


int main()
{
	int pennies = 1;
	int nickel = 5;
	int dimes = 10;
	int quarter_value = 25;
	int num_of_quarters = 0;
	int num_of_dimes = 0;
	int num_of_nickels = 0;
	int num_of_pennies=0;
	int temp = 0;


	int dollar_value;
	int cent_value;

	cout << "Enter dollars: "; cin >> dollar_value;

	cout << "Enter cents: "; cin >> cent_value;


	if ( dollar_value > 0)
	{
		num_of_quarters = dollar_value * 4;
	}

	temp = cent_value; 

	if( cent_value >= 25)
	{
			num_of_quarters = (num_of_quarters +  (cent_value / quarter_value));
			temp = cent_value % quarter_value;
			
	}

	if( temp >= 10)
	{
			num_of_dimes = temp/10;
			temp = temp % 10;
			
	}

	if( temp >= 5)
	{
			num_of_nickels = temp/5;
			temp = temp % 5;

	}

	if( temp >=1)
	{
		num_of_pennies = temp/1;

	}
	

	
	int total_coins = num_of_quarters+num_of_pennies+num_of_dimes+num_of_nickels;


	cout << "Pennies: " << num_of_pennies << endl;
	cout << "Nickels: " << num_of_nickels << endl;
	cout << "Dimes: " << num_of_dimes << endl;
	cout << "Quarters: " << num_of_quarters << endl;
	cout << "Total coins used: " << total_coins << endl;

	


}



	




