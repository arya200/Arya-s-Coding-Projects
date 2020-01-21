/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>

using namespace std;

int main()
{
    int n = 7;
    int arr[] = {1,2,3,4,5,6,7};
    int sum=0;
    int check = 0;
    int k = 8;
    for(int i=0; i<n; i++)
    {
        
        for(int j=i+1;j<n;j++)
        {
            sum = arr[i]+arr[j];
            if(sum==k)
            {
                cout << arr[i] << " " << arr[j] << endl;
                check++;
            }
            sum=0;
        }
    }
    if(check==0)
    {
        cout << "none" << endl;
    }
}

