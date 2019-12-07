int countOnes(int n)
{
    int cnt = 0;
    for (int i = 0; i<n; i++)
        if (arr[i] == 1)
            cnt++;
    return cnt;
}
