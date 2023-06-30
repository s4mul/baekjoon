#include <iostream>
#include<queue>
using namespace std;
int BFS(int[][1001]);
int dir[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};
int N, M;

int main()
{
    int maze[1001][1001];
 
    scanf("%d %d", &M, &N);
    for(int i = 0; i < N; i++){
        for(int j = 0; j < M; j++){
            scanf("%d", &maze[i][j]);
        }
    }
    int tmp;
    tmp = BFS(maze);
    if(tmp == -1) printf("%d", tmp);
    else printf("%d\n", tmp - 2);
    /*
    for(int i =0 ; i < N; i++){
        for(int j = 0; j < M; j++){
            printf("%d ", maze[i][j]);
        }
        printf("\n");
    }*/
    

    return 0;
}
int BFS(int maze[][1001]){
    queue<pair<int, int>> que;
    pair<int, int> cor;
    int x, y, cnt = 0;
    
    for(int i =0 ; i < N; i++){
        for(int j = 0; j < M; j++){
            if(maze[i][j] == 1){
                que.push(make_pair(i, j));
                //printf("%d %d\n", i, j);
                maze[i][j] = 2;
                cnt++;
            }
            if(maze[i][j] == -1){
                cnt++;
            }
        }
    }
    

    
    while(!que.empty()){
        cor = que.front();
        que.pop();
        x = cor.first;
        y = cor.second;
        //printf("x: %d, y: %d\n", x, y);
        for(int i = 0; i < 4; i++){
            if(0 <= x + dir[i][0] && x + dir[i][0] < N && 0 <= y + dir[i][1] && y + dir[i][1] < M){ //범위 안에 있고
                if(maze[x + dir[i][0]][y + dir[i][1]] == 0){//안익은 토마토가 있음
                    maze[x + dir[i][0]][y + dir[i][1]] =  maze[x][y] + 1;
                    que.push(make_pair(x + dir[i][0],y + dir[i][1]));
                    //printf("%d %d\n", x + dir[i][0],y + dir[i][1]);
                    cnt++;
                }
                
            }
        }
        /*
        for(int i =0 ; i < N; i++){
        for(int j = 0; j < M; j++){
            printf("%d ", maze[i][j]);
        }
        printf("\n");
    }
    printf("\n=============\n");
        */
    }
    if(cnt >= M*N){
            return maze[x][y];
    }
    return -1;
}
