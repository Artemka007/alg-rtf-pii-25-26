public class task24Test {
    static class TestCase25 implements TestUtils.TestCase {
        int N, M, K, L, expected;
        TestCase25(int N, int M, int K, int L, int expected) {
            this.N = N;
            this.M = M;
            this.K = K;
            this.L = L;
            this.expected = expected;
        }
        @Override
        public int getExpected() {
            return expected;
        }
    }

    public static void main(String[] args) {
        // Test cases: [N, M, K, L, expected]
        TestCase25[] testCases = {
            new TestCase25(2, 1, 1, 1, 1),
            new TestCase25(3, 1, 1, 2, 1),
            new TestCase25(5, 3, 2, 4, 3),
            new TestCase25(10, 7, 5, 3, 1),
            new TestCase25(20, 2, 3, 15, 2),
            new TestCase25(100, 50, 40, 75, -1),
            new TestCase25(1000, 600, 400, 123, -1),
            new TestCase25(1000, 600, 400, 900, -1)
        };

        TestUtils.printHeader("Task25 Performance Test", "Input", "Expected", "Result", "Time (ms)", "Memory (MB)", "Status");

        int passed = 0;
        for (TestCase25 tc : testCases) {
            TestUtils.TestResult result = TestUtils.runTest(tc, () -> task24.solution(tc.N, tc.M, tc.K, tc.L));
            if (result.passed) passed++;
            int actualResult = task24.solution(tc.N, tc.M, tc.K, tc.L);
            System.out.printf("(%d,%d,%d,%d) %-10d %-12d %-15d %-20s %s%n",
                    tc.N, tc.M, tc.K, tc.L, tc.expected, actualResult, result.timeMs, 
                    String.format("%.4f MB", result.memoryMB), result.passed ? "✓ PASS" : "✗ FAIL");
        }

        TestUtils.printSummary(passed, testCases.length);
    }
}
