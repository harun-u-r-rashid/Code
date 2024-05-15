
// Public encapsulation


#include<bits/stdc++.h>
using namespace std;

class Student{
        public:
        int roll;
        
        Student(int roll){
                this->roll = roll;
        }

        void display(){
                cout << roll << endl;
        }
};



int main(){
        Student student(2006015);
        student.display();
        student.roll = 2006030;
        student.display();

        return 0;
}


// Private incapsulation

#include<bits/stdc++.h>
using namespace std;

class Student{
        private:
           int roll;

        public:
        
           Student(int roll){
                this->roll = roll;
        }

        void setter(int r){
                roll = r;
        }

        int getter(){
                return roll;
        }
};



int main(){
        Student student(2006015);
        student.setter(2006013);
        cout << student.getter() << endl;

        return 0;
}
