class Solution
{
    //calheight
    int calHeight(Node root)
    {
       if(root==null)
          return 0;
          
          int lh = calHeight(root.left);
          int rh = calHeight(root.right);
          
          return Math.max(lh,rh)+1;
          
    }
    
    //chk level
    boolean chklevel(Node root,int level,int H)
    {
        if(root==null)
          return true;
          
          if(root.left==null && root.right==null && level!=H-1)
            return false;
            
          return chklevel(root.left,level+1,H) && chklevel(root.right,level+1,H);
    }
    
    
    boolean check(Node root)
    {
       int H = calHeight(root);    
       
       return chklevel(root,0,H);
    }
}