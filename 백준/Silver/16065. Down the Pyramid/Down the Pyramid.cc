#include <iostream>
#include <algorithm>
using namespace std;
const int INF = 0x3f3f3f3f3f;
const int maxn = 1000000 + 5;
int b[maxn];
int main() {
    int n;
    cin >> n;
    for (int i = 1; i <= n; i++)
        cin >> b[i];
    int mina1 = 0, maxa1 = INF;
    int temp = 0;

    for (int i = 1; i <= n; i++) {
        temp = b[i] - temp;
        if (i % 2)
            maxa1 = min(maxa1, temp);
        else
            mina1 = max(mina1, -temp);
    }
    // cout << mina1 << " " << maxa1 << endl;
    if (maxa1 >= mina1)
        cout << maxa1 - mina1 + 1;
    else
        cout << 0;
    return 0;
}