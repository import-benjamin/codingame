import java.util.*;
import java.io.*;
import java.math.*;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
class Player {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int W = in.nextInt(); // width of the building.
        int H = in.nextInt(); // height of the building.
        int N = in.nextInt(); // maximum number of turns before game over.
        int X0 = in.nextInt();
        int Y0 = in.nextInt();

        // game loop
        while (true) {
            String bombDir = in.next(); // the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
            int moveSize = 7;
            switch(bombDir) {
                case "U":
                    Y0 -= moveSize;
                    break;
                case "UR":
                    X0 += moveSize;
                    Y0 -= moveSize;
                    break;
                case "R":
                    X0 += moveSize;
                    break;
                case "DR":
                    Y0 += moveSize;
                    X0 += moveSize;
                    break;
                case "D":
                    Y0 += moveSize;
                    break;
                case "DL":
                    X0 -= moveSize;
                    Y0 += moveSize;
                    break;
                case "L":
                    Y0 -= moveSize;
                    break;
                case "UL":
                    X0 += moveSize;
                    Y0 += moveSize;
                    break;
            }
            
            // Write an action using System.out.println()
            // To debug: System.err.println("Debug messages...");


            // the location of the next window Batman should jump to.
            System.out.println(X0+" "+Y0);
        }
    }
}
