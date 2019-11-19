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



// Python Code:
def sub(str, output=""):
  if len(str) == 0:
    print(output)
    return 

  sub(str[1:], output)
  sub(str[1:], output+str[0])  

sub("ABC")
//
