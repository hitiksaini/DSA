#include<iostream>
using namespace std;
void merge(int a[], int Firstindex, int m, int Lastindex);
 
void mergeSort(int a[], int Firstindex, int Lastindex) 
{ 
    if (Firstindex < Lastindex) 
    {
        int m = Firstindex + (Lastindex - Firstindex)/2; 
        mergeSort(a, Firstindex, m); 
        mergeSort(a, m+1, Lastindex); 
   
        merge(a, Firstindex, m, Lastindex); 
    } 
}   
void merge(int a[], int Firstindex, int m, int Lastindex) 
{ 
    int x; 
    int y;
    int z;
    int sub1 = m - Firstindex + 1; 
    int sub2 =  Lastindex - m; 
    int First[sub1]; 
    int Second[sub2]; 
    for (x = 0; x < sub1; x++) 
        First[x] = a[Firstindex + x]; 
    for (y = 0; y < sub2; y++) 
        Second[y] = a[m + 1+ y]; 
    x = 0; 
    y = 0; 
    z = Firstindex; 
    while (x < sub1 && y < sub2) 
    { 
        if (First[x] <= Second[y]) 
        { 
            a[z] = First[x]; 
            x++; 
        } 
        else
        { 
            a[z] = Second[y]; 
            y++; 
        } 
        z++; 
    } 
    while (x < sub1) 
    { 
        a[z] = First[x]; 
        x++; 
        z++; 
    } 
    while (y < sub2) 
    { 
        a[z] = Second[y]; 
        y++; 
        z++; 
    } 
} 
int main() 
{ 
    int size;
    cout<<"Enter the size of the array "; cin>>size;
    int Hello[size],i;
    cout<<"Enter the elements";
    for(i=0; i<size; i++) cin>>Hello[i];
    mergeSort(Hello, 0, size - 1);
    for(i=0; i<size; i++)
    {
        cout<<Hello[i]<<" ";
    }
    return 0;
}
