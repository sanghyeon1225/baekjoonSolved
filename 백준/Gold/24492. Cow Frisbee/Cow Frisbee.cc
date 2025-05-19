#include <iostream>
#include <stack>
#include <iomanip>
#include <time.h>

using namespace std;

int main() {
    clock_t start = clock();
    // 친구의 수를 입력 받아 n에 저장함
    int n;
    cin >> n;

    // 친구들의 키를 저장할 크기가 n인 h 배열을 선언함
    int *h;
    h = new int[n];
    
    // 친구들의 키를 입력 받아 h 벡터에 순서대로 저장함
    for (int i = 0; i < n; i++) {
        cin >> h[i];
    }


    // 각 인덱스 별로 왼쪽에 자신보다 큰 값의 인덱스를 저장할 left 배열 생성
    int *left;
    left = new int[n];

    // 왼쪽 인덱스에 자신보다 큰 값이 있는지 확인하기 위해 왼쪽 값들을 저장할 stack 선언
    stack<int> stack;

    // 각 인덱스 별로 자신보다 작은 인덱스에 자신보다 큰 키를 갖는 가장 가까운 인덱스를 찾음
    for (int i = 0; i < n; i++) {
        // stack에 h[i]보다 키가 큰 원소를 찾을 때까지 stack을 pop함 
        while (!stack.empty() && h[stack.top()] < h[i]) {
            stack.pop();
        }
        // while문이 끝난 후, stack이 비어있지 않다면 stack의 맨 위에 h[i]보다 큰 원소가 있다는 의미이므로 stack의 top을 left[i]로 저장함
        if (!stack.empty()) {
            left[i] = stack.top(); 
        } 
        // 그렇지 않고 stack이 빌 때까지 pop했다면 h[i]보다 큰 원소가 없다는 의미이므로 -1을 저장함
        else {
            left[i] = -1;
        }
        // 해당 원소를 stack에 추가함
        stack.push(i);
    }

    // 각 인덱스 별로 오른쪽에 자신보다 큰 값의 인덱스를 저장할 right 배열 생성
    int *right;
    right = new int[n];

    // stack을 초기화함
    while (!stack.empty()) {
        stack.pop();
    }

    // 각 인덱스 별로 자신보다 큰 인덱스에 자신보다 큰 키를 갖는 가장 가까운 인덱스를 찾음
    for (int i = n - 1; i > -1; i--) {
        while (!stack.empty() && h[stack.top()] < h[i]) {
            stack.pop();
        }
         if (!stack.empty()) {
            right[i] = stack.top(); 
        } 
        else {
            right[i] = -1;
        }
        stack.push(i);
    }

    // 총 거리를 저장할 answer 선언
    long long answer = 0;

    // 모든 인덱스를 돌면서 원반을 던질 수 없는 경우를 제외하고 (left, right 값이 -1) i와 left, right 사이의 거리를 answer에 더함
    for (int i = 0; i < n; i++) {
        if (left[i] != -1) {
            answer += (i - left[i] + 1);
        }
        if (right[i] != -1) {
            answer += (right[i] - i + 1);
        }
    }
    cout << answer << endl;
    clock_t end = clock();

    // cout << "실행시간: " << (double)(end - start) / CLOCKS_PER_SEC << "초" << endl;
    
    return 0;
}