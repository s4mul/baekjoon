#include <iostream>

using namespace std;

int main()
{
    int coin[10];
    int N, K, idx, cnt = 0;
    
    scanf("%d %d", &N, &K);
    for(int i = 0; i < N; i++){
       scanf("%d", coin + i);
    }
    idx = N - 1;
    while(K > coin[0]){
        
        printf("%d %d\n", K, coin[idx]);
        if(K < coin[idx]){
            idx--;
        }
        else{
            K -= coin[idx];
            cnt++;
        }
    }
    
    printf("%d",cnt);
    return 0;
}
