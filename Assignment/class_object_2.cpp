#include<iostream>
using namespace std;

class Student
{
	//Access Modifiers : public,private,protected
	
	//class members
	public:
		
		float h; //can access thought the class
		
		//setter method
		void input()
		{
			int id;
			string name;
			float height;
			
			cout<<"Enter id : ";
			cin>>id;
			cout<<"Enter name : ";
			cin>>name;
			cout<<"Enter height : ";
			cin>>height;
			
			h=height; //assign to class var
		}
		
		//getter method
		void eligiblity_check()
		{
			if(h>=5.5){
				cout<<"Eigible for match";
			}
			else
			{
				cout<<"Not Eligible ..";
			}
				
		}
};



int main()
{
	Student o1;
	
	o1.input();
	o1.eligiblity_check();
	
	return 0;
}
