package fibonacci;

public class Recursive {

  public static void main(String[] args) {
    int answer = fibonacci(10);
    System.out.println(answer);
  }

  private static int fibonacci(int n) {
    if (n == 0) {
      return 0;
    } else if (n == 1) {
      return 1;
    }
    return fibonacci(n - 1) + fibonacci(n - 2);
  }
}
