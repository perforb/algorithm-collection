package fibonacci;

public class DynamicProgramming {

  public static void main(String[] args) {
    int answer = fibonacci(10);
    System.out.println(answer);
  }

  private static int fibonacci(int n) {
    int[] a = new int[n + 1];
    a[0] = 0;
    a[1] = 1;
    if (n == 0) {
      return a[0];
    } else if (n == 1) {
      return a[1];
    }
    for (int i = 2; i <= n; i++) {
      a[i] = a[i - 1] + a[i - 2];
    }
    return a[n];
  }
}
