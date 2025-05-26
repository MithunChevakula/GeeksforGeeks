/*
class Node {
    int data;
    Node next;

    Node(int x) {
        data = x;
        next = null;
    }
} */

class Solution {
    public Node sortedInsert(Node head, int data) {
        // code here
        if(head==null){
            return new Node(data);
        }
        Node node=new Node(data);
        
        Node temp=head;
        
         if(node.data<temp.data){
            Node curr=head;
            
            while(curr.next!=head){
                curr=curr.next;
            }
            curr.next=node;
            node.next=head;
            return node;
        }
        
        while(temp.next!=head && temp.next.data<node.data ){
                temp=temp.next;
        }
        node.next=temp.next;
        temp.next=node;
        return head;
        
    }
}