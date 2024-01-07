#include <iostream>

int main();

class TwoD {
    public:
        double x;
        double y;
        virtual double area (double x, double y) {
            return x*y;
        }
        virtual double perimeter (double x, double y) {
            return 2*(x+y);
        }

    protected: 
        static unsigned int token_id;
};

class ThreeD:public TwoD {
    public:
        double z;
        double area (double x, double y) override {
            double area = x*y*z;
            return area;
        }
        double perimeter (double x, double y) override {
            double surface = 2*(x*y + x*z + y*z);
            return surface;
        }

    private:
        static unsigned int token_id;
};

int main() {
    TwoD square;
    ThreeD cube;
    std::cout << "Enter Width: ";
    std::cin >> square.x;
    std::cout << "Enter Height: ";
    std::cin >> square.y;
    std::cout << "Enter Depth: ";
    std::cin >> cube.z;
    std::cout << "Volume: " << cube.area(square.x, square.y) << std::endl;
    std::cout << "Surface Area: " << cube.perimeter(square.x, square.y) << std::endl;

    std::cout << "Area: " << square.area(square.x, square.y) << std::endl;
    std::cout << "Perimeter: " << square.perimeter(square.x, square.y) << std::endl;
    return 0;
}
