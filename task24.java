import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.function.BiConsumer;

public class task24 {
    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String[] data = reader.readLine().trim().split(" ");
        int N = Integer.parseInt(data[0]);
        int M = Integer.parseInt(data[1]);
        int K = Integer.parseInt(data[2]);
        int L = Integer.parseInt(data[3]);

        int result = solution(N, M, K, L);
        if (result != -1) {
            System.out.println(result);
        } else {
            System.out.println("OOPS");
        }
    }

    public static int solution(int N, int M, int K, int L) {
        Deque<int[]> queue = new ArrayDeque<>();
        int[][] visited = new int[M + 1][K + 1];

        for (int i = 0; i <= M; i++) {
            for (int j = 0; j <= K; j++) {
                visited[i][j] = -1;
            }
        }

        queue.addLast(new int[]{0, 0});
        visited[0][0] = 0;

        while (!queue.isEmpty()) {
            int[] state = queue.removeFirst();
            int b = state[0];
            int c = state[1];
            int a = N - b - c;
            int step = visited[b][c];

            BiConsumer<Integer, Integer> pushNext = (newB, newC) -> {
                if (visited[newB][newC] == -1) {
                    visited[newB][newC] = step + 1;
                    queue.add(new int[]{newB, newC});
                }
            };

            if (a == L) {
                return step;
            }

            if (a > 0 && b < M) {
                int transfer = Math.min(a, M - b);
                if (transfer == M - b) {
                    pushNext.accept(M, c);
                }
                if (transfer == a) {
                    pushNext.accept(b + a, c);
                }
            }

            if (a > 0 && c < K) {
                int transfer = Math.min(a, K - c);
                if (transfer == K - c) {
                    pushNext.accept(b, K);
                }
                if (transfer == a) {
                    pushNext.accept(b, c + a);
                }
            }

            if (b > 0 && a < N) {
                int transfer = Math.min(b, N - a);
                if (transfer == b) {
                    pushNext.accept(0, c);
                }
                if (transfer == N - a) {
                    pushNext.accept(b - (N - a), c);
                }
            }

            if (b > 0 && c < K) {
                int transfer = Math.min(b, K - c);
                if (transfer == b) {
                    pushNext.accept(0, c + b);
                }
                if (transfer == K - c) {
                    pushNext.accept(b - (K - c), K);
                }
            }

            if (c > 0 && a < N) {
                int transfer = Math.min(c, N - a);
                if (transfer == c) {
                    pushNext.accept(b, 0);
                }
                if (transfer == N - a) {
                    pushNext.accept(b, c - (N - a));
                }
            }

            if (c > 0 && b < M) {
                int transfer = Math.min(c, M - b);
                if (transfer == c) {
                    pushNext.accept(b + c, 0);
                }
                if (transfer == M - b) {
                    pushNext.accept(M, c - (M - b));
                }
            }
        }
        return -1;
    }
}