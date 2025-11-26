import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class task5 {
  public static String solution(int N, int M) {
        if (N == 0) {
            return "0";
        }
        if (M == 0) {
            return "0";
        }
        
        StringBuilder sign = new StringBuilder();
        if ((N < 0) != (M < 0)) {
            sign.append("-");
        }
        long num = Math.abs((long) N);
        long den = Math.abs((long) M);
        
        long integerPart = num / den;
        long remainder = num % den;
        
        if (remainder == 0) {
            return sign.toString() + integerPart;
        }
        
        List<String> result = new ArrayList<>();
        Map<Long, Integer> remainders = new HashMap<>();
        int position = 0;
        
        while (remainder != 0) {
            if (remainders.containsKey(remainder)) {
                List<String> nonRepeating = result.subList(0, remainders.get(remainder));
                List<String> repeating = result.subList(remainders.get(remainder), result.size());
                
                StringBuilder decimalPart = new StringBuilder();
                for (String digit : nonRepeating) {
                    decimalPart.append(digit);
                }
                decimalPart.append("(");
                for (String digit : repeating) {
                    decimalPart.append(digit);
                }
                decimalPart.append(")");
                
                if (integerPart == 0) {
                    return sign.toString() + "0." + decimalPart.toString();
                } else {
                    return sign.toString() + integerPart + "." + decimalPart.toString();
                }
            }
            
            remainders.put(remainder, position);
            
            remainder *= 10;
            long digit = remainder / den;
            result.add(String.valueOf(digit));
            remainder %= den;
            position++;
        }
        
        StringBuilder decimalPart = new StringBuilder();
        for (String digit : result) {
            decimalPart.append(digit);
        }
        
        if (integerPart == 0) {
            return sign.toString() + "0." + decimalPart.toString();
        } else {
            return sign.toString() + integerPart + "." + decimalPart.toString();
        }
    }
    
    public static void main(String[] args) throws IOException {
      try (BufferedReader reader = new BufferedReader(new InputStreamReader(System.in))) {
          String[] input = reader.readLine().split(" ");
          int N = Integer.parseInt(input[0]);
          int M = Integer.parseInt(input[1]);
          System.out.println(solution(N, M));
      }
    }
}
