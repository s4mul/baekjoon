#include <iostream>

using namespace std;

int main()
{
    int N, S, flag = 0, cnt, res = 0;
    char str[1000001];
    scanf("%d\n%d\n",&N, &S);
    
    cnt = 0;
    
    for(int i =0; i < S; i++){
        scanf("%c",str + i);
        if(flag == 0 && str[i] == 'I'){
            flag = 1;
        }
        else if(flag == -1 && str[i] == 'I'){
            flag *= -1;
            cnt++;
        }
        else if(flag == 1 && str[i] == 'O'){
            flag *= -1;
        }
        else{
            //printf("%d %d\n", i, cnt);
            if(str[i] == 'I'){
                flag = 1;
            }
            else
                flag = 0;

            if(cnt >= N){
                res += cnt - N + 1;
            }
            cnt = 0;
        }
    }
    if(cnt >= N){
                res += cnt - N + 1;
            }
    printf("%d", res);
    return 0;
}
