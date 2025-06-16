class Solution {
    public int inorderSuccessor(Node root, Node x) {
        int successor=-1;
        while(root!=null){
            if(x.data<root.data){
                successor=root.data;
                root=root.left;
            }
            else root=root.right;
        }
        return successor;
    }
}