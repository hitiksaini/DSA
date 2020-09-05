#include<bits/stdc++.h> 
using namespace std; 
  
struct Node 
{ 
    int data; 
    struct Node *next; 
}; 

struct Node *addToEmpty(struct Node *last, int data) 
{ 
    if (last != NULL) 
      return last; 
    struct Node *temp =  
           (struct Node*)malloc(sizeof(struct Node)); 
    temp -> data = data; 
    last = temp; 
    last -> next = last; 
  
    return last; 
} 
  

struct Node *insertion_begin(struct Node *last, int data) 
{ 
    if (last == NULL) 
        return addToEmpty(last, data); 
  
    struct Node *temp =  
            (struct Node *)malloc(sizeof(struct Node)); 
  
    temp -> data = data; 
    temp -> next = last -> next; 
    last -> next = temp; 
  
    return last; 
} 
  


  
void traverse(struct Node *last) 
{ 
    struct Node *p; 
    if (last == NULL) 
    { 
        cout << "List is empty." << endl; 
        return; 
    } 
    p = last -> next; 
    printf("\nList : "); 
    do
    { 
        cout << p -> data << " "; 
        p = p -> next; 
    } 
    while(p != last->next); 
  
} 
int main() 
{ 
    struct Node *last = NULL; 
    last = addToEmpty(last, 12); 
    last = insertion_begin(last, 8); 
    last = insertion_begin(last, 4); 
    traverse(last); 
    return 0; 
} 
