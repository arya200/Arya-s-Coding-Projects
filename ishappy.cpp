/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>

using namespace std;



bool ishappy(int n)
{
    int sum = 0;
    while(true)
    {   
        if(sum==1)
        {
            return true;
            break;
        }
        else if(sum==4)
        {
            return false;
            break;
        }
        
        if(n<10)
        {
           sum = n*n; 
        }
        else
        {   
            sum = 0;
            while(n>0)
            {
                
                int digit = n%10;
                sum = sum + (digit*digit);
                n = n/10;
            }
            
        }
        
        n = sum;
        
        
    }
    
    
}

int main()
{
     bool answer = ishappy(13);
     cout << answer << endl;
}