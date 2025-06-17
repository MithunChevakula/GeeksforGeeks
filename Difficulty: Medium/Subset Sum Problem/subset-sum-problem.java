class Solution {
    static Boolean isSubsetSum(int arr[], int target) {
        int n=arr.length;
        boolean [] prev=new boolean[target+1];
        boolean [] curr=new boolean[target+1];
        prev[0]=curr[0]=true;
        if (arr[0] <= target) prev[arr[0]] = true;
        for(int i=1;i<n;i++){
            for(int j=1;j<target+1;j++){
                boolean notTake=prev[j];
                boolean take=false;
                if(j>=arr[i])take=prev[j-arr[i]];
                curr[j]= take||notTake;
            }
            prev=curr.clone();
        }
        return prev[target];
    }
}

