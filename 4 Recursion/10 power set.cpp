
// CPP program to generate power set
#include <bits/stdc++.h>
using namespace std;

/*This is a function problem.You only need to complete the function given below*/
//User function Template for C++
//Complete this function
void powerSet(string str, vector<string> &v,int index = 0, string curr = "")
{
int n = str.length();
if (index == n) {
v.push_back(curr);
return;
}
powerSet(str, v, index + 1, curr + str[index]);
powerSet(str, v, index + 1, curr);
}

vector <string> powerSet(string s)
{
vector<string> v;
powerSet(s,v);
return v;
}



// Driver code
int main()
{
    int T;
    cin>>T;
    while(T--)
    {
        string s;
        cin>>s;
        vector<string> ans = powerSet(s);
        sort(ans.begin(),ans.end());
        for(auto x:ans)
        cout<<x<<" ";
        cout<<endl;
        
        
    }

return 0;
} 
