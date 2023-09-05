#include <iostream>

using namespace std;
int ar[500][500];
int dp[500][500];

int tri(int height);
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
        for(int j = 0; j <= i; j++){
            scanf("%d", &ar[i][j]);
        }
    }
    

    
    for(int i = 1; i < n; i++)
        tri(n - i);
    
    
    printf("%d",ar[0][0]);
    return 0;
}

int tri(int height){//결국 탑다운이네?
    for(int i =0 ; i <= height; i++){//가로에 있는 모든 원소에 대해
                ar[height - 1][i] += (ar[height][i] > ar[height][i + 1] ? ar[height][i] : ar[height][i + 1]);
    }
    return 0;
}

