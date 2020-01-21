/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>

using namespace std;

int main()
{
    int sarahDonations[] = {100,200,50,100,100,50,-10};
    int kellyDonations[] = {10,130,50,140,80,190,-40};
    
    int size_sarah=0;
    int size_kelly = 0;
    int location =0;
    int sum_sarah=0;
    int sum_kelly=0;
    
    while(sarahDonations[location]>0)
    {
        sum_sarah = sum_sarah+sarahDonations[location];
        location++;
    }
    
    size_sarah=location;
    location=0;
    
    while(kellyDonations[location]>0)
    {
        sum_kelly = sum_kelly + kellyDonations[location];
        location++;
    }
    
    size_kelly=location;
    
    cout << "size of kelly" << size_kelly << endl;
    cout << "size of sarah" << size_sarah << endl;
    cout << "sum of kelly" << sum_kelly << endl;
    cout << "sum of sarah" << sum_sarah << endl;
    if((size_kelly<5 && size_sarah >=5)&&(sum_sarah>300 &&sum_kelly>300))
    {
        cout << "Sarah Wins" << endl;
        cout << "im here" << endl;
    }
    else if((size_kelly >= 5 && size_sarah<5)&&(sum_sarah>300 &&sum_kelly>300))
    {
        cout << "Kelly wins" << endl;
    }
    else if((size_sarah <5 && size_kelly <5)||(sum_kelly<300 && size_sarah<5)||(sum_sarah<300&&size_kelly<5)||(sum_sarah<300)&&(sum_kelly<300))
    {
        cout << "do not qualify" << endl;
    }
    else if((sum_kelly <300 && sum_sarah>=300) && (size_kelly>=5 &&size_sarah>=5))
    {
        cout << "Sarah Wins" << endl;
    }
    else if((sum_kelly >=300 && sum_sarah <300)&& (size_kelly>=5 &&size_sarah>=5))
    {
        cout << "Kelly wins" << endl;
    }
    else
    {
        double average_sarah = sum_sarah/size_sarah;
        double average_kelly = sum_kelly/size_kelly;
        
        if(average_sarah>average_kelly)
        {
            cout << "Sarah Wins" << endl;
        }
        else if(average_sarah < average_kelly)
        {
            cout << "Kelly wins" << endl;
        }
        else
        {
            if(size_sarah>size_kelly)
            {
                cout << "sarah wins" << endl;
            }
            else if(size_sarah < size_kelly)
            {
                cout << "kelly wins" << endl;
            }
            else
            {
                cout << "they tie" << endl;
            }
            
        }
        
    }
    
    
    
}
