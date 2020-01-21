#include <iostream>

using namespace std;

int main()
{
    int check=0;
    int n=1320;
    int sum;
    int i=1;
    
    if(n>0)
    {
       
        
        
        while((i+2)<=n)
        {
            sum = i * (i+1) * (i+2);

            
            if(sum == n)
            {
                check=1;
                break;
                
            }
            
            
            i=i+3;
            
        }
    }
    if(check==0)
    {
        cout << "it is not a triangular number" << endl;
    }
    else
    {
        cout << "it is a triangular number " << endl;
    }
}
