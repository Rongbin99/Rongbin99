#include <iostream>
#include <cmath>

class TwoDimension {
    public:
        long double x;
        long double y;
        
        virtual long double Area (long double x, long double y) {
            return x*y;
        }
        virtual long double Perimeter (long double x, long double y) {
            return 2*(x+y);
        }

    private:
        static unsigned int token_id;

};

class ThreeDimension:public TwoDimension {
    public:
        long double z;

        virtual long double Area (long double x, long double y) override {
            return x*y*z;
        }
        virtual long double Perimeter (long double x, long double y) override {
            return 2*(x+y+z);
        }
    
    private:
        static unsigned int token_id;
};

class Circle {
    public:
        long double radius;

        virtual long double Area (long double r) {
            return (r*r)*M_PI;
        }
        virtual long double Circumference (long double r) {
            return 2*M_PI*r;
        }

    private:
        static unsigned int token_id;
};

class Sphere:public Circle {
    public:
        virtual long double Area (long double r) override {
            return (4/3)*M_PI*(r*r*r);
        }
        virtual long double Circumference (long double r) override {
            return 4*M_PI*(r*r);
        }
    
    private:
        static unsigned int token_id;
};

unsigned int TwoDimension::token_id = 0;
unsigned int ThreeDimension::token_id = 0;
unsigned int Circle::token_id = 0;
unsigned int Sphere::token_id = 0;

int main() {
    long double width;
    long double height;
    long double depth;
    long double radius;

    std::cout << "Enter width: ";
    std::cin >> width;
    std::cout << "Enter height: ";
    std::cin >> height;
    std::cout << "Enter depth: ";
    std::cin >> depth;
    std::cout << "Enter radius: ";
    std::cin >> radius;

    if (radius == 0) {
        if (depth == 0) {
            TwoDimension *p_two = new TwoDimension();

            p_two->x = width;
            p_two->y = height;

            std::cout << std::endl;
            std::cout << "Area: " << p_two->Area(p_two->x, p_two->y) << std::endl;
            std::cout << "Perimeter: " << p_two->Perimeter(p_two->x, p_two->y) << std::endl;
        }
        else {
            ThreeDimension *p_three = new ThreeDimension();

            p_three->x = width;
            p_three->y = height;
            p_three->z = depth;

            std::cout << std::endl;
            std::cout << "Volume: " << p_three->Area(p_three->x, p_three->y) << std::endl;
            std::cout << "Surface Area: " << p_three->Perimeter(p_three->x, p_three->y) << std::endl;
        }
    }
    else {
        Circle *p_circle = new Circle();
        Sphere *p_sphere = new Sphere();

        p_circle->radius = radius;

        std::cout << std::endl;
        std::cout << "Area: " << p_circle->Area(p_circle->radius) << std::endl;
        std::cout << "Circumference: " << p_circle->Circumference(p_circle->radius) << std::endl;
        std::cout << std::endl;
        std::cout << "Volume: " << p_sphere->Area(p_circle->radius) << std::endl;
        std::cout << "Surface Area: " << p_sphere->Circumference(p_circle->radius) << std::endl;
    }
    return 0;
}