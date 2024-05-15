#include<bits/stdc++.h>
using namespace std;

class Vehicle{
        public:
        void move(){
                cout << "Can move in roads or water or air" << endl;
        }
};



class Truck : public Vehicle{
        public:
        void move(){
                cout << "Moves in the road" << endl;
        }
};


class Ship : public Vehicle{
        public:
        void move (){
                cout << "Moves in the water" << endl;
        }
};



int main(){
        Vehicle vehicle;
        Truck truck;
        Ship ship;


         vehicle.move();
        truck.move();
        ship.move();

        return 0;
}