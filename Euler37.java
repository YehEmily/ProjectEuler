public class Euler37 {
  
  private int count;
  
  public Euler37 () {
    count = 0;
  }
  
  public int truncatablePrimesSum () {
    int sum = 0;
    int candidate = 13;
    
    while (count < 11) {
      if (isPrimeL(candidate) && isPrimeR(candidate)) {
        count++;
        sum += candidate;
        System.out.println(candidate);
      }
      candidate++;
    }
    return sum;
  }
  
  private boolean isPrimeL (int n) {
    while (n > 0) {
      if (!isPrime(n)) return false;
      n = truncate(n, "Left");
    }
    return true;
  }
  
  private boolean isPrimeR (int n) {
    while (n > 0) {
      if (!isPrime(n)) return false;
      n = truncate(n, "Right");
    }
    return true;
  }
  
  private boolean isPrime (int n) {
    if (n == 1) return false;
    if (n == 2) return true;
    if (n % 2 == 0) return false;
    for (int i = 3; i * i <= n; i += 2) {
      if (n % i == 0) return false;
    }
    return true;
  }
  
  private int truncate (int n, String direction) {
    try {
      char[] characters = Integer.toString(n).toCharArray();
      char[] truncated = new char[characters.length-1];
      
      if (direction.equals("Left")) {
        for (int i = 1; i < characters.length; i++) {
          truncated[i-1] = characters[i];
        }
      } else if (direction.equals("Right")) {
        for (int i = 0; i < characters.length-1; i++) {
          truncated[i] = characters[i];
        }
      }
      return Integer.parseInt(String.valueOf(truncated));
    } catch (NumberFormatException e) {
      return -1;
    }
  }
  
  public static void main (String[] args) {
    Euler37 test = new Euler37();
    System.out.println(test.truncatablePrimesSum());
  }
}