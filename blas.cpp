#include <iostream>
#include <cmath>


int amax(const double* x, const unsigned int len) 
{
	
	double max=x[0];
	unsigned int location=0;
	if(len==0)
	{
		location = -1;
	}
	else
	{
		for(unsigned int j=0;j<len-1;j++)
		{
			if(std::abs(max)<std::abs(x[j+1]))
			{
				max = x[j+1];
				location=j+1;
				
			}
			

		}
	}

		
	return location;
	
}


double asum(const double* x, const unsigned int len) 
{
	double sum = 0;
    for(unsigned int i=0; i<len; i++)
    {
    	sum = sum + std::abs(x[i]);
    }
    return sum;

}

void axpy(const double a, const double* x, double* y, const unsigned int len) 
{
	
	for(unsigned int i = 0; i<len; i++)
	{
		y[i] = y[i] + (x[i]*a);
	}




    
}

void copy(const double* src, double* dest, const unsigned int len) 
{
	for(unsigned int i = 0; i<len; i++)
	{
		dest[i]  = src[i]; 
	}
    
}

double dot(const double* x, const double* y, const unsigned int len) 
{
    double sum = 0;
    for (unsigned int i=0; i<len; i++)
    {
    	sum = sum + (x[i]*y[i]);
    }
    return sum;
}

double norm2(const double* x, const unsigned int len) 
{
	double magnitude = 0;
	double sum=0;
    for(unsigned int i=0;i<len;i++)
    {
    	sum = sum + (x[i]*x[i]);
    	
    }
    magnitude = sqrt(sum);
    return magnitude;

}

void scale(const double a, double* x, const unsigned int len) 
{
    for(unsigned int i=0;i<len;i++)
    {
    	x[i] = a*x[i];
    }


}

void swap(double* x, double* y, const unsigned int len) 
{
	for(unsigned int i =0; i<len; i++)
	{
		double temp=x[i];
		x[i] = y[i];
		y[i] = temp;
	}
    
}

