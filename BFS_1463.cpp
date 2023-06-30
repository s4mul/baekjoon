#include <iostream>
#include<queue>

using namespace std;

int memory[1000001] = {0};
int BFS(int num);
int main()
{
   int n;
   scanf("%d", &n);
   printf("%d", BFS(n) - 1);
    return 0;
}

int BFS(int num){
    queue <int> que;
    int value, parent;
    
    que.push(num);
    memory[num] = 1;
    while(!que.empty()){
        value = que.front();
        que.pop();
        if(value == 1)
            return memory[value];
        parent = memory[value];
        if(value % 3 == 0 && (memory[value / 3] == 0 || memory[value / 3] > parent + 1)){
            que.push(value / 3);
            memory[value / 3] = parent + 1;
        }
        if(value % 2 == 0 && (memory[value / 2] == 0 || memory[value / 2] > parent + 1)){
            que.push(value / 2);
            memory[value / 2] = parent + 1;
        }
        if(value - 1 > 0 && (memory[value -1] == 0 || memory[value -1] > parent + 1)){
            que.push(value -1);
            memory[value -1] = parent + 1;
        }
        
    }
    
    return -1;
}
