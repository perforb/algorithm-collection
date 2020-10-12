package fibonacci;

import java.util.HashMap;
import java.util.Map;

public class Memo {

  private final Map<Integer, Integer> memo;

  private Memo() {
    this.memo = new HashMap<>();
    memo.put(0, 0);
    memo.put(1, 1);
  }

  public static void main(String[] args) {
    int answer = new Memo().fibonacci(10);
    System.out.println(answer);
  }

  private int fibonacci(int n) {
    if (memo.containsKey(n)) {
      return memo.get(n);
    }
    memo.put(n, fibonacci(n - 1) + fibonacci(n - 2));
    return memo.getOrDefault(n, 0);
  }
}
