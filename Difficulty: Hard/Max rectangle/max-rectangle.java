class Solution {
    // Returns area of the largest rectangle with all 1s in mat[][]
    static int maxArea(int mat[][]) {
        int n = mat.length;
        int m = mat[0].length;
        int ans = Integer.MIN_VALUE;
        int[] dp = new int[m];
        for(int i =0; i < n; i++) {
            for(int j =0; j < m; j++) {
                dp[j] = mat[i][j] != 0 ? dp[j] + mat[i][j] : 0;
            }
            ans = Math.max(ans, getMaxArea(dp));
        }
        return ans;
    }
    
    static int getMaxArea(int[] arr) {
        int n = arr.length;
        Stack<Integer> stack = new Stack<>();
        int[] leftPrev = new int[n];
        int[] rightPrev = new int[n];
        
        for(int i =0; i < n; i++) {
            while(!stack.isEmpty() && arr[stack.peek()] >= arr[i]) {
                stack.pop();
            }
            leftPrev[i] = stack.isEmpty() ? 0 : stack.peek() + 1;
            stack.push(i);
        }
        stack.clear();
        
        for(int i =n-1; i >= 0; i--) {
            while(!stack.isEmpty() && arr[stack.peek()] >= arr[i]) {
                stack.pop();
            }
            rightPrev[i] = stack.isEmpty() ? n-1 : stack.peek() - 1;
            stack.push(i);
        }
        // System.out.println(Arrays.toString(leftPrev));
        // System.out.println(Arrays.toString(rightPrev));
        int maxArea = Integer.MIN_VALUE;
        for(int i =0; i < n; i++) {
           maxArea = Math.max(maxArea, (rightPrev[i] - leftPrev[i] + 1) * arr[i]); 
        }
        return maxArea;
        
    }
}