class Solution {
    // Function to return a list of integers denoting spiral traversal of matrix.
    public ArrayList<Integer> spirallyTraverse(int mat[][]) {
        
        int n=mat.length,m=mat[0].length,s=n*m;
        ArrayList<Integer> ans=new ArrayList<>();
        int a=0,b=0,c=n-1,d=m-1;
        while(ans.size()<s){
            for(int i=b;i<=d && ans.size()<s;i++) ans.add(mat[a][i]);
            a++;
            for(int i=a;i<=c && ans.size()<s;i++) ans.add(mat[i][d]);
            d--;
            for(int i=d;i>=b && ans.size()<s;i--) ans.add(mat[c][i]);
            c--;
            for(int i=c;i>=a && ans.size()<s;i--) ans.add(mat[i][b]);
            b++;
        }
        return ans;
    }
}

