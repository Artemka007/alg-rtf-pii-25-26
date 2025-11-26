import java.util.Arrays;
import java.util.List;

public class task3Test {
    // Тестовые случаи для обычных чисел
    static class task3TestCase implements TestUtils.TestCase {
        public int L;
        public int N;
        public int[] points;
        public int expected;
        
        public task3TestCase(int L, int N, int[] points, int expected) {
            this.L = L;
            this.N = N;
            this.points = points;
            this.expected = expected;
        }
        
        @Override
        public int getExpected() {
            return expected;
        }
    }

    
    public static void main(String[] args) {
        runtask3Tests();
    }
    
    public static void runtask3Tests() {
        System.out.println("=== Quick Sort Solution Tests ===");

        int[] t = new int[(int)1e5];
        for (int i = 0; i < (int)1e5; i++) {
            t[i] = (int) (1e9);
        }
        
        // Подготовка тестовых данных
        List<task3Test.task3TestCase> testCases = Arrays.asList(
            new task3Test.task3TestCase(0, 1, new int[]{100}, 1),
            new task3Test.task3TestCase(100, 1, new int[]{-1000}, 1),
            new task3Test.task3TestCase(1, 2, new int[]{0, 1}, 1),
            new task3Test.task3TestCase(1, 2, new int[]{0, 2}, 2),
            
            new task3Test.task3TestCase(100000000, 3, 
                new int[]{-1000000000, 0, 1000000000}, 3),
            new task3Test.task3TestCase(500000000, 3, 
                new int[]{-1000000000, 0, 1000000000}, 2),
            new task3Test.task3TestCase(10, 5, 
                new int[]{30, 3, 14, 19, 21}, 2),
            new task3Test.task3TestCase((int)1e8, (int)1e5, 
                t, 2)
        );
        
        // Заголовок таблицы
        TestUtils.printHeader("Quick Sort Algorithm Tests", 
            "Test #", "Expected", "Result", "Time(ms)", "Memory(MB)", "Status");
        
        for (task3TestCase tc : testCases) {
            TestUtils.TestResult result = TestUtils.runTest(tc, () -> task3.solution(tc.L, tc.N, tc.points));
            TestUtils.printResult(tc.N, tc.expected, task3.solution(tc.L, tc.N, tc.points), result.timeMs, result.memoryMB, result.passed);
        }
        
    }
}
