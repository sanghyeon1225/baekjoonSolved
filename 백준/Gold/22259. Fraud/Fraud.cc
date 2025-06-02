#include <iostream>
#include <vector>
#include <limits>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<long long> A(N), B(N);
    for (int i = 0; i < N; ++i) cin >> A[i];
    for (int i = 0; i < N; ++i) cin >> B[i];

    // Y = 1로 놓고 X의 범위 구하기
    double left = -1e18, right = 1e18;
    for (int i = 0; i < N - 1; ++i) {
        long long a = A[i] - A[i + 1];
        long long b = B[i] - B[i + 1];
        if (a == 0) {
            if (b <= 0) {
                // 불가능
                cout << "NO\n";
                return 0;
            }
            // b > 0이면 항상 성립
        } else if (a > 0) {
            // aX + b > 0 -> X > -b/a
            left = max(left, -double(b) / a);
        } else {
            // a < 0
            // aX + b > 0 -> X < -b/a
            right = min(right, -double(b) / a);
        }
    }
    // X > left, X < right, X > 0, X는 정수
    double l = max(left, 0.0);
    if (right - l > 1e-8) {
        cout << "YES\n";
        return 0;
    }
    // X = 1로 놓고 Y의 범위 구하기
    left = -1e18, right = 1e18;
    for (int i = 0; i < N - 1; ++i) {
        long long a = A[i] - A[i + 1];
        long long b = B[i] - B[i + 1];
        if (b == 0) {
            if (a <= 0) {
                cout << "NO\n";
                return 0;
            }
        } else if (b > 0) {
            left = max(left, -double(a) / b);
        } else {
            right = min(right, -double(a) / b);
        }
    }
    l = max(left, 0.0);
    if (right - l > 1e-8) {
        cout << "YES\n";
        return 0;
    }
    cout << "NO\n";
    return 0;
}
