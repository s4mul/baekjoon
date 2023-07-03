#include <iostream>
#include<queue>
#include<tuple>
using namespace std;
int BFS(int[101][101][101]);
int dir[6][3] = {{1,0,0},{-1,0,0},{0,1,0},{0,-1,0},{0,0,1},{0,0,-1}};
int N, M, H;

int main()
{
    int maze[101][101][101];
 
    scanf("%d %d %d", &M, &N, &H);
    for(int k = 0; k < H; k++){
        for(int i = 0; i < N; i++){
            for(int j = 0; j < M; j++){
                
                scanf("%d", &maze[k][i][j]);
            }
        }
    }
    int tmp;
    tmp = BFS(maze);
    if(tmp == -1) printf("%d", tmp);
    else printf("%d\n", tmp - 2);
    /*
    printf("\n");
    for(int i =0 ; i < N; i++){
        for(int j = 0; j < M; j++){
            printf("%d ", maze[0][i][j]);
        }
        printf("\n");
    }*/
    

    return 0;
}
int BFS(int maze[101][101][101]){
    queue<tuple<int, int, int>> que;
    tuple<int, int, int> cor;
    int x, y,z, cnt = 0;
    for(int k = 0; k < H; k++){
        for(int i =0 ; i < N; i++){
            for(int j = 0; j < M; j++){
                if(maze[k][i][j] == 1){
                    que.push(make_tuple(i, j, k));
                    //printf("%d %d\n", i, j);
                    maze[k][i][j] = 2;
                    cnt++;
                }
                if(maze[k][i][j] == -1){
                    cnt++;
                }
            }
        }
    }
    

    
    while(!que.empty()){
        cor = que.front();
        que.pop();
        x = get<0>(cor);
        y = get<1>(cor);
        z = get<2>(cor);
        //printf("x: %d, y: %d\n", x, y);
        for(int i = 0; i < 6; i++){
            if(0 <= x + dir[i][0] && x + dir[i][0] < N 
                && 0 <= y + dir[i][1] && y + dir[i][1] < M
                && 0 <= z + dir[i][2] && z + dir[i][2] < H){ //범위 안에 있고
                
                if(maze[z + dir[i][2]][x + dir[i][0]][y + dir[i][1]] == 0){//안익은 토마토가 있음
                    maze[z + dir[i][2]][x + dir[i][0]][y + dir[i][1]] =  maze[z][x][y] + 1;
                    que.push(make_tuple(x + dir[i][0],y + dir[i][1],z + dir[i][2]));
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
    //printf("cnt: %d\n", cnt);
    if(cnt >= M*N*H){
            return maze[z][x][y];
    }
    
    return -1;
}
