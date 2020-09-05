#include <bits/stdc++.h> 
using namespace std; 

struct Node 
{ 
    int data; 
    struct Node *next; 
    struct Node *prev; 
}; 

void insert_in_End(struct Node** start, int value) 
{ 
    if (*start == NULL) 
    { 
        struct Node* new_node = new Node; 
        new_node->data = value; 
        new_node->next = new_node->prev = new_node; 
        *start = new_node; 
        return; 
    } 
    Node *last = (*start)->prev; 

    struct Node* new_node = new Node; 
    new_node->data = value;  
    new_node->next = *start; 
    (*start)->prev = new_node; 
    new_node->prev = last; 
    last->next = new_node; 
} 
  
void display(struct Node* start) 
{ 
    struct Node *temp = start; 
  
    printf("\nList : "); 
    while (temp->next != start) 
    { 
        printf("%d ", temp->data); 
        temp = temp->next; 
    } 
    printf("%d ", temp->data); 
} 
  
int main() 
{ 
    struct Node* start = NULL; 
    insert_in_End(&start, 15);  
    insert_in_End(&start, 4); 
    insert_in_End(&start, 9); 
    display(start); 
    return 0; 
} 
