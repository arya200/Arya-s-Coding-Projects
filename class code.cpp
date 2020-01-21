#include <iostream>
using namespace std:

int main()
{
	const unsigned int noRow = 2;
	const unsigned int noCols = 3;
	int arr2[noRows][noCols];
	int assignment = 0;
	for(int i = 1; i<=rows ; i++)
	{
		for(int j = 1; j <=noCols; j++ )
		{
			arr2[i][j] = assignment;
			assignment++;
		}
		
	}

	cout << arr2 << endl;
}