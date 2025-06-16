class MyStack {
    // class StackNode {
    //     int data;
    //     StackNode next;
    //     StackNode(int a) {
    //         data = a;
    //         next = null;
    //     }
    // }
    StackNode top;

    // Function to push an integer into the stack.
    void push(int a) {
        StackNode temp = new StackNode (a);
        temp.next = top;
        top = temp; // Add your code here
    }

    // Function to remove an item from top of the stack.
    int pop() {
        if (top==null) return -1;
        int popped = top.data;
        top=top.next;
        return popped;
        // Add your code here
    }
}