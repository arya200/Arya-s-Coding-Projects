#include <iostream>
using namespace std;
#include <fstream>
#include "functions.h"
#include "provided.h"

int main()
{
	int ngames, duration;
	char titles[MAX_TITLE_SIZE];
	char gameTitles[MAX_NB_GAMES][MAX_TITLE_SIZE];
	char prefs_name[MAX_TITLE_SIZE];
	char plan_name[MAX_TITLE_SIZE];
	int prefs[MAX_NB_GAMES];
	int plan[366];
	int start_date;

	cout << "Please enter ngames and duration: ";
	cin >> ngames >> duration;
	
	
	if(ngames>200 || ngames<=0 || duration <=0 || duration > 365)
	{
		cout << "Invalid input." << endl;
		return -1;

	}
	
	cout << "Please enter name of file with titles: ";
	cin >> titles;
	cout << "Please enter name of file with preferences: ";
	cin  >> prefs_name;
	cout << "Please enter name of file with plan: ";
	cin >> plan_name;

	readGameTitles(titles, ngames, gameTitles);

	int value = readPrefs(prefs_name, ngames, prefs);
	if( value == -1)
	{
		cout << "Invalid file." << endl;
		return 0;
	}
	int value1 = readPlan(plan_name, ngames, plan);
	if( value1 == -1)
	{
		cout << "Invalid file." << endl;
		return 0;
		
	}
	
	start_date = findBestVacation(duration, prefs, ngames, plan);
	cout << "Best start day is " << start_date << endl;
	cout << "Games to be played: " << endl;
	printGamesPlayedInVacation (start_date, duration, plan, gameTitles, ngames);





}
