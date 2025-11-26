public class QuickSort {
    public static void quickSort(int[] arr) {
        if (arr == null || arr.length <= 1) {
            return;
        }
        
        int[] stack = new int[arr.length * 2];
        int top = -1;
        
        stack[++top] = 0;
        stack[++top] = arr.length - 1;
        
        while (top >= 0) {
            int high = stack[top--];
            int low = stack[top--];
            
            int pivotIndex = partition(arr, low, high);
            
            if (pivotIndex - 1 > low) {
                stack[++top] = low;
                stack[++top] = pivotIndex - 1;
            }
            
            if (pivotIndex + 1 < high) {
                stack[++top] = pivotIndex + 1;
                stack[++top] = high;
            }
        }
    }
    
    private static int partition(int[] arr, int low, int high) {
        int pivot = arr[high];
        int i = low - 1;
        
        for (int j = low; j < high; j++) {
            if (arr[j] <= pivot) {
                i++;
                swap(arr, i, j);
            }
        }
        
        swap(arr, i + 1, high);
        return i + 1;
    }
    
    private static void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}