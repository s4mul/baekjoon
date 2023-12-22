int main()
{
    int truth_person[51] = {0}, party[50][51];
    int N, M, able_party, truth_person_amount;
    int isFalseParty;
    
    scanf("%d %d", &N, &M);
    scanf("%d", &truth_person_amount);
    for(int i = 0; i < truth_person_amount; i++){
        scanf("%d", truth_person);//0번째 사람을 tmp값으로 사용
        truth_person[truth_person[0]] = 1;
    } //사실을 알고있는 인간과 그렇지 않은 인간으로만 구분하면 됨.
    
  
    for(int i = 0; i < M; i++){//사실을 들어서 알고있을 사람을 표시
        scanf("%d", &party[i][0]);
        isFalseParty = 0;
        
        for(int j = 1; j <= party[i][0]; j++){
            scanf("%d", &party[i][j]);
            if(truth_person[party[i][j]]) isFalseParty = 1;//party[i][j] = tmp
        }
        
        if(isFalseParty){
            for(int j = 1; j <= party[i][0]; j++){
                truth_person[party[i][j]] = 1;
            }
        }
        
    
    }
    
    able_party = 0;
    for(int i = 0; i < M; i++){
        isFalseParty = 0;
        for(int j = 1; j <= party[i][0]; j++){
            if(truth_person[party[i][j]]) isFalseParty = 1;
        }
        able_party += isFalseParty;
    }
    
    printf("%d", M - able_party);

    return 0;
}
