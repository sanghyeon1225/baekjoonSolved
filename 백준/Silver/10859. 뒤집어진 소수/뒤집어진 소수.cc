#include <iostream>
#include <string>
using namespace std;

bool is_prime(long long num) {
    if (num < 2) return false;
    for (long long i = 2; i * i <= num; ++i)
        if (num % i == 0) return false;
    return true;
}

int main() {
    string n;
    cin >> n;
    string rotated = "";

    for (int i = n.length() - 1; i >= 0; --i) {
        char c = n[i];
        if (c == '3' || c == '4' || c == '7') {
            cout << "no\n";
            return 0;
        }
        else if (c == '6') rotated += '9';
        else if (c == '9') rotated += '6';
        else rotated += c;
    }

    long long original_num = stoll(n);
    long long rotated_num = stoll(rotated);

    if (is_prime(original_num) && is_prime(rotated_num))
        cout << "yes\n";
    else
        cout << "no\n";

    return 0;
}
