#include<stdio.h>
#include<stdlib.h>

#pragma warning(disable:4996)

void dfs(int depth, int n, int m, int* ar, int* visited, int priv);
int cnt = 0;

int main(void) {
	
	int N, M;
	scanf("%d %d", &N, &M);
	int ar[9];
	int visited[9];
	

	for (int i = 0; i < 9; i++) {
		ar[i] = 0;

	}
	for (int i = 0; i < 9; i++) {
		visited[i] = 0;

	}
	
	dfs(0, N, M, ar, visited, 0);
	//printf("%d", cnt);

}

void dfs(int depth, int n, int m, int* ar, int* visited, int priv) {
	if (depth == m) {
		for (int i = 0; i < m; i++) {
			printf("%d ", ar[i]);
		}
		printf("\n");
		return;
	}
	//1부터 n까지의 정점이 모두 서로 연결되어 있는 그래프라고 가정
	for (int i = 1; i <= n; i++) {//모든 정점에 대해서
		//cnt++;
		
			visited[i] = 1;
			ar[depth] = i;
			dfs(depth + 1, n, m, ar, visited, i);
			visited[i] = 0;
		
	}
}
