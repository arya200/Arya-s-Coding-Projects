#include <cstdlib>
#include <cmath>

using std::sqrt;

double approx_pi(int seed, int n) {
    // seed the random number generator
    srand(seed);

    double check = 0.0;
    for (int i = 0; i < n; i++) {
    	double x = static_cast<double>(rand()) / RAND_MAX;
    	double y = static_cast<double>(rand()) / RAND_MAX;
    	if (sqrt(pow(x, 2)+pow(y, 2)) <= 1) {
    		check++;
    	}
    }

    double pi = 4 * (check / n);

    // TODO(student): implement the rest.
    // simulate the dart-throwing process
    // estimate the area of the quadrant
    // estimate the value of pi
    // return the estimated value of pi
    return pi;
}

