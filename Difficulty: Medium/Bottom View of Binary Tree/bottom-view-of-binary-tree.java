class Solution
{
    //Function to return a list containing the bottom view of the given tree.
    public ArrayList <Integer> bottomView(Node root)
    {
        // Code here
        ArrayList<Integer> ans=new ArrayList<Integer>();
        if(root==null){
            return ans;
        }
        Map<Integer,Integer> map=new TreeMap<>();
        Queue<Node> q=new LinkedList<Node>();
        root.hd=0;
        q.add(root);
        while(!q.isEmpty()){
            Node temp=q.remove();
            int hd=temp.hd;
            map.put(hd,temp.data);
            if(temp.left!=null){
                temp.left.hd=hd-1;
                q.add(temp.left);
            }
            if(temp.right!=null){
                temp.right.hd=hd+1;
                q.add(temp.right);
            }
        }
          for(Integer val:map.values()){
            ans.add(val);
        }
        
        return ans;
        
        
    }
}