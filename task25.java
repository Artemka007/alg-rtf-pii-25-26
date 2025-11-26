import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class task25 {
    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String[] data = reader.readLine().trim().split(" ");
        int N = Integer.parseInt(data[0]);
        int M = Integer.parseInt(data[1]);

        int result = solution(reader, N, M);
        System.out.println(result);
    }

    public static int solution(BufferedReader reader, int N, int M) throws IOException {
        int[][] resultMatrix = new int[N][M];
        for (int i = 0; i < N; i++) {
            String[] rowData = reader.readLine().trim().split(" ");
            for (int j = 0; j < M; j++) {
                if (j == 0 && i == 0) {
                    resultMatrix[0][0] = Integer.parseInt(rowData[j]);
                    continue;
                }
                if (j == 0) {
                    int topValue = resultMatrix[i - 1][j];
                    int currentValue = Integer.parseInt(rowData[j]);
                    resultMatrix[i][j] = Math.max(topValue, currentValue);
                    continue;
                }
                if (i == 0) {
                    int leftValue = resultMatrix[i][j - 1];
                    int currentValue = Integer.parseInt(rowData[j]);
                    resultMatrix[i][j] = Math.max(leftValue, currentValue);
                    continue;
                }
                int leftValue = resultMatrix[i][j - 1];
                int topValue = resultMatrix[i - 1][j];
                int currentValue = Integer.parseInt(rowData[j]);

                int fromLeft = Math.max(leftValue, currentValue);
                int fromTop = Math.max(topValue, currentValue);

                resultMatrix[i][j] = Math.min(fromLeft, fromTop);
            }
        }

        return resultMatrix[N - 1][M - 1];
    }
}