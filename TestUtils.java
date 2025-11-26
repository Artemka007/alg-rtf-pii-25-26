import java.math.BigInteger;

public class TestUtils {
    public static class TestResult {
        public long timeMs;
        public double memoryMB;
        public boolean passed;

        public TestResult(long timeMs, double memoryMB, boolean passed) {
            this.timeMs = timeMs;
            this.memoryMB = memoryMB;
            this.passed = passed;
        }
    }

    public static TestResult runTest(TestCase testCase, TestExecutor executor) {
        Runtime runtime = Runtime.getRuntime();
        long memBefore = runtime.totalMemory() - runtime.freeMemory();

        long startTime = System.nanoTime();
        int result = executor.execute();
        long endTime = System.nanoTime();

        long memAfter = runtime.totalMemory() - runtime.freeMemory();

        long timeMs = (endTime - startTime) / 1_000_000;
        long memUsedBytes = memAfter - memBefore;
        double memUsedMB = memUsedBytes / (1024.0 * 1024.0);

        boolean isCorrect = (result == testCase.getExpected());

        return new TestResult(timeMs, memUsedMB, isCorrect);
    }

    public static TestResult runTest(TestCaseBigInteger testCase, TestExecutorBigInteger executor) {
        Runtime runtime = Runtime.getRuntime();
        long memBefore = runtime.totalMemory() - runtime.freeMemory();

        long startTime = System.nanoTime();
        BigInteger result = executor.execute();
        long endTime = System.nanoTime();

        long memAfter = runtime.totalMemory() - runtime.freeMemory();

        long timeMs = (endTime - startTime) / 1_000_000;
        long memUsedBytes = memAfter - memBefore;
        double memUsedMB = memUsedBytes / (1024.0 * 1024.0);

        boolean isCorrect = (result.equals(testCase.getExpected()));

        return new TestResult(timeMs, memUsedMB, isCorrect);
    }

    public static void printHeader(String testName, String... columns) {
        System.out.println(testName + "\n");
        StringBuilder format = new StringBuilder();
        for (String column : columns) {
            format.append("%-15s ");
        }
        System.out.printf(format.toString() + "%n", (Object[]) columns);
        System.out.println("-".repeat(80));
    }

    public static void printResult(int testNum, int expected, int result, long timeMs, double memMB, boolean passed) {
        String status = passed ? "✓ PASS" : "✗ FAIL";
        System.out.printf("%-15d %-15d %-15d %-15d %-20s %s%n",
                testNum, expected, result, timeMs, String.format("%.4f MB", memMB), status);
    }

    public static void printResult(int testNum, BigInteger expected, BigInteger result, long timeMs, double memMB, boolean passed) {
        String status = passed ? "✓ PASS" : "✗ FAIL";
        System.out.printf("%-15d %-15d %-15d %-15d %-20s %s%n",
                testNum, expected, result, timeMs, String.format("%.4f MB", memMB), status);
    }

    public static void printResult(String testNum, int expected, int result, long timeMs, double memMB, boolean passed) {
        String status = passed ? "✓ PASS" : "✗ FAIL";
        System.out.printf("%s %-15d %-15d %-15d %-20s %s%n",
                testNum, expected, result, timeMs, String.format("%.4f MB", memMB), status);
    }

    public static void printSummary(int passed, int total) {
        System.out.println("-".repeat(80));
        System.out.printf("Tests passed: %d/%d\n", passed, total);
    }

    public interface TestCase {
        int getExpected();
    }

    public interface TestCaseBigInteger {
        BigInteger getExpected();
    }

    public interface TestExecutor {
        int execute();
    }

    public interface TestExecutorBigInteger {
        BigInteger execute();
    }
}
