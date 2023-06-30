#include <iostream>
#include<queue>
using namespace std;
int BFS(int[][101]);
int dir[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};
int N, M;

int main()
{
    int maze[101][101];
    char tmp;
    scanf("%d %d", &N, &M);
    getchar();
    for(int i = 0; i < N; i++){
        for(int j = 0; j < M; j++){
            scanf("%c", &tmp);
            maze[i][j] = tmp - '0';
        }
        getchar();
    }
    printf("%d\n",BFS(maze) - 1);
    
    /*for(int i = 0; i < N; i++){
        for(int j = 0; j < M; j++){
            printf("%d ", maze[i][j]);
        }
        printf("\n");
    }*/

    return 0;
}
int BFS(int maze[][101]){
    queue<pair<int, int>> que;
    pair<int, int> cor;
    int x = 0, y = 0;
    que.push(make_pair(x, y));
    maze[x][y] = 2;
    
    while(!que.empty()){
        cor = que.front();
        que.pop();
        x = cor.first;
        y = cor.second;
        if(x == N - 1 && y == M - 1){
            return maze[x][y];
        }
        for(int i = 0; i < 4; i++){
            if(0 <= x + dir[i][0] && x + dir[i][0] < N 
            && 0 <= y + dir[i][1] && y + dir[i][1] < M 
            && maze[x + dir[i][0]][y + dir[i][1]] == 1){
                maze[x + dir[i][0]][y + dir[i][1]] = maze[x][y] + 1;
                que.push(make_pair(x + dir[i][0],y + dir[i][1]));
            }
        }
    }
    return -1;
}
