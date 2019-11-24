void printfrequency(int arr[], int n)
{ 
    for (int i = 0; i < n; i++)
        arr[i] -= 1;
        
    for (int i = 0; i < n; i++)
        arr[arr[i]%n] += n;
        
    for (int i = 0; i < n; i++)
        cout<<arr[i]/n<<" ";
    
	
} 
