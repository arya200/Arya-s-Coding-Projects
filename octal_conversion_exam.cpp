/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>

using namespace std;

int main()
{
    int octal[]={1,0,0,1};
    int n=4;
    int sum=0;
    int power = n-2;
    for(int i=0;i<n;i++)
    {
        int value =2;
        for(int j=0;j<power;j++)
        {
            value = value*8;
        }
        power = power-1;
        if(power>=0)
        {
            sum = sum+(octal[i]*value);
            cout << 
            
        }
        else
        {
            
            sum = sum+(octal[i]*1);

        }
    }
    
    cout << sum << endl;
    
}
