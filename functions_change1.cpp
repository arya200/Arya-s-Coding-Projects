#include <iostream>
#include "functions.h"
using namespace std;

void readForceValuesFromStdIn(double* leftTeam, double* rightTeam, unsigned const int noParticipants)
{
	double force;
	for(int i=0; i<noParticipants; i++)
	{
		cin >> force;
		leftTeam[i] = force;
		cin >> force;
		rightTeam[i] = force;


	}
}

bool validForces(const double* forces, unsigned const int noParticipants) 
{
    for (int i = 0; i < noParticipants; ++i) {
        if (forces[i] < 0) 
        {
            return false;
        }
    }
    return true; 
}

double calculateForce(const double* leftTeam, const double* rightTeam, unsigned const int noParticipants)
{

	double sum_left=0;
	double sum_right=0;
	for(int i=0; i<noParticipants; i++)
	{
		sum_left = sum_left + leftTeam[i];
		sum_right = sum_right + rightTeam[i];
	}

	const double netForce = sum_left - sum_right;
	return netForce;

}


void printWinnerToStdOut(const char* leftTeamName, const char* rightTeamName, const double netForce)
{
	double leftTeam[200];
	double rightTeam[200];

if (netForce < -5)
{
	cout << rightTeamName  << " wins!" << endl;
}

else if (netForce > 5)
{
	cout << leftTeamName << " wins!" << endl;
}
else
{
	cout << "Tie." << endl;
}

}


