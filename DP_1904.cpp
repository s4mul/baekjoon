#include <iostream>

using namespace std;
int ar[1000001] = {0};
int main()
{
    int a;
    scanf("%d", &a);
    ar[0] = 1;
    ar[1] = 2;
    for(int i =2; i < a; i++){
        ar[i] = (ar[i - 1] + ar[i - 2])% 15746;//prevent int overflow
    }
    printf("%d", ar[a - 1] % 15746);
    return 0;
}
