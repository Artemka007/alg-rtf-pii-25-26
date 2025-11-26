import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;

public class task16 {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String[] data = reader.readLine().trim().split(" ");
        int N = Integer.parseInt(data[0]);
        int M = Integer.parseInt(data[1]);
        BigInteger result = solution(N, M);
        System.out.println(result);
    }

    public static BigInteger solution(int N, int M) {
        int halfLen = N / 2;
        int len1 = halfLen / 2;
        int len2 = halfLen - len1;
        
        BigInteger[] part1 = computeDistribution(len1, M);
        BigInteger[] part2 = computeDistribution(len2, M);
        
        int maxSum1 = len1 * (M - 1);
        int maxSum2 = len2 * (M - 1);
        int maxHalfSum = halfLen * (M - 1);
        
        BigInteger[] half = new BigInteger[maxHalfSum + 1];
        for (int i = 0; i <= maxHalfSum; i++) {
            half[i] = BigInteger.ZERO;
        }
        
        for (int s1 = 0; s1 <= maxSum1; s1++) {
            for (int s2 = 0; s2 <= maxSum2; s2++) {
                int sum = s1 + s2;
                if (sum <= maxHalfSum) {
                    half[sum] = half[sum].add(part1[s1].multiply(part2[s2]));
                }
            }
        }
        
        BigInteger total = BigInteger.ZERO;
        for (int s = 0; s <= maxHalfSum; s++) {
            total = total.add(half[s].multiply(half[s]));
        }
        return total;
    }
    
    private static BigInteger[] computeDistribution(int length, int M) {
        if (length == 0) {
            return new BigInteger[]{ BigInteger.ONE };
        }
        int maxSum = length * (M - 1);
        BigInteger[] dp = new BigInteger[maxSum + 1];
        for (int i = 0; i <= maxSum; i++) {
            dp[i] = BigInteger.ZERO;
        }
        dp[0] = BigInteger.ONE;
        
        for (int pos = 0; pos < length; pos++) {
            BigInteger[] newDp = new BigInteger[maxSum + 1];
            for (int i = 0; i <= maxSum; i++) {
                newDp[i] = BigInteger.ZERO;
            }
            for (int sum = 0; sum <= maxSum; sum++) {
                if (dp[sum].compareTo(BigInteger.ZERO) > 0) {
                    for (int digit = 0; digit < M; digit++) {
                        int newSum = sum + digit;
                        if (newSum <= maxSum) {
                            newDp[newSum] = newDp[newSum].add(dp[sum]);
                        }
                    }
                }
            }
            dp = newDp;
        }
        return dp;
    }
}