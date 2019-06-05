#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>

#define PLAYER_SPEED 1000
#define ZB_SPEED 400
#define GUN_AIM 2000

using namespace std;

typedef struct Position
{
    int x;
    int y;
};

typedef struct Humain
{
    int Id;
    Position pos;
};

typedef struct Zombie
{
    int Id;
    Position pos;
    Position next;
};

int distanceBetween(Position p1, Position p2) {
    return sqrt(pow(p1.x - p2.x, 2)+pow(p1.y - p2.y, 2));
}

void nextMove(Position *me, Humain *humains, int hc, Zombie *zombies, int zc) {
    me->x += 1000;
    me->y += 950;
    
    for (int i = 0; i < hc; ++i)
    {
        cerr << humains[i].pos.x << humains[i].pos.y <<endl;
    }


    // those we must save directly
    // rule 1 : he can make it in time (dist:human-zombie/zombie speed) < (dist:human-me)
    // then the closest he can save 
    
}

/**
 * Save humans, destroy zombies!
 **/
int main()
{

    // game loop
    while (1) {        
        Position me;
        cin >> me.x >> me.y; cin.ignore();
        int humanCount;
        cin >> humanCount; cin.ignore();
        Humain humains[humanCount];
        for (int i = 0; i < humanCount; i++) {
            cin >> humains[i].Id >> humains[i].pos.x >> humains[i].pos.y; cin.ignore();
        }
        int zombieCount;
        cin >> zombieCount; cin.ignore();
        Zombie zombies[zombieCount];
        for (int i = 0; i < zombieCount; i++) {
            cin >> zombies[i].Id >> zombies[i].pos.x >> zombies[i].pos.y >> zombies[i].next.x >> zombies[i].next.y; cin.ignore();
        }
        
        nextMove(&me, humains, humanCount, zombies, zombieCount);
        
        cout << me.x << " " << me.y << endl;
    }
}
