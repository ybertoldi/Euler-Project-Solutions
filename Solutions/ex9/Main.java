package Solutions.ex9;

public class Main {
    public static void main(String[] args) {
        int abc = solve();
        System.out.println(abc);
    }

    private static int solve() {
        int a = 0;
        while (true) {
            for (int b = 0; b < a; b++) {
                if (isNotNaturalSquare(a, b)) {
                    continue;
                }

                int c = (int) (Math.sqrt( (a*a + b*b) ) + 0.5);
                if (a + b + c == 1000) {
                    System.out.printf("a: %d, b: %d, c: %d \n", a, b, c);
                    return a * b * c;
                }
            }
            a++;
        }
    }

    private static boolean isNotNaturalSquare(int a, int b) {
        int n = (a*a + b*b);
        double sqrt = Math.sqrt(n);
        int roundSqrt = ((int) (sqrt + 0.5));

        return sqrt * roundSqrt == n;
    }

}
