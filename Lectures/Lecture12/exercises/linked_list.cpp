# include <iostream>

using namespace std;


class Node{
public:
    int val;
    Node* next;

    Node(int n){
        val = n;
    }
};
class LinkedList{
public:
    Node* head;
    LinkedList(){
        head = NULL;
    }
    void insert(int n){
        // insert an integer to the end of linked list
        if(head==NULL){
            // when the linked list is empty
            head = new Node(n);
        }
        else{
            // when it's not empty
            Node *temp=head;
            // (*temp).next is same as temp->next
            while(temp->next!=NULL)
                temp=temp->next;
            temp->next = new Node(n);
        }
    }
};

int main(){
    Node* n = new Node(1);
    n->next = new Node(2);


    DataType* dt; //int, float, Node, LinkedList
    // dt is a point - it stores the address of the actual object
    // *dt - it's the actual object


    LinkedList myList;
    int n;
    cin>>n;
    myList.insert(n);
}