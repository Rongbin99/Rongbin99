#include <iostream>
#include <cmath>
// TODO: fix so that if not an INT is entered, it re-asks for input.
// TODO: create GUI
int main() {
    bool exit = true;
    
    while (exit) {
        try {
            double a, b, c;
            exit = false;
            std::string trigger;
        
            std::cout << "=====Quadratic Calculator Solver=====" << std::endl;
            std::cout << "Enter Coefficients: " <<std::endl;
            std::cout << "a: ";
            std::cin >> a;
            std::cout << "b: ";
            std::cin >> b;
            std::cout << "c: ";
            std::cin >> c;
            std::cout << "\n \n";

            long double discriminant = (b * b) - (4 * a * c);
            long double x1 = ((-b) + (sqrt(discriminant))) / (2 * a);
            long double x2 = ((-b) - (sqrt(discriminant))) / (2 * a);

            if (discriminant < 0) {
                std::cout << "No roots, discriminant is negative! " << discriminant << std::endl;
            }
            else {
                std::cout << "Discriminant: " << discriminant << std::endl;
                std::cout << "Root 1: " << x1 << std::endl;
                std::cout << "Root 2: " << x2 << std::endl;
            }
            
            std::cout << "Press R to Reset. Press anything else to exit. ";
            std::cin >> trigger;

            if (trigger == "R" || "r") {
                exit = true;
            } else {
                exit = false;
            }
        }
        catch(std::invalid_argument &error) {
            std::cout << error.what() << '\n';
        }
    }
    return 0;
}
