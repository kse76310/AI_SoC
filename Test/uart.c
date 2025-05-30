#include <stdio.h>
#include <wiringPi.h>
#include <wiringSerial.h>
#include <termios.h>

#define B_RATE B9600

int main()
{
    //struct termios op;
    int fd = serialOpen("/dev/serial0", 9600);

    serialPutchar(fd, 'a');
    
    char a = serialGetchar(fd);
    
    printf("%c\n\n",a);

    return 0;
}