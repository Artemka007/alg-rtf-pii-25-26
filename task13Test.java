public class task13Test {
    static class TestCase13 implements TestUtils.TestCase {
        int N, expected;
        TestCase13(int N, int expected) {
            this.N = N;
            this.expected = expected;
        }
        @Override
        public int getExpected() {
            return expected;
        }
    }

    public static void main(String[] args) {
        // Test cases: [N, expected result (0 or 1)]
        TestCase13[] testCases = {
            new TestCase13(1, 0),
            new TestCase13(2, 1),
            new TestCase13(3, 1),
            new TestCase13(4, 1),
            new TestCase13(5, 0),
            new TestCase13(10, 1),
            new TestCase13(100, 1),
            new TestCase13(1000, 0),
            new TestCase13(10000, 1),
            new TestCase13(1000000, 0)
        };

        TestUtils.printHeader("Task13 Performance Test", "N", "Expected", "Result", "Time (ms)", "Memory (MB)", "Status");

        int passed = 0;
        for (TestCase13 tc : testCases) {
            TestUtils.TestResult result = TestUtils.runTest(tc, () -> task13.solution(tc.N));
            if (result.passed) passed++;
            TestUtils.printResult(tc.N, tc.expected, task13.solution(tc.N), result.timeMs, result.memoryMB, result.passed);
        }

        TestUtils.printSummary(passed, testCases.length);
    }
}
