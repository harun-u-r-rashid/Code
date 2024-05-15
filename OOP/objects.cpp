#include<bits/stdc++.h>

using namespace std;

class cppClass{
        public:
        int roll;
        string name; 
};

int main(){
        cppClass student;
        student.roll = 100;
        student.name = "Harun";

        cout << student.name << " " << student.roll << endl;

        return 0;
}


// Here, student is the object