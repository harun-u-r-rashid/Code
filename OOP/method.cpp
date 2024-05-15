

#include<bits/stdc++.h>
using namespace std;


class myClass {
        public:
        int roll;


        void cppMethod() { //Here this is the method
                cout << "This is the cpp method" << endl;
                cout << "Roll : " << roll << endl;
        }
};


int main() {
        myClass student;
        student.roll = 10;

        student.cppMethod();
        return 0;
}