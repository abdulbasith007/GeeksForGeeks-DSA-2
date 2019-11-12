# There are many ways to do this problem:-
#   1) Using inbuilt popcount() in C++
#   2) checking if the number (bitwise &) number-1 is zero
  

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
void power1(long long int n)
{
  int res = __builtin_popcountll(n);
  if (res==1)
      cout<<"True\n";
  else
      cout<<"False\n";  
}
int main() {
    int t; 
    long long int n;
    cin>>t;
    while(t--)
    {
        cin>>n;
        power1(n);
    }
    return 0;
}



//Aliter: 

bool isPowerofTwo(long long n){
  return (n&(n-1) == 0);
}
