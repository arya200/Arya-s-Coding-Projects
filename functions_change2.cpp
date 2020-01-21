#include <iostream>
#include <fstream>
using namespace std;

int readPrefs(char fileName[], int ngames, int prefs[])
{
	int check=0;
	int game_id, rating;
	ifstream inFS(fileName);
	for(int i= 0; i<ngames; i++)
	{
		prefs[i] = 0;
	}

	while(!inFS)
	{
		
		return -1;
	}

	while(inFS >> game_id >> rating)
	{
		if (!(game_id < 0 || game_id >200) && !(rating < 0 || rating >5)) 
      	{
      			prefs[game_id] =rating;
      			//cout << "game id " << game_id << " rating " << prefs[game_id] << endl;
      			check++;

      	}

      	
	}

	
	return check;

}

int readPlan(char fileName[], int ngames, int plan[])
{

	int day;
	int game_id;
	ifstream inFS(fileName);

	while(!inFS)
	{
		return -1;
	}
	
	
	while(inFS >> day >> game_id)
	{
		
      	plan[day] = game_id;
      	//cout << "day number: " << day << " game id: " << plan[day]<< endl;
    }

    return 0;
}

int computeFunLevel (int start, int duration, int prefs[], int ngames, int plan[])
{
	int sum = 0;
	if((start+duration) > 366)
	{
		return -1;
	}
	else
	{
		for(int i=start; i<(start + duration); i++)
		{

			int location = plan[i];
			sum = sum + prefs[location];

		}
	}
	return sum;

}

int findBestVacation (int duration, int prefs[], int ngames, int plan[])
{
	int max = 0;
	int start_date;
	int fun;


	for(int i=1; i <= (366-duration); i++)
	{

		fun = computeFunLevel(i, duration, prefs, ngames, plan);

		if(fun > max)
		{
			max = fun;
			start_date = i;
		}
	}


	return start_date;

}

