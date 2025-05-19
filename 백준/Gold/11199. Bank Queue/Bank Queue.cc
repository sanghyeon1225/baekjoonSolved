#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Customer {
    int money;
    int deadline;
};

// 돈이 많은 순으로 정렬
bool compare(Customer a, Customer b) {
    return a.money > b.money;
}

int main() {
    int n, t;
    cin >> n >> t;

    vector<Customer> customers(n);
    for (int i = 0; i < n; ++i) {
        cin >> customers[i].money >> customers[i].deadline;
    }

    sort(customers.begin(), customers.end(), compare);

    // 시간별 예약 여부
    vector<bool> timeSlot(t, false);

    int total = 0;
    for (const auto& c : customers) {
        // 마감 시간 or 그 이전 가능한 시간 중 가장 늦은 시간에 배치
        for (int i = min(c.deadline, t - 1); i >= 0; --i) {
            if (!timeSlot[i]) {
                timeSlot[i] = true;
                total += c.money;
                break;
            }
        }
    }

    cout << total << endl;
    return 0;
}
