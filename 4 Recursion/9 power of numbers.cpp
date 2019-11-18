#include <iostream>

using namespace std;
long long power(int N,int R)
{
//Your code here
if(R==0)
return 1;
return ((power(N,R-1)*N)%(1000000007));

}

int main()
{
    cout<<power(12,21);
    return 0;
}
