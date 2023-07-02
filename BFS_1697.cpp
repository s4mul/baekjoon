#include <iostream>
#include<queue>
using namespace std;

int space[100001] = {0};
int BFS(int sis, int bab);
int main()
{
    int N, K;
    scanf("%d %d",&N, &K);
  
    
    printf("%d",BFS(N, K) - 1);
    
    return 0;
}
int BFS(int sis, int bab){
    queue<int>que;
    int cor, cnt =1;
    que.push(sis);
    space[sis] = 1;
    
    while(!que.empty()){
        cor = que.front();
        que.pop();
        //printf("sis: %d\n", cor);
        
        if(cor - 1 >= 0 && space[cor - 1] == 0){
            cnt++;
            que.push(cor - 1);
            space[cor - 1] = space[cor] + 1;
        }
        if(cor + 1 <= 100000 && space[cor + 1] == 0){
            cnt++;
            que.push(cor + 1);
            space[cor + 1] = space[cor] + 1;
        }
        if(cor * 2 <= 100000 && space[cor * 2] == 0){
            cnt++;
            que.push(cor * 2);
            space[cor * 2] = space[cor] + 1;
        }
    }
    
    return space[bab];
}
