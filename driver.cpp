#include <iostream>
#include <cmath>
#include "functions.h"
using namespace std;


int main()
{
	unsigned int noParticipants;
	char leftTeamName[255];
	char rightTeamName[255];
	cin >> noParticipants;
	cin >> leftTeamName;
	cin >> rightTeamName;
	double leftTeam[200];
	double rightTeam[200];
	bool LeftTeamVal;
	bool RightTeamVal;
	int netforce = 0;

	readForceValuesFromStdIn(leftTeam, rightTeam, noParticipants);
	LeftTeamVal = validForces(leftTeam, noParticipants);
	RightTeamVal = validForces(rightTeam, noParticipants);

	if ((RightTeamVal == false) &&  (LeftTeamVal == false)) 
	{
		cout << "both teams have an invalid force!";
    	return 1;
    }

	if (RightTeamVal == false) 
	{
		cout << rightTeamName << " has an invalid force!";
		return 1;

	}

	if (LeftTeamVal == false) 
	{
		cout << leftTeamName << " has an invalid force!";
		return 1;
	}

	netforce = calculateForce(leftTeam, rightTeam, noParticipants);
	printWinnerToStdOut(leftTeamName, rightTeamName, netforce);
}