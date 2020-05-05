# include <iostream>

using namespace std;


class LinkedList{
public:
    class Node{
    public:
        int val;
        Node* next;
        Node(int n){
            val = n;
        }
    };
    Node* head;
public:
    LinkedList(){
        head = NULL;
    }
    void insert(int n){
        if(head==NULL){
            head = new Node(n);
        }
        else{
            Node* temp=head;
            while(temp->next!=NULL)
                temp=temp->next;
            temp->next = new Node(n);
        }
    }
};

int main(){
    LinkedList myList;
    int n;
    cin>>n;
    myList.insert(n);
}