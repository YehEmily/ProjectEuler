public class Euler27 {
  
  private int largest_so_far; // Largest number of consecutive primes
  
  public Euler27() {
    largest_so_far = 0;
  }
  
  public int quad_primes() {
    int max_a = 0;
    int max_b = 0;
    
    for (int a = -999; a < 1000; a++) {
      for (int b = -1000; b < 1000; b++) {
        int n = 0;
        while (isPrime(n*n + a*n + b)) {
          n++;
        }
        if (n > largest_so_far) {
          largest_so_far = n;
          max_a = a;
          max_b = b;
        }
      }
    }
    System.out.println(largest_so_far); // Let's see what the largest number of consecutive primes is
    return max_a*max_b; // Return the product
  }
  
  public static boolean isPrime(int num) {
    for (int i = 2; i<= num/i; i++) {
      if (num % i == 0) {
        return false;
      }
    }
    return num > 1;
  }

      
  public static void main(String [] args) {
    Euler27 solution = new Euler27();
    System.out.println(solution.quad_primes());
  }
}