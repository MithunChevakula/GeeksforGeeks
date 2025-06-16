class Solution {
    public int kthSmallest(int[] arr, int k) {
        int low = Arrays.stream(arr).min().getAsInt();
        int high = Arrays.stream(arr).max().getAsInt();

        while (low <= high) {
            int mid = low + (high - low) / 2;
            int count = countLessThanOrEqual(arr, mid);

            if (count < k) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }

        return low;
    }

    private int countLessThanOrEqual(int[] arr, int val) {
        int count = 0;
        for (int num : arr) {
            if (num <= val) {
                count++;
            }
        }
        return count;
    }
}


