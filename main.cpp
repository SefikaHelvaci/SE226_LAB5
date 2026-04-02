#include <iostream>



double solve(int n) {
    if (n <= 0) {
        return 0.0;
    }
    double curr = (n % 2 != 0) ? (1.0 / n) : (-1.0 / n);
    return curr + solve(n - 1);
}


int main() {
    int n;
    std::cout << "Enter n: ";
    std::cin >> n;

    if (n < 0) {
        std::cout << "Enter positive int" << std::endl;
    }else{
        double result = solve(n);
        std::cout << "Result: " << result << std::endl;
    }
    return 0;
}

