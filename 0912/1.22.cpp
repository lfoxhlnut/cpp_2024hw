#include "Sales_item.h"
using namespace std;
int main(){
Sales_item a;
while (cin>>a)
{
	Sales_item b;
	while (cin>>b)
	{
		if(a.isbn() == b.isbn())
		a+=b;
		else
		break;
	}
	cout<<a<<endl;
	
}

}

