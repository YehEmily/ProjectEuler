import java.util.*;

public class Euler32 {
  
  LinkedList<Integer> products;
  
  public Euler32 () {
    products = new LinkedList<Integer>();
  }
  
  public void findPandigitals () {
    for (int i = 1; i < 9999; i++) {
      for (int j = 1; j < 9999; j++) {
        if (isPandigital(i, j) && !products.contains(i * j)) {
          products.add(i * j);
        }
      }
    }
  }
  
  public int sumPandigits () {
    findPandigitals();
    int sum = 0;
    while (!products.isEmpty()) {
      int product = products.remove();
      sum += product;
    }
    return sum;
  }
  
  private boolean isPandigital (int a, int b) {
    LinkedList<Character> comparators = new LinkedList<Character>();
    int c = a * b;
    char[] a_chars = convertToChars(a);
    char[] b_chars = convertToChars(b);
    char[] c_chars = convertToChars(c);
    
    for (int i = 0; i < a_chars.length; i++) {
      if (!comparators.contains(a_chars[i])) {
        comparators.add(a_chars[i]);
      } else {
        return false;
      }
    }
    
    for (int j = 0; j < b_chars.length; j++) {
      if (!comparators.contains(b_chars[j])) {
        comparators.add(b_chars[j]);
      } else {
        return false;
      }
    }
    
    for (int k = 0; k < c_chars.length; k++) {
      if (!comparators.contains(c_chars[k])) {
        comparators.add(c_chars[k]);
      } else {
        return false;
      }
    }
    
    if (comparators.contains('0')) return false;
    
    if (comparators.size() < 9) return false;
    
    return true;
  }

  private char[] convertToChars (int n) {
    char[] result = Integer.toString(n).toCharArray();
    return result;
  }
  
  public static void main (String [] args) {
    Euler32 test = new Euler32();
    System.out.println(test.sumPandigits());
  }
}