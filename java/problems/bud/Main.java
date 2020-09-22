import static java.lang.Math.pow;

public class Main {

  public static void main(String[] args) {
    int n = 10;
    solve(n);
  }

  /**
   * a^3 + b^3 == c^3 + d^3
   */
  public static void solve(int n) {
    for (int a = 1; a <= n; a++) {
      for (int b = 1; b <= n; b++) {
        for (int c = 1; c <= n; c++) {
          for (int d = 1; d <= n; d++) {
            if (pow(a, 3) + pow(b, 3) == pow(c, 3) + pow(d, 3)) {
              System.out.printf("%d, %d, %d, %d\n", a, b, c, d);
            }
          }
        }
      }
    }
  }

  public static void solve2(int n) {
    for (int a = 1; a <= n; a++) {
      for (int b = 1; b <= n; b++) {
        for (int c = 1; c <= n; c++) {
          int d = (int) pow(pow(a, 3) + pow(b, 3) + pow(c, 3), (double) 1 / 3);
          if (pow(a, 3) + pow(b, 3) == pow(c, 3) + pow(d, 3) && 0 <= d && d <= n) {
            System.out.printf("%d, %d, %d, %d\n", a, b, c, d);
          }
        }
      }
    }
  }
}
