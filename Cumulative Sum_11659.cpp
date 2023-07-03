#include <iostream>
#include<queue>
#include<tuple>
using namespace std;


int main()
{
    int ar[100001] = {0};
    int tmp;
    int M,N, i, j;
    scanf("%d %d", &N, &M);
    
    for(int k =1; k <= N; k++){//0번째 항은 누적합 구하기의 일관성을 위해 0이라고 해준다.
        scanf("%d", &tmp);
        ar[k] += ar[k - 1] + tmp;//구간까지의 총합을 구해준다
    }
    
    /*for(int k =0; k < N; k++){
        printf("%d ", ar[k]);
    }*/
    //printf("NM: %d %d\n", N, M);
    for(int k =0; k < M; k++){
        scanf("%d %d", &i, &j);
        //printf("j, i: %d %d\n", j, i);
        printf("%d\n", ar[j] - ar[i - 1]);//제일 앞까지의 합에서 제일 뒷까지의 합을 빼준다.
        //i번째는 포함이므로 이전값을 빼준다.
    }
    return 0;
}
