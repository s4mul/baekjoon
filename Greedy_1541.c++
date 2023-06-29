
#include <iostream>


using namespace std;


int main()
{
    char str[60];
    int num = 0, sum =0, flag = 0, mode = 0;
    char* p = str;
    
    scanf("%s", str);
    
    for(; *p != '\n'; p++){
        if('0' <= *p && *p <= '9'){
            num *= 10;
            num += *p - '0';
        }
        if(*p == '+'){
            if(flag == 1){
                sum -= num;
            }
            else{
                sum += num;
            }
            num = 0;
        }
        if(*p == '-'){
            if(!flag){
                sum += num;
                flag = 1;
            }
            
            sum -= num;
            num = 0;
        }
        printf("%d ", sum);
    }
    
    if(flag){
        sum -= num;
    }
    else{
        sum += num;
    }
    
    printf("%d", sum);
    return 0;
}
