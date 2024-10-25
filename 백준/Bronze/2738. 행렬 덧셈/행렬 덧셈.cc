#include <iostream>
#include <string>
using namespace std;


int main() {
    int n;
    int m;
    cin >> n;
    cin >> m;
    int a1[n][m];
    int a2[n][m];
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> a1[i][j];
        }
    }
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> a2[i][j];
        }
    }
    
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m - 1; j++) {
            cout << a1[i][j] + a2[i][j] << " ";
        }
        cout << a1[i][m-1] + a2[i][m-1] << endl;
    }
    
}