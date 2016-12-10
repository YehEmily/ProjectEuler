import java.util.*;

public class Euler38 {
  
  int largest;
  LinkedList<Character> digitsList;
  
  public Euler38 () {
    largest = 9;
    digitsList = new LinkedList<Character>();
  }
  
  public int largestPandigital () {
    int counter = largest;
    while (counter < 100000) {
      if (isPandigital(counter) && isPandigital(counter * 2)) {
        int factor = 3;
        while (isPandigital(counter * factor)) {
          factor++;
        }
        if (finalIsPandigital()) {
          largest = counter;
        }
      }
      digitsList.clear();
      counter++;
    }
    return Integer.parseInt(Integer.toString(largest) + Integer.toString(largest*2));
  }
  
  private boolean finalIsPandigital () {
    if (digitsList.contains('0')) return false;
    if (digitsList.size() < 9) return false;
    return true;
  }
  
  private boolean isPandigital (int n) {
    char[] digits = convertInt(n);
    for (int i = 0; i < digits.length; i++) {
      if (!digitsList.contains(digits[i])) {
        digitsList.add(digits[i]);
      } else {
        return false;
      }
    }
    return true;
  }
  
  private char[] convertInt (int n) {
    return Integer.toString(n).toCharArray();
  }
  
  public static void main (String[] args) {
    Euler38 test = new Euler38();
    System.out.println(test.largestPandigital());
  }
}