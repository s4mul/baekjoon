#include <iostream>

using namespace std;
int step[300];
int value[300] = {0};
int topDown(int cor);
int main()
{
    int N;
    scanf("%d", &N);
    for(int i = 0; i < N; i++){
        scanf("%d", step + i);
    }
    value[0] = step[0];
    value[1] = step[1] + step[0];
    value[2] = step[0] + step[2] > step[1] + step[2] ? step[0] + step[2] : step[1] + step[2];
    printf("%d", topDown(N - 1));
    
    return 0;
}
int topDown(int cor){
    int max, tmp1, tmp2;
    if(cor < 0)
        return 0;
    if(value[cor] != 0){
        return value[cor];
    }
    
    tmp1 = step[cor] + step[cor - 1] + topDown(cor - 3);//현재칸 + 현재 전칸 + 현재 전전전칸의 최대값
    tmp2 = step[cor] + topDown(cor - 2);//현재칸 + 현재 전전칸
    max = tmp1 > tmp2 ? tmp1: tmp2;
    //printf("max: %d\n", max);
    value[cor] = max;
    return value[cor];
}
