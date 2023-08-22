#include <iostream>

using namespace std;
int dp[1001][3] = {0};
int ar[1001][3] = {0};

void findMin(int d, int color);
int main()
{
    int N;
    scanf("%d", &N);
    for(int i = 0; i < N; i++){
        scanf("%d %d %d", &ar[i][0], &ar[i][1], &ar[i][2]);
    }
    
    
    findMin(N - 1, 0);
    findMin(N - 1, 1);
    findMin(N - 1, 2);
    
    if(dp[N - 1][0] <= dp[N - 1][1] && dp[N - 1][0] < dp[N - 1][2]) printf("%d", dp[N - 1][0]);
    else if(dp[N - 1][1] <= dp[N - 1][0] && dp[N - 1][1] < dp[N - 1][2]) printf("%d", dp[N - 1][1]);
    else printf("%d", dp[N - 1][2]);
    
    return 0;
}

void findMin(int d, int color){
    if(d == 0) {
        dp[0][color] = ar[0][color];
         return;
    }
    for(int i = 0; i < 3; i++){
        if(i != color && dp[d - 1][i] != 0){
            findMin(d - 1, i);
           
        }
    }
    dp[d][color] = ar[d][color] + (dp[d - 1][(color + 1) % 3] < dp[d - 1][(color + 2) % 3] ? dp[d - 1][(color + 1) % 3] : dp[d - 1][(color + 2) % 3]);
    return;
}
