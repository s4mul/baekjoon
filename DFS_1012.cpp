#include <iostream>

using namespace std;
 int ground[50][50] = {0};
int countWormAmount(int xcor, int ycor, int x, int y);//DFS
int DFS(int x, int y);
int main()
{
    int T, M, N, K, xcor, ycor, worm;
   
    
    scanf("%d", &T);
    for(int i = 0; i < T; i++){
        scanf("%d %d %d", &M, &N, &K);
        for(int j = 0; j < K; j++){
            scanf("%d %d", &xcor, &ycor);
            ground[xcor][ycor] = 1;
        }
        worm = DFS(M, N);
        printf("%d\n", worm);
        
        for(int i = 0; i < 50; i++){
            for(int j =0 ; j < 50; j++){
                ground[i][j] = 0;
            }
        }
    }//input
    
    
    
    
    return 0;
}

int countWormAmount(int xcor, int ycor, int x, int y){//DFS
    int flag =0;
    if(ground[xcor][ycor] != 1){
        return 0;
    }
    else{
        printf(" xcor: %d, ycor: %d\n ", xcor, ycor);
      flag = 1;
      ground[xcor][ycor] = 2;
    } 
    
    if( xcor >= 1){
        
        flag += countWormAmount(xcor - 1,ycor, x, y);
    }
    if(xcor < x - 1){
        
        flag += countWormAmount(xcor + 1,ycor, x, y);
    }
    if(ycor >= 1){
        flag += countWormAmount(xcor,ycor - 1, x, y);
    }
    if(ycor < y - 1){
        flag += countWormAmount(xcor ,ycor + 1, x, y);
    }
    printf("flag : %d\n", flag);
    return flag > 0;
}
int DFS(int x, int y){
    int cnt=0;

    for(int i = 0; i < x; i++){
        for(int j = 0; j < y; j++){
            cnt += countWormAmount(i, j, x, y);
        }
    }
    return cnt;
}
