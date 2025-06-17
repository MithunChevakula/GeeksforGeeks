class Solution {
    Node reverse(Node head){
        Node prev=null,curr=head,next=null;
        while(curr!=null){
           next=curr.next;
            curr.next=prev;
            prev=curr;
            curr=next;
        }
        return prev;
    }
    public Node addOne(Node head) {
        head=reverse(head);
        Node current=head;
        int carry=1;
        while(current!=null){
            int val=current.data+carry;
            current.data=val%10;
            carry=val/10;
            if(current.next==null && carry==1){
                current.next=new Node(1);
                current=current.next;
            }
            current=current.next;
        }
        return reverse(head);
    }
}

