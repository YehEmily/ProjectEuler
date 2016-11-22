public class Euler31 {
  
  public Euler31() {
  }
  
  public int make200 () {
    int count = 0;
    for (int i = 0; i <= 200; i++) { // 1p pieces
      for (int j = 0; j <= 100; j++) { // 2p pieces
        for (int k = 0; k <= 40; k++) { // 5p pieces
          for (int l = 0; l <= 20; l++) { // 10p pieces
            for (int m = 0; m <= 10; m++) { // 20p pieces
              for (int n = 0; n <= 4; n++) { // 50p pieces
                for (int o = 0; o <= 2; o++) { // 100p pieces
                  if (i + 2*j + 5*k + 10*l + 20*m + 50*n + 100*o == 200)
                    count++;
                }
              }
            }
          }
        }
      }
    }
    return count + 1; // because 1*200p is also valid
  }
  
  public static void main(String [] args) {
    Euler31 solution = new Euler31();
    System.out.println(solution.make200());
  }
}