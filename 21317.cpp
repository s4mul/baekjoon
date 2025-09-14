#include<iostream>
#pragma warning(disable: 4996)

using namespace std;

int main(void) {
    int N, k;//k: maxEn
    int dp[23][2] = { 0 };
    int arr[21][2] = { 0 };
    scanf_s("%d", &N);
    for (int i = 1; i < N; i++) {
        scanf_s("%d %d", &arr[i][0], &arr[i][1]);
    }
    scanf_s("%d", &k);

    for (int i = 2; i < N; i++) {
        dp[i][0] = 100000;
        dp[i][1] = 100000;
    }

    dp[1][0] = 0;
    dp[1][1] = 1000000;
    dp[2][1] = 1000000;
    dp[2][0] = arr[1][0];
    dp[3][0] = min(arr[1][1] + dp[1][0], arr[2][0] + dp[2][0]);
    dp[3][1] = 1000000;

    for (int i = 4; i <= N; i++) {
        dp[i][0] = min(arr[i - 1][0] + dp[i - 1][0], arr[i - 2][1] + dp[i - 2][0]);
        dp[i][1] = min(min(dp[i - 1][1] + arr[i - 1][0], dp[i - 2][1] + arr[i - 2][1]), dp[i - 3][0] + k);
            //dp[][0]는 이전에 개큰점프를 뛰지 않은 경우
            //dp[][1]은 이전에 개큰점프를 뛰거나 방금 뛰어서 온경우
            //따라서 dp[i][]는 한칸 전에서 작은점프 비용 + 이전까지 비용, 두칸 전에서 큰점프 비용 + 이전까지 비용
            //이때 개큰점프를 한 경우는 큰점프 한거에서 두개, 안한거에서 하나의 총 3개를 비교함.
    }

    printf("%d", min(dp[N][0], dp[N][1]));

}