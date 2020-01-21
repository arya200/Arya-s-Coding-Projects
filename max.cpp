int max(int a, int b)
{
	if (a >= b) {
		return a;
	} else {
		return b;
	}
}

double max(double a, double b)
{
	if (a >= b) {
		return a;
	} else {
		return b;
	}
}

char max(char a, char b)
{
	if ((a >= 97) && (b < 97)) {
		return a;
	} else if ((b >= 97) && (a < 97)) {
		return b;
	} else if (a >= b) {
		return a;
	} else {
		return b;
	}
}

int *max (int *A , int D, int *B, int E)
{
	int len; 
	int s;
	bool capA;

	if(D>E)
	{
		len = D;
		s = E;
		capA = true;
	}
	else
	{
		len = E;
		s = D;
		capA = false;
	}

	int* maxArray = new int[len];
	for(int i = 0; i < s; i++)
	{
		if(A[i] < B[i])
			maxArray[i] = B[i];
		else
			maxArray[i] = A[i];
	}
	for(int i = s; i < len; i++)
	{
		if(capA)
			maxArray[i] = A[i];
		else
			maxArray[i] = B[i];
	}

	return maxArray;

}

char* max(char* a, char*b)  // c-style strings
{
	int i = 0;
	char capA[255];
	while(a[i] != '\0')
	{
		if(a[i] >= 97)
			capA[i] = a[i]-32;
		else
			capA[i] = a[i];

		i++;
	}

	int j = 0;
	char capB[255];
	while(b[j] != '\0')
	{
		if(a[j] >= 97)
			capB[j] = b[j]-32;
		else
			capB[j] = b[j];

		j++;
	}

	if(capA>capB)
		return a;
	return b;
}