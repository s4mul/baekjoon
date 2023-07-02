#include <iostream>

using namespace std;
void DFS(int x);
int inc[101][101] = {0};
int cmp[101] = {0};
int cnt = 0;
int N;
int main()
{
    int M, x, y;
    scanf("%d", &N);
    scanf("%d", &M);
    
    for(int i = 0; i < M; i++){
        scanf("%d %d", &x, &y);
        inc[x][y] = 1;
        inc[y][x] = 1;
    }
    cmp[1] = 1;
    DFS(1);
    printf("%d", cnt);
    
    return 0;
}
void DFS(int x){
    printf("x: %d\n", x);
    for(int i = 0; i <= N; i++){
        if(inc[x][i] && !cmp[i]){
            cmp[i] = 1;
            cnt++;
            DFS(i);
        }
    }
    return;
}
