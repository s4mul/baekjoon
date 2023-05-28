#include <iostream>
#include<stdio.h>
#include <queue> //include stack library
#define MAXCOR 500000
using namespace std;

int sister_start_cor, my_start_cor;
int calcSisterCor(int sec);// 시작점을 받아서 해당 시간에 대한 동생의 좌표를 계산함
int calcMyCor(int curent_cor);//이전 단계의 시작점을 받아서 시간(깊이)에서 가능한 나의 위치를 확인함
queue<int> buffer;

int main() {
    scanf("%d %d", &my_start_cor, &sister_start_cor);
    
    printf("%d",calcMyCor(my_start_cor));
    

    return 0;
}

int calcSisterCor(int sec){
    if(sec == 0)
        return sister_start_cor;
    else
        return sister_start_cor + sec*(sec + 1)/2;
}
// 시작점을 받아서 해당 시간에 대한 동생의 좌표를 계산함
int calcMyCor(int current_cor){
    int sec = 0;
    int sister_cor, size_depth = 1;
    buffer.push(current_cor);//시작점
    
    while(1){
        sister_cor = calcSisterCor(sec);
        
        for(int i = 0; i < size_depth; i++){//search each depth
            current_cor = buffer.front();
            buffer.pop();
            if(sister_cor > MAXCOR){//기저_못찾음
                return -1;
            }
            if(sister_cor == current_cor)//기저_찾음
                return sec;
            
            
            
            if(current_cor > 0)
                buffer.push(current_cor - 1);
            buffer.push(current_cor + 1);
            buffer.push(current_cor * 2);
            
        }
        sec++;//find all case in same depth, go next depth
        size_depth = buffer.size();//save case size in same depth
    }
    
    
}//이전 단계의 시작점을 받아서 시간(깊이)에서 가능한 나의 위치를 확인함
//이때 동생을 찾으면 시간, 못 찾으면 -1을 반환한다. 즉, 동생을 찾았는지 여부를 반환한다.
