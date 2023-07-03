#include <iostream>
#include<algorithm>
using namespace std;

int home[25][25] = {0};
int dir[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};
int complex[500];
int cor= 0;
int N;
void travel(int x, int y);
bool compare(int a, int b);
int main()
{

    char tmp;
    scanf("%d", &N);
    getchar();
    for(int i = 0; i < N; i++){
        for(int j =0; j < N; j++){
            scanf("%c", &tmp);
            home[i][j] = tmp -'0';
        }
        getchar();
    }/*
    for(int i = 0; i < N; i++){
        for(int j =0; j < N; j++){
            printf("%d ", home[i][j ]);
        }
        printf("\n");
    }*/
    for(int i = 0; i < N; i++){
        for(int j =0; j < N; j++){
            if(home[i][j] == 1) cor++;
            travel(i, j);
        }
    }
    printf("%d\n", cor);
    
    sort(complex + 1, complex + cor + 1, compare);
    for(int i =1; i <= cor; i++){
        printf("%d\n", complex[i]);
    }
    /*
    for(int i = 0; i < N; i++){
        for(int j =0; j < N; j++){
            printf("%d ", home[i][j ]);
        }
        printf("\n");
    }*/
    return 0;
}
bool compare(int a, int b){
    return a < b;
}
void travel(int x, int y){
    if(home[x][y] != 1){
        return;
    }
    if(home[x][y] == 1){
        home[x][y] += cor;
        complex[cor]++;
        for(int i = 0; i < 4; i++){
            if(0 <= x + dir[i][0] && x + dir[i][0] < N &&0 <= y + dir[i][1] && y + dir[i][1] < N ){
                travel(x + dir[i][0], y + dir[i][1]);
            }
        }
    }
    
}
