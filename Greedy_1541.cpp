#include <iostream>


using namespace std;


int main()
{
    char str[60];
    int num = 0, sum =0, flag = 0, mode = 0;
    char* p = str;
    
    scanf("%s", str);
    
    for(; *p != '\0'; p++){
        if('0' <= *p && *p <= '9'){
            num *= 10;
            num += *p - '0';
        }
        if(*p == '+'){
            //printf("1. %d %d\n", num,sum);
            if(flag){
                sum -= num;
            }
            else{
                sum += num;
            }
            num = 0;
        }
        if(*p == '-'){
            //printf("2. %d %d\n", num, sum);
            if(!flag){
                sum += num;
                flag = 1;
            }
            
            else{
                sum -= num;
            }
            num = 0;
        }
        
    }
    //printf("L: %d %d\n", num, sum);
    if(flag){
        sum -= num;
    }
    else{
        sum += num;
    }
    
    printf("%d", sum);
    return 0;
}
