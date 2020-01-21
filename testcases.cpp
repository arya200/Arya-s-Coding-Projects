#include<iostream>
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
      
    cout << "check value is " << check << endl;
      if(check >= 2 )
      {
          return check;
        
      }
      
         
    if(check < 2)
    {
        return check;
    }
    
}


int main()
{
	int a;
	int b;
	int loop_number;
	int digit;
	int check;
	int number_of_good = 0;
	cout << "Enter numbers a<=b: ";
	cin >> a >> b;
	if(a >=b || a <0 || b<0 || a>10000 || b>10000)
	{
		cout << "Invalid input" << endl; 
		return 0;
	}

	for(int i = a; i<= b; i++)
	{
		int n = i;
		loop_number = i;

		while (loop_number > 0)
		{

			digit = loop_number%10;
			
			
			cout << "the n value is " << n << endl;
			check = countDigitOccurrences(n, digit);
			
			
			
			if(check <=1)
			{
			    number_of_good++;
				break;
				
			}
			else
			{
			    break;
			}
            
            
			loop_number = loop_number/10;
		 
		}
	}


	cout << "number of good numbers " << number_of_good << endl;
}
