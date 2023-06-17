#include <iostream>

using namespace std;

int DP[41] = {0};
int DP_zero[41] = {0};
int DP_one[41] = {0};

int cnt_zero =0;
int cnt_one = 0;
int pivo(int value);
int main()
{
    int n, value;
    
    scanf("%d", &n);
    
    for(int i =0 ; i < n; i++){
        scanf("%d", &value);
        pivo(value);
        printf("%d %d\n",DP_zero[value],DP_one[value]);
    }
    
    
    return 0;
}
int pivo(int value){
    int prev_value, prev_prev_value;
    if(value == 0){
        cnt_zero++;
        DP_zero[0] = 1;
        
        return 0;
    } 
    if(value == 1){
        cnt_one++;
        DP_one[0] = 0;
        DP_one[1] = 1;
        return 1;  
    } 
    //무조껀 value가 1보다 클 때이므로 상관없음
    if(DP[value - 2] == 0){
        DP[value - 2] = pivo (value - 2);
    }
    prev_prev_value = DP[value - 2];
    
    if(DP[value - 1] == 0){
        DP[value - 1] = pivo(value-1);
    }
    prev_value = DP[value - 1];
    DP_one[value] = DP_one[value - 1] + DP_one[value - 2];
    DP_zero[value] = DP_zero[value - 1] + DP_zero[value - 2];
    
    return prev_value + prev_prev_value;
}
