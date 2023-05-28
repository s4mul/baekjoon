#include <iostream>
#include<stdio.h>
#include <stack> //include stack library
using namespace std;


int S[9][9] = {0};
int target[82];

int size;


bool is_correct(int, int);
void appendSu();
void sudocu();

int main() {
    
    for(int i = 0; i < 9; i++){
        for(int j = 0; j < 9; j++){
            scanf("%d", &S[i][j]);
        }
    }
    
    appendSu();
    
    sudocu();
    printf("\n");
    for(int i = 0; i < 9; i++){
        for(int j = 0; j < 9; j++){
            printf("%d ", S[i][j]);
        }
        printf("\n");
    }
    
    return 0;
}

bool is_correct(int x, int y){
    int tmp, xtmp, ytmp, cnt = 0;
    //if(S[x][y] > 9)
        //return false;
    for(int i = 0; i < 9; i++){//가로, 세로줄에 있나 확인
        
        tmp = S[x][y];
        if(S[x][i] == tmp && i != y)
            return false;
        if(S[i][y] == tmp && i != x)
            return false;
        //if(cnt > 1)//각 줄을 한 번씩 탐색하므로 기본적으로 2회는 존재함
            
    }
    
    xtmp = (x) / 3 * 3;
    ytmp = (y) / 3 * 3;
    
  
    
    //printf("%d %d", xtmp, ytmp);
    for(int i = 0; i < 3; i++){//사각형 안에 있나 확인
        for(int j = 0; j < 3; j++){
            if(S[xtmp + i][ytmp + j] == tmp && xtmp + i != x && ytmp + j != y){
                return false;
            } 
        }
    }
    return true;
}

void appendSu(){
    int iter = 0;
    for(int i = 0; i < 9; i++){
        for(int j = 0; j < 9; j++){
            if(S[i][j] == 0){
                target[iter++] = 10 * i + j;
            }
        }
    }
    size = iter;

}

void sudocu(){

    int xcor, ycor, iter = 0;
    while(iter < size){//빈칸이 다 체워진 경우
        xcor = target[iter] / 10;
        ycor = target[iter] % 10;
        S[xcor][ycor]++;
        while(!is_correct(xcor,ycor) && S[xcor][ycor] < 10){
            S[xcor][ycor]++;
        }
        
        if(S[xcor][ycor] > 9){//넣을수 있는 경우가 없는 경우
            S[xcor][ycor] = 0;
            iter--;//이전의 처리로 돌아간다
            //무조껀 해가 있기 때문에 가능한 경우가 없는 경우는 처리해주지 않는다.
        }
        else{//올바른 값이 넣어졌을 경우
            iter++;
        }
    }
    
    return;
    
}
