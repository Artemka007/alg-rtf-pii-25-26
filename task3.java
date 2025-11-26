import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class task3 {
    
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String[] data = reader.readLine().trim().split(" ");
        int L = Integer.parseInt(data[0]);
        int N = Integer.parseInt(data[1]);

        String[] pointsStr = reader.readLine().trim().split(" ");
        
        int[] points = new int[N];
        for (int i = 0; i < N; i++) {
            points[i] = Integer.parseInt(pointsStr[i]);
        }
        
        int result = solution(L, N, points);
        System.out.println(result);
    }
    
    public static int solution(int L, int N, int[] points) {
        QuickSort.quickSort(points);
        
        int count = 1;
        long currentEnd = (long) points[0] + L;
        
        for (int i = 1; i < N; i++) {
            if (points[i] >= currentEnd) {
                count++;
            }
            currentEnd = (long) points[i] + L;
        }
        
        return count;
    }
}
