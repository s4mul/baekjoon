#include <iostream>

using namespace std;

long long int ar[100];
int main()
{
    ar[0] = 1;
    ar[1] = 1;
    ar[2] = 1;
    
    int N, T;
    scanf("%d", &T);
    for(int i =3; i < 100; i++){
        ar[i] = ar[i - 2] + ar[i - 3];
    }
    for(int j =0; j < T; j++)
    {
        scanf("%d", &N);
        printf("%lld\n", ar[N - 1]);
    }
    
    return 0;
}
