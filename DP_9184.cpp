#include <iostream>

using namespace std;

int w(int a, int b, int c);
int dp[101][101][101] = {0};
int main()
{
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);
    a = a + 50;
    b = b + 50; 
    c = c + 50;
    while(a != 49 || b != 49 || c != 49){
        printf("w(%d, %d, %d) = %d\n",a - 50, b - 50, c - 50, w(a,b,c));
        scanf("%d %d %d", &a, &b, &c);
        a = a + 50;
        b = b + 50; 
        c = c + 50;
    }

    return 0;
}


int w(int a, int b, int c){
    
    
    if(a <= 50 || b <= 50 || c <= 50){
        return 1;
    }
    if(a > 70 || b > 70||c > 70){
        return w(70,70,70);
    }
    if(dp[a][b][c] != 0){
        return dp[a][b][c];
    }
    
    if(a < b && b < c){
        dp[a][b][c] = w(a,b,c-1) + w(a,b-1,c-1) - w(a, b-1, c);
        return  dp[a][b][c];
    }
    else {
        dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1);
        return dp[a][b][c];
    }
}
