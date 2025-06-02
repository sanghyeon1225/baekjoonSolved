#include <iostream>
#include <vector>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<int> A(N), B(N);
    for (int i = 0; i < N; ++i) cin >> A[i];
    for (int i = 0; i < N; ++i) cin >> B[i];

    // X, Y를 1부터 100까지 브루트포스
    bool possible = false;
    for (int X = 1; X <= 100 && !possible; ++X) {
        for (int Y = 1; Y <= 100 && !possible; ++Y) {
            bool ok = true;
            for (int i = 0; i < N - 1 && ok; ++i) {
                for (int j = i + 1; j < N && ok; ++j) {
                    int diff = (A[i] - A[j]) * X + (B[i] - B[j]) * Y;
                    if (diff <= 0) ok = false;
                }
            }
            if (ok) possible = true;
        }
    }
    cout << (possible ? "YES" : "NO") << endl;
    return 0;
}
