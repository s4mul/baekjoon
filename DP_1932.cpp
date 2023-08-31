#include <iostream>

using namespace std;
int ar[500][500];
int dp[500][500];

void tri(int height);
int main()
{
    int n;
    for(int i = 0; i < 500; i++){
        for(int j = 0; j < 500; j++){
            ar[i][j] = -1;
            dp[i][j] = -1;
        }
    }
    
    scanf("%d", &n);
    
    for(int i =0; i < n; i++){
        for(int j = 0; k <= i; j++){
            scanf("%d", &ar[i][j]);
        }
    }
    
    dp[0][0] = ar[0][0];
    
    tri(1);
    
    return 0;
}

void tri(int height){
    for(int i =0 ; i <= height; i++){
        
        if(dp[height][i] == -1){
            if(i == height)
            dp[height][i] = ar[height][i] + (dp[height - 1][i] > dp[height - 1][i];
        }
    }
}
