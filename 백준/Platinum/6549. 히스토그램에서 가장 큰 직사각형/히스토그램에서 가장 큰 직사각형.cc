#include <iostream>
#include <vector>
#include <stack>
#include <cmath>
#include <algorithm>

using namespace std;

class Histogram {
public:
    int height;
    int leftX;
    int rightX;

    Histogram() {
        leftX = rightX = height = 0; // 초기화 추가
    }

    Histogram(int index, int height) {
        this->leftX = index;
        this->rightX = this->leftX + 1;
        this->height = height;
    }
};

long long getLargestRectangleArea(const vector<Histogram>& histograms) {
    long long answer = 0;
    stack<Histogram> continuedHistograms;
    continuedHistograms.push(Histogram(-1, 0));

    for(int i = 0; i < histograms.size() + 1; i++) {
        Histogram h;
        if(i < histograms.size()) {
            h = histograms[i];
        } else {
            h = Histogram(histograms.size(), 0);
        }

        while (continuedHistograms.size() > 1 && continuedHistograms.top().height >= h.height) {
            Histogram lh = continuedHistograms.top();
            continuedHistograms.pop();

            Histogram bh = continuedHistograms.top();

            long long width = abs(h.leftX - bh.rightX);
            long long height = lh.height;
            long long area =  width * height;

            answer = max(answer, area);
        }

        continuedHistograms.push(h);
    }

    return answer;
}

// process가 종료 여부를 판단할 수 있도록 int로 변경
int process() {
    int n;
    cin >> n;
    if (n == 0) return 0;

    vector<Histogram> histograms;
    for(int i = 0 ; i < n ; i ++) {
        int height;
        cin >> height;
        histograms.push_back(Histogram(i, height));
    }

    long long answer = getLargestRectangleArea(histograms);
    cout << answer << endl;
    return 1;
}

int main() {
    while (true) {
        if (process() == 0) break;
    }
}
