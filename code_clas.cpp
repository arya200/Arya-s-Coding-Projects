#include <iostream>
using namespace std;

int main()
{
	/*const unsigned int noRow = 2;
	const unsigned int noCols = 3;
	int arr2[noRow][noCols];
	int assignment = 0;

	for(int i = 0; i<noRow ; i++)
	{
		for(int j = 0; j <noCols; j++ )
		{
			arr2[i][j] = assignment;
			cout << arr2[i][j] << '\t';
			assignment++;
		}
		cout << endl;
		
	*/
	
		
		string word = "Texas";
		int position = 0;
		for(int i = word.length(); i>=0; i--)
		{
			char temp = word[position];
			word[position]=word[i];
			word[i] = temp;

			position++;
		}

		cout << word;
}