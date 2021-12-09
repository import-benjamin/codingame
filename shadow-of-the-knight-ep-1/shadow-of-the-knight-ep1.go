package main

import (
    "fmt"
)

// Min returns the smaller of x or y.
func Min(x, y int) int {
    if x > y {
            return y
    }
    return x
}

// Max returns the larger of x or y.
func Max(x, y int) int {
    if x < y {
            return y
    }
    return x
}

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

func main() {

    var shiftW, shiftH int = 0, 0

    // W: width of the building.
    // H: height of the building.
    var W, H int
    fmt.Scan(&W, &H)
    
    // N: maximum number of turns before game over.
    var N int
    fmt.Scan(&N)
    
    var X0, Y0 int
    fmt.Scan(&X0, &Y0)
    
    for {
        // bombDir: the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
        var bombDir string
        fmt.Scan(&bombDir)

        for i := 0 ; i < len(bombDir) ; i++ {
            switch(bombDir[i]) {
            case 'U':
                Y0 -= (Y0 - shiftH)/ 2
            case 'D':
                shiftH = Y0
                Y0 = Min(Y0 + ((H - Y0) / 2), H - 1)
            case 'R':
                shiftW = X0
                X0 = Min(X0 + ((W - X0) / 2), W - 1)
            case 'L':
                X0 -= (X0 - shiftW ) / 2 
            }
        }
        
        
        // fmt.Fprintln(os.Stderr, "Debug messages...")
        
        // the location of the next window Batman should jump to.
        fmt.Printf("%v %v\n", X0, Y0)
    }
}
