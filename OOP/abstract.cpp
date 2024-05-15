

#include<bits/stdc++.h>
using namespace std;


class Shape{
        public:
        virtual void sides() = 0;
};


class Rectangular : public Shape{
        public:
        void sides(){
                cout << "My opposite sides are equal" << endl;
        }
};




int main(){
        Rectangular rectangle;
        rectangle.sides();

        return 0;
}
