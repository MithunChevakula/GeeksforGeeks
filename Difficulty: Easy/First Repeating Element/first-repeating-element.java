class Solution {
    public static int firstRepeated(int[] arr) {
        // code here
          HashSet<Integer> mp = new HashSet<>();

    int ele = Integer.MAX_VALUE;
    for (int i = arr.length - 1; i >= 0; i--) {
        if (mp.contains(arr[i])) {
            ele = Math.min(ele, i);
        }
        mp.add(arr[i]);
    }

    return ele == Integer.MAX_VALUE ? -1 : ele+1;
    }
}

