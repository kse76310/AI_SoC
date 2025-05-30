#include<stdio.h>
#include<wiringPi.h>

#define ORANGE  21
#define YELLOW  22
#define PINK    23
#define BLUE    24
#define RED     25
#define TRIG    27
#define ECHO    28

#define REVERSE_DISTANCE 10.0

void step_forward(int step)
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

void step_backward(int step)
{   
    switch(step)
    {
        case 0:
            digitalWrite(ORANGE, 1);
            digitalWrite(YELLOW, 0);
            digitalWrite(PINK,   0);
            digitalWrite(BLUE,   1);
            break;
        case 1:
            digitalWrite(ORANGE, 0);
            digitalWrite(YELLOW, 0);
            digitalWrite(PINK,   1);
            digitalWrite(BLUE,   1);
            break;
        case 2:
            digitalWrite(ORANGE, 0);
            digitalWrite(YELLOW, 1);
            digitalWrite(PINK,   1);
            digitalWrite(BLUE,   0);
            break;
        case 3:
            digitalWrite(ORANGE, 1);
            digitalWrite(YELLOW, 1);
            digitalWrite(PINK,   0);
            digitalWrite(BLUE,   0);
            break;
        default:
            break;
    }
    
}


void Trigger()
{
    //Trigger signal
    digitalWrite(TRIG, HIGH);
    delayMicroseconds(10);
    digitalWrite(TRIG, LOW);
    delayMicroseconds(200); //wait for Burst end0p
}

double Distance()
{
    while(1)
    {
        int e = digitalRead(ECHO);
        if(e == 1) break;
    }
    int t1 = micros();
    while(1)    //wait until echo receive
    {
        int e = digitalRead(ECHO);
        if(e == 0) break;
    }
    int t2 = micros();

    double dist = (t2 - t1) * 0.017;
    return dist;
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

    pinMode(TRIG, OUTPUT);
    pinMode(ECHO, INPUT);
    digitalWrite(TRIG, LOW);
    delay(10);  //초기 pin 상태 0

    int stepCounter = 0;

    while(1)
    {
        //Trigger signal
        Trigger();
        double dist = Distance();
        printf("Distance : %.2f\n\n",dist);

        if(dist < REVERSE_DISTANCE)
        {
            for(int i=0;i<200;i++)
            {
                step_backward(stepCounter % 4);
                stepCounter++;
                delay(2);
            }
            delay(500);
        }
        else
        {
            for(int i=0;i<200;i++)
            {
                step_forward(stepCounter % 4);
                stepCounter++;
                delay(2);
            }
        }
        delay(100); //delay for next trigger
    }

    
    return 0;
}