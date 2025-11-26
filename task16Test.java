
import java.math.BigInteger;

public class task16Test {
    static class TestCase13 implements TestUtils.TestCaseBigInteger {
        int N, M;
        BigInteger expected;
        TestCase13(int N, int M, BigInteger expected) {
            this.N = N;
            this.M = M;
            this.expected = expected;
        }
        @Override
        public BigInteger getExpected() {
            return expected;
        }
    }

    public static void main(String[] args) {
        TestCase13[] testCases = {
            new TestCase13(6, 10, new BigInteger("55252")),
            new TestCase13(28, 12, new BigInteger("35806106077437501422929813320")),
            new TestCase13(150, 26, new BigInteger("764485668472672515783170878043956732152720687894642666768747230247757616459696029541313522686204640386790673053169884153974150844585472693651836254864072430874661109483949943146902450151006126136010441648944656")),
        };

        TestUtils.printHeader("Task13 Performance Test", "N", "Expected", "Result", "Time (ms)", "Memory (MB)", "Status");

        int passed = 0;
        for (TestCase13 tc : testCases) {
            TestUtils.TestResult result = TestUtils.runTest(tc, () -> task16.solution(tc.N, tc.M));
            if (result.passed) passed++;
            TestUtils.printResult(tc.N, tc.expected, task16.solution(tc.N, tc.M), result.timeMs, result.memoryMB, result.passed);
        }

        TestUtils.printSummary(passed, testCases.length);
    }
}
