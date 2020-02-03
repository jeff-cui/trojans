#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(int argc, char*argv[]) {
	// if we don't have arguments for x,y and d, don't run program
	if (argc != 4) {
		printf("Program requires 3 inputs for calculation.");
		return 0;
	}

	else {
		// grab x,y and d from command line input
		float x = atof(argv[1]);
		float y = atof(argv[2]);
		float d = atof(argv[3]);

		// calculate z
		float z = pow(x,2) + pow(y,2);

		// calculate e, e is a randomly generated float from 0 to z*d
		float e = (float)rand() / (float)(RAND_MAX/(z*d)); 

		// calculate zd and print
		float zd = z + e;
		printf("%f\n", zd);
	}
}