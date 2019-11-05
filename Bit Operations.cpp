#include <bits/stdc++.h>
using namespace std;

int main(){
	int x = 5, y = 4;     // No's in binary 5 - 101 | 4 - 100   

	printf("%d ", x&y);   //  x  101  (5)
	                      //  y	 100  (4)
	                      // x&y 100  (4)

	printf("%d ", x|y);   //  x  101  (5)
	                      //  y	 100  (4)
	                      // x|y 101  (5)
                          
	printf("%d ", x^y);   //  x  101  (5)
	                      //  y	 100  (4)
	                      // x^y 001  (1)
	
	printf("%d ", ~x);    // Negation
	printf("%d ", ~y);    // Negation

}

