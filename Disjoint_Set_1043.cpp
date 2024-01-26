
#include <iostream>

using namespace std;

typedef struct person{
    int ID;
    person* next;
}person;

void find();
void margeGroup();

int main()
{
    person people[50];
    for(int i; i < 50; i++){
        people[i].next = people[i];
        people[i].ID = i;
    }//make all head 
    
    int N, M, truthPeople, privID, ID, priorityID;
    int party[50][50];
    
    scanf("%d %d",&N, &M);
    scanf("%d", &truthPeople);
    for(int i = 0; i < truthPeople; i++){
        scanf("%d", &party[0][i])
    }
    for(int i = 0; i < truthPeople - 1; i++){
        margeGroup(people + party[0][0], people + party[0][i + 1]);
    }//merge all truth person
    
    priorityID = people[party[0][0]].ID;//head
    for(int i = 0; i < M; i++){
        
    }
    return 0;
}
