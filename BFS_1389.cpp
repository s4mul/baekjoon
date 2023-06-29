
#include <iostream>
#include<queue>

using namespace std;

int inc[101][101] = {0};
int visit[101][101] = {0};
int Num;

int bacon(int person);//인물을 받고 그 인물에 대한 케빈 베이컨의 수를 반환함

int main()
{
    int N, M, x, y, min, tmp, min_person = 1;
    scanf("%d %d", &N, &M);
    Num = N;
    for(int i = 0; i < M; i++){
        scanf("%d %d",&x, &y );
        inc[x][y] = 1;
        inc[y][x] = 1;
    }//인접행렬 초기화
    
    min = bacon(1);
    for(int i = 2; i <= N; i++){
        tmp = bacon(i);
        if(min > tmp){
            min = tmp;
            min_person = i;
        }
    }
    printf("%d", min_person);
    return 0;
}

int bacon(int person){
    
    queue<int> que;
    int fr;
    int parent = 0;
    que.push(person);
    visit[person][person] = 1;//넣으면서 방문 체크
    
    parent = 1;//부모의 깊이는 1이라고 하자.
    while(!que.empty()){    
        fr = que.front();
        que.pop();
        parent = visit[person][fr];
        //printf("*");
        for(int i = 1; i <= Num; i++){
            if(inc[fr][i] == 1){
                if(visit[person][i] == 0 || visit[person][i] > parent + 1){//방문한 적이 없거나 새로 방문한 경우가 더 빠를때
                    visit[person][i] = parent + 1;
                    que.push(i);
                }//방문 및 거리 체크
                
            }//경로가 있을 때
       }//해당 노드에 대해 모든 경로에 대해
       
       //printf("p: %d ",parent);
    }//모든 노드에 대해
    int sum = 0;
    for(int i = 1; i <= Num; i++){
        sum += visit[person][i] - 1;
    }
    return sum;
}
