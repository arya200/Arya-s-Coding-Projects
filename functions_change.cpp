
#include <iostream>
#include "functions.h"
using namespace std;



int countDigitOccurrences (int n, int digit)
{
  
  int check = 0;
 

      while (check <=1 && n>0)
      {
        
        if(digit == (n%10))
        {
          
            check++;
            
           
        }

        n = n/10;
       }
      

      if(check == 2)
      {
          return check;
        
      }
      
         
    if(check < 2)
    {
        return check;
    }
    
}
