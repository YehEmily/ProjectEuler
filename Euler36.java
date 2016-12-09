import java.util.*;

public class Euler36 {
  
  public Euler36 () {
  }
  
  public int findPalindromes () {
    int sum = 0;
    for (int i = 0; i < 1000000; i++) {
      if (isPalindrome_10(i) && isPalindrome_2(i)) {
        sum += i;
      }
    }
    return sum;
  }
  
  private boolean isPalindrome_10 (int n) {
    char[] digits_10 = Integer.toString(n).toCharArray();
    Stack<Character> stack_10 = new Stack<Character>();
    
    for (int i = 0; i < digits_10.length; i++) {
      stack_10.push(digits_10[i]);
    }
    
    for (int i = 0; i < digits_10.length; i++) {
      digits_10[i] = stack_10.pop();
    }
    
    int reverse_n = Integer.parseInt(String.valueOf(digits_10));
    if (reverse_n == n) return true;
    return false;
  }
  
  private boolean isPalindrome_2 (int n) {
    String binaryString = Integer.toBinaryString(n);
    char[] digits_2 = binaryString.toCharArray();
    Stack<Character> stack_2 = new Stack<Character>();
    
    for (int j = 0; j < digits_2.length; j++) {
      stack_2.push(digits_2[j]);
    }
    
    for (int j = 0; j < digits_2.length; j++) {
      digits_2[j] = stack_2.pop();
    }
    
    String reverse_binaryString = String.valueOf(digits_2);
    if (reverse_binaryString.equals(binaryString)) return true;
    return false;
  }
  
  public static void main (String [] args) {
    Euler36 test = new Euler36();
    System.out.println(test.findPalindromes());
  }
}