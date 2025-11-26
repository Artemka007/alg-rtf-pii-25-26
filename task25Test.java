import java.io.*;
import java.util.Random;

public class task25Test {
    static class TestCase25 implements TestUtils.TestCase {
        int N, M;
        int[][] matrix;
        int expected;
        TestCase25(int N, int M, int[][] matrix, int expected) {
            this.N = N;
            this.M = M;
            this.matrix = matrix;
            this.expected = expected;
        }
        @Override
        public int getExpected() {
            return expected;
        }
    }

    public static void main(String[] args) {
        // Test cases: [N, M, matrix, expected result]
        Random random = new Random();
        int[][] matrix = new int[1000][1000];
        
        for (int i = 0; i < 1000; i++) {
            for (int j = 0; j < 1000; j++) {
                matrix[i][j] = random.nextInt(1000) + 1; // от 1 до 1000
            }
        }

        TestCase25[] testCases = {
            new TestCase25(2, 2, new int[][]{{1, 2}, {3, 4}}, 4),
            new TestCase25(3, 3, new int[][]{{0, 1, 2}, {1, 2, 3}, {2, 3, 4}}, 4),
            new TestCase25(3, 5, new int[][]{{3, 1, 4, 1, 5}, {9, 2, 6, 5, 3}, {5, 9, 7, 9, 3}}, 1),
            new TestCase25(1000, 1000, matrix, 5),
        };

        TestUtils.printHeader("Task25 Performance Test", "N", "M", "Expected", "Result", "Time (ms)", "Memory (MB)", "Status");

        int passed = 0;
        for (TestCase25 tc : testCases) {
            TestUtils.TestResult result = TestUtils.runTest(tc, () -> {
                try {
                    java.io.ByteArrayInputStream in = new java.io.ByteArrayInputStream(generateInput(tc).getBytes());
                    System.setIn(in);
                    java.io.BufferedReader reader = new java.io.BufferedReader(new java.io.InputStreamReader(System.in));
                    return task25.solution(reader, tc.N, tc.M);
                } catch (IOException e) {
                    throw new RuntimeException("IO error in test", e);
                }
            });
            if (result.passed) passed++;
            
            // Для вывода результата создаем отдельный reader
            try {
                ByteArrayInputStream in = new ByteArrayInputStream(generateInput(tc).getBytes());
                System.setIn(in);
                BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
                int actualResult = task25.solution(reader, tc.N, tc.M);
                TestUtils.printResult(tc.N + ", " + tc.M, tc.expected, actualResult, result.timeMs, result.memoryMB, result.passed);
            } catch (IOException e) {
                System.err.println("IO error: " + e.getMessage());
                TestUtils.printResult(tc.N + ", " + tc.M, tc.expected, -1, result.timeMs, result.memoryMB, false);
            }
        }

        TestUtils.printSummary(passed, testCases.length);
    }

    private static String generateInput(TestCase25 tc) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < tc.N; i++) {
            for (int j = 0; j < tc.M; j++) {
                sb.append(tc.matrix[i][j]);
                if (j < tc.M - 1) sb.append(" ");
            }
            sb.append("\n");
        } 
        return sb.toString();
    }
}