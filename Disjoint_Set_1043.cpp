#include <iostream>

using namespace std;

typedef struct person{
    int ID;
    person* next;
}person;

person* find(person* attendant);
void margeGroup(person* attendantMaster, person* attendantSlave, int priorityID);

int main()
{
    person people[51];
    for(int i = 0; i < 51; i++){
        people[i].next = &people[i];
        people[i].ID = i;
    }//make all head 
    
    int N, M, truthPeople, privID, ID, priorityID, partyPeople, cnt;
    int party[51][51];
    
    scanf("%d %d",&N, &M);
    scanf("%d", &truthPeople);
    
    for(int i = 1; i < truthPeople; i++){
        scanf("%d", &party[0][i]);
    }
    priorityID = people[party[0][1]].ID;//head -> 사실을 알고 있는 집단을 최고우위로 만들어줌
    if(truthPeople == 0) priorityID = -1;// 사실을 알고 있는 사람이 없는 경우라면 아무도 지정되지 않도록 -1을 지정해줌
    for(int i = 1; i < truthPeople; i++){
        margeGroup(people + party[0][i], people + party[0][i + 1], priorityID);
    }//merge all truth person
    for(int i = 1; i <= M; i++){
        scanf("%d",&partyPeople);
        party[i][0] = partyPeople;
        for(int j = 1; j <= partyPeople; j++){
            scanf("%d",&party[i][j]);
        }
        for(int j = 1; j <= partyPeople - 1; j++){
            margeGroup(people + party[i][j],people + party[i][j + 1], priorityID);
        }
    }//해당 과정이 모두 끝나면 그룹화가 끝남
    
    cnt = 0;
    for(int i = 1; i < M; i++){
        for(int j = 1; j < party[i][j]; j++){
            if(find(&people[party[i][j]])->ID == priorityID){
                break;
            }
        }
        cnt++;
    }
    printf("%d", cnt);
    return 0;
}
person* find(person* attendant){
    if(attendant->ID == attendant->next->ID){
        return attendant;
    }
    return find(attendant->next);
}
void margeGroup(person* attendantMaster, person* attendantSlave, int priorityID){
    if(attendantSlave->ID == priorityID){
        find(attendantMaster)->next = find(attendantSlave);
    }
    else{
        find(attendantSlave)->next = find(attendantMaster);
    }
}
