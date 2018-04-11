#include <stdlib.h>
#include <math.h>
#include <stdio.h>

//test with double vs. long double vs double_t if this makes a difference in rounding error

double_t solve_quartic(double_t a, double_t b, double_t c){
    //there are 2, a plus and minus; we only take the plus
    return (-b + sqrt(b*b - 4*a*c))/(2*a);
}

int main() {
    double_t b = 1e-10;
    for (int i =0; i<20; i++){
        b*=10;
        printf("%e\n", solve_quartic(2,b,3));
    }
    //std::cout << "Hello, World!" << std::endl;
    return 0;
}