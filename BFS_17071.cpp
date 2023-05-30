
#include <iostream>
#include<stdio.h>
#include <queue> //include stack library
#define MAXCOR 500000
using namespace std;

int sister_start_cor, my_start_cor;
int calcSisterCor(int sec);// 시작점을 받아서 해당 시간에 대한 동생의 좌표를 계산함
int calcMyCor();//시간(깊이)에서 가능한 나의 위치를 확인함
queue<int> buffer;

int visited_map[2][500001] = {0};

int main() {
    scanf("%d %d", &my_start_cor, &sister_start_cor);
    
    printf("%d",calcMyCor());
    

    return 0;
}

int calcSisterCor(int sec){
        return sister_start_cor + sec*(sec + 1)/2;
}
// 시작점을 받아서 해당 시간에 대한 동생의 좌표를 계산함

int calcMyCor(){
    int sec = 0;
    int sister_cor, my_cor, size_depth = 1;
    buffer.push(my_start_cor);//시작점
    visited_map[0][my_start_cor] = 1;
    
    
    while(1){
        sister_cor = calcSisterCor(sec);
        
        for(int i = 0; i < 21; i++){
            printf("%d ", visited_map[0][i]);
        }
        printf("\n");
        for(int i = 0; i < 21; i++){
            printf("%d ", visited_map[1][i]);
        }
        printf("\n");
        
        
        
        for(int i = 0; i < size_depth; i++){//search each depth
            my_cor = buffer.front();
           
            printf("mycor: %d\n", my_cor);
            buffer.pop();
            if(my_cor > MAXCOR){//기저_못찾음
                return -1;
            }
            
            sec++;
            if(my_cor > 0 && visited_map[sec&0][my_cor - 1] == 0){
                buffer.push(my_cor - 1);
                visited_map[sec&1][my_cor - 1] = 1;
            }
            if(my_cor + 1 <= MAXCOR && visited_map[sec&1][my_cor + 1] == 0){
                buffer.push(my_cor + 1);
                visited_map[sec&1][my_cor + 1] = 1;
            }
            if(my_cor * 2 <= MAXCOR && visited_map[sec&1][my_cor * 2] == 0){
                buffer.push(my_cor * 2);
                visited_map[sec&1][my_cor * 2] = 1;
            }
            sec--;
            
            
        }
        
        if(visited_map[sec&1][sister_cor]){
            printf("%d\n",sister_cor);
            printf("%d\n",visited_map[sec&1][sister_cor] );
            return sec;
        }
        
        
        
        
        sec++;//find all case in same depth, go next depth
        size_depth = buffer.size();//save case size in same depth
        
    }
    
    
}//이전 단계의 시작점을 받아서 시간(깊이)에서 가능한 나의 위치를 확인함
//이때 동생을 찾으면 시간, 못 찾으면 -1을 반환한다. 즉, 동생을 찾았는지 여부를 반환한다.
