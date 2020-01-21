#include <iostream>
using namespace std;

int main()
{
int i;
int print;
int num = 23;

if(num%2==0)
{
	print=0;
	for(i=0;i<num;i++)
	{
		cout << print << " ";
		print+=2; 
	}
}
else
{
	print=1;
	for(i=0;i<num;i++)
	{
		cout << print << " ";
		print+=2;
	}

}
}