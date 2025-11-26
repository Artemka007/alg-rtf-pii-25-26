import java.util.*;
import java.io.*;

public class task5Test {
    
    // Базовый класс для тестовых случаев
    static class TestCase {
        int N;
        int M;
        String expected;
        
        TestCase(int N, int M, String expected) {
            this.N = N;
            this.M = M;
            this.expected = expected;
        }
    }
    
    // Утилиты для тестирования
    static class TestUtils {
        static class TestResult {
            boolean passed;
            long timeMs;
            double memoryMB;
            
            TestResult(boolean passed, long timeMs, double memoryMB) {
                this.passed = passed;
                this.timeMs = timeMs;
                this.memoryMB = memoryMB;
            }
        }
        
        public static TestResult runTest(TestCase tc, Runnable test) {
            Runtime runtime = Runtime.getRuntime();
            System.gc();
            long startMemory = runtime.totalMemory() - runtime.freeMemory();
            long startTime = System.currentTimeMillis();
            
            boolean passed = false;
            try {
                test.run();
                passed = true;
            } catch (Exception e) {
                passed = false;
            }
            
            long endTime = System.currentTimeMillis();
            long endMemory = runtime.totalMemory() - runtime.freeMemory();
            long memoryUsed = endMemory - startMemory;
            double memoryMB = memoryUsed / (1024.0 * 1024.0);
            
            return new TestResult(passed, endTime - startTime, memoryMB);
        }
        
        public static void printHeader(String testName, String... columns) {
            System.out.println("\n" + "=".repeat(100));
            System.out.println(testName);
            System.out.println("-".repeat(100));
            System.out.printf("%-15s %-40s %-20s %-10s %-12s %s%n", 
                (Object[]) columns);
            System.out.println("-".repeat(100));
        }
        
        public static void printResult(int input, String expected, String actual, 
                                     long timeMs, double memoryMB, boolean passed) {
            String status = passed ? "PASS" : "FAIL";
            String colorStart = passed ? "" : "\u001B[31m";
            String colorEnd = passed ? "" : "\u001B[0m";
            
            System.out.printf("%-15d %-40s %-20s %-10d %-12.2f %s%s%s%n",
                input, 
                expected.length() > 40 ? expected.substring(0, 37) + "..." : expected,
                actual.length() > 20 ? actual.substring(0, 17) + "..." : actual,
                timeMs,
                memoryMB,
                colorStart, status, colorEnd);
        }
        
        public static void printSummary(int passed, int total) {
            System.out.println("-".repeat(100));
            double percentage = (double) passed / total * 100;
            System.out.printf("Summary: %d/%d tests passed (%.1f%%)%n", passed, total, percentage);
            System.out.println("=".repeat(100));
        }
    }
    
    public static void runEdgeCaseTests() {
        TestCase[] edgeCases = {
            new TestCase(0, 1, "0"),
            new TestCase(0, 100, "0"),
            new TestCase(1, 1, "1"),
            new TestCase(999999, 1000000, "0.999999"),
            new TestCase(1, 100000000, "0.00000001"),
            new TestCase(149999999, 150000000, "0.9(999999993333333)") // Почти 1
        };
        
        TestUtils.printHeader("Task5 Edge Cases", "Input N/M", "Expected", "Result", "Time (ms)", "Memory (MB)", "Status");
        
        int passed = 0;
        for (TestCase tc : edgeCases) {
            String actual = task5.solution(tc.N, tc.M);
            boolean testPassed = actual.equals(tc.expected);
            
            TestUtils.TestResult result = TestUtils.runTest(tc, () -> {
                task5.solution(tc.N, tc.M);
            });
            
            if (testPassed) passed++;
            TestUtils.printResult(tc.N, tc.expected, actual, result.timeMs, result.memoryMB, testPassed);
        }
        
        TestUtils.printSummary(passed, edgeCases.length);
    }
    
    public static void main(String[] args) {
        System.out.println("Task 5 Tests - Periodic Decimal Fraction");
        System.out.println("Testing conversion of N/M to decimal representation with repeating periods");
        
        // Запускаем различные типы тестов
        runEdgeCaseTests();
        
        // Дополнительная проверка на специфические случаи
        System.out.println("\nAdditional Validation Tests:");
        validateSpecificCases();
    }
    
    private static void validateSpecificCases() {
        // Проверка конкретных известных периодов
        Map<String, String> knownPeriods = Map.of(
            "1/3", "0.(3)",
            "1/7", "0.(142857)",
            "1/81", "0.(012345679)",
            "1/97", "0.(010309278350515463917525773195876288659793814432989690721649484536082474226804123711340206185567)"
        );
        
        int correct = 0;
        for (var entry : knownPeriods.entrySet()) {
            String[] parts = entry.getKey().split("/");
            int N = Integer.parseInt(parts[0]);
            int M = Integer.parseInt(parts[1]);
            String expected = entry.getValue();
            String actual = task5.solution(N, M);
            
            if (actual.equals(expected)) {
                System.out.println("✓ " + entry.getKey() + " = " + actual);
                correct++;
            } else {
                System.out.println("✗ " + entry.getKey() + " = " + actual + " (expected: " + expected + ")");
            }
        }
        System.out.println("Period validation: " + correct + "/" + knownPeriods.size() + " correct");
    }
}