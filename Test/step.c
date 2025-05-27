#include<stdio.h>
#include<wiringPi.h>

#define ORANGE  21
#define YELLOW  22
#define PINK    23
#define BLUE    24
#define RED     25

void step_wave(int step)
{   
    switch(step)
    {
        case 0:
            digitalWrite(ORANGE, 1);
            digitalWrite(YELLOW, 0);
            digitalWrite(PINK,   0);
            digitalWrite(BLUE,   0);
            break;
        case 1:
            digitalWrite(ORANGE, 0);
            digitalWrite(YELLOW, 1);
            digitalWrite(PINK,   0);
            digitalWrite(BLUE,   0);
            break;
        case 2:
            digitalWrite(ORANGE, 0);
            digitalWrite(YELLOW, 0);
            digitalWrite(PINK,   1);
            digitalWrite(BLUE,   0);
            break;
        case 3:
            digitalWrite(ORANGE, 0);
            digitalWrite(YELLOW, 0);
            digitalWrite(PINK,   0);
            digitalWrite(BLUE,   1);
            break;
        default:
            break;
    }
    
}

void step_full(int step)
{
    switch(step)
    {
        case 0:
            digitalWrite(ORANGE, 1);
            digitalWrite(YELLOW, 1);
            digitalWrite(PINK,   0);
            digitalWrite(BLUE,   0);
            break;
        case 1:
            digitalWrite(ORANGE, 0);
            digitalWrite(YELLOW, 1);
            digitalWrite(PINK,   1);
            digitalWrite(BLUE,   0);
            break;
        case 2:
            digitalWrite(ORANGE, 0);
            digitalWrite(YELLOW, 0);
            digitalWrite(PINK,   1);
            digitalWrite(BLUE,   1);
            break;
        case 3:
            digitalWrite(ORANGE, 1);
            digitalWrite(YELLOW, 0);
            digitalWrite(PINK,   0);
            digitalWrite(BLUE,   1);
            break;
        default:
            break;
    }
}

void step_half(int step)
{
    switch(step)
    {
        case 0:
            digitalWrite(ORANGE, 1);
            digitalWrite(YELLOW, 0);
            digitalWrite(PINK,   0);
            digitalWrite(BLUE,   0);
            break;
        case 1:
            digitalWrite(ORANGE, 1);
            digitalWrite(YELLOW, 1);
            digitalWrite(PINK,   0);
            digitalWrite(BLUE,   0);
            break;
        case 2:
            digitalWrite(ORANGE, 0);
            digitalWrite(YELLOW, 1);
            digitalWrite(PINK,   0);
            digitalWrite(BLUE,   0);
            break;
        case 3:
            digitalWrite(ORANGE, 0);
            digitalWrite(YELLOW, 1);
            digitalWrite(PINK,   1);
            digitalWrite(BLUE,   0);
            break;
        case 4:
            digitalWrite(ORANGE, 0);
            digitalWrite(YELLOW, 0);
            digitalWrite(PINK,   1);
            digitalWrite(BLUE,   0);
            break;
        case 5:
            digitalWrite(ORANGE, 0);
            digitalWrite(YELLOW, 0);
            digitalWrite(PINK,   1);
            digitalWrite(BLUE,   1);
            break;
        case 6:
            digitalWrite(ORANGE, 0);
            digitalWrite(YELLOW, 0);
            digitalWrite(PINK,   0);
            digitalWrite(BLUE,   1);
            break;
        case 7:
            digitalWrite(ORANGE, 1);
            digitalWrite(YELLOW, 0);
            digitalWrite(PINK,   0);
            digitalWrite(BLUE,   1);
            break;
        default:
            break;
    }
}

int main()
{
    wiringPiSetup();
    pinMode(ORANGE, OUTPUT);
    pinMode(YELLOW, OUTPUT);
    pinMode(PINK,   OUTPUT);
    pinMode(BLUE,   OUTPUT);
    pinMode(RED,    OUTPUT);    //Power line
    digitalWrite(RED, HIGH);

    for(int i=0;i<4096;i++)     // half or full(wave)
    {
        step_wave(i%4);
        //step_full(i%4);
        //step_half(i%8);
        delay(2);
    }

    return(1);
}