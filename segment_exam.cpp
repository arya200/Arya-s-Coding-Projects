/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>

using namespace std;

int main()
{
    int n = 6;
    int arr[] = {5,2,3,4,4,1};
   int segment=0;
   for(int i=0;i<n-1;i++)
   {
       if(arr[i] != arr[i+1])
       {
           cout<<arr[i] << " " << arr[i+1] << endl;
           segment++;
       }
       
   }
   
   
   cout << segment +1 << " segments" << endl;
   
   
   
   
}

