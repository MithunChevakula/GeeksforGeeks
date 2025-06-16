void StackQueue :: push(int x)
{
     while(!s2.empty()){
        s1.push(s2.top());
        s2.pop();
    }
    s1.push(x);
   
    while(!s1.empty()){
        s2.push(s1.top());
        s1.pop();
    }
}

//Function to pop an element from queue by using 2 stacks.
int StackQueue :: pop()
{
        if(s2.empty()) return -1;
        int x=s2.top();
        s2.pop();
        return x;
}