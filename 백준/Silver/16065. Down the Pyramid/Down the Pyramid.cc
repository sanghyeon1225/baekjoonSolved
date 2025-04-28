#include <cstdio>
#include <algorithm>

using namespace std;

int main() {
    int n;
    int *numList;
    int answer = 0;
    scanf("%d", &n);
    numList = new int[n];

    for (int i = 0; i < n; i++) {
        scanf("%d", &numList[i]);
    }

    int left = 0;
    int right = 1000000000;

    for (int i = 0 ; i < n; i++) {
        int newLeft = numList[i] - right;
        int newRight = numList[i] - left;

        left = max(newLeft, 0);
        right = newRight;
    }

    if (right < 0) {
        printf("%d", 0);
    }
    else {
        printf("%d", right - left + 1);
    }
    
}

