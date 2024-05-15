#include<bits/stdc++.h>
using namespace std;



class Shape {
        public:
        int radius;
};



// Inherits the class Shape
class Circle: public Shape{
        public:
        int area() {
                return 3.1415*radius*radius;
        }
};

int main() {
        Circle circle;
        circle.radius = 5;
        cout << circle.area() << endl;

        return 0;
}