class Solution {
    static class Pair{
        Node node;
        int hd;
        Pair(Node node,int hd){
            this.node=node;
            this.hd=hd;
        }
    }
    static ArrayList<Integer> topView(Node root) {
        ArrayList<Integer> ans =new ArrayList<>();
        if(root==null){
            return ans;
        }
        TreeMap<Integer,Integer> map =new TreeMap<>();
        Queue<Pair> q=new LinkedList<>();
        q.add(new Pair(root,0));
        while(!q.isEmpty()){
            Pair current=q.poll();
            Node node=current.node;
            int hd=current.hd;
            
            if(!map.containsKey(hd)){
                map.put(hd,node.data);
            }
            if(node.left!=null){
                q.add(new Pair(node.left,hd-1));
            }
            if(node.right!=null){
                q.add(new Pair(node.right,hd+1));
            }
        }
        ans.addAll(map.values());
        return ans;
    }
}