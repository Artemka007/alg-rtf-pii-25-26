import java.io.BufferedReader;
import java.io.InputStreamReader;

public class task13 {
    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(reader.readLine().trim());
        System.out.println(solution(N) == 0 ? "First" : "Second");
    }

    public static int solution(int N) {
        int[] dp = new int[N + 1];
        int[] prefix = new int[N + 1];

        prefix[0] = 1;

        for (int i = 1; i <= N; i++) {
            int maxTake = (int) Math.sqrt(i);
            int step = i - maxTake;
            int prev = prefix[i - 1];
            int base = (step > 0) ? prefix[step - 1] : 0;
            int loseCount = prev - base;
            if (loseCount > 0) {
                dp[i] = 1;
                prefix[i] = prev;
            } else {
                dp[i] = 0;
                prefix[i] = prev + 1;
            }
        }

        return dp[N];
    }
}
