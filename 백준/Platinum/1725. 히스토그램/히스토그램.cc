#include <iostream>
#include <vector>
#include <stack>
#include <cmath>
#include <algorithm>

using namespace std;

class Histogram {
public:
	int height;    // 히스토그램의 높이
	int leftX;     // 인덱스 혹은 히스토그램의 왼쪽 변의 x 좌표
	int rightX;    // 히스토그램의 오른쪽 변의 x좌표

	Histogram() { }

    // 생성자를 통해 히스토그램의 x좌표와 높이를 저장함
	Histogram(int index, int height) {
		this->leftX = index;
		this->rightX = this->leftX + 1;
		this->height = height;
	}

};


long long getLargestRectangleArea(const vector<Histogram>& histograms) {
	// 직사각형의 최대 넓이를 저장할 answer 할당
    long long answer = 0;

	// 현재 우측으로 확장 가능성이 있는 히스토그램들
	stack<Histogram> continuedHistograms;

	// 인덱스 계산을 쉽게 하기 위해 continuedHistograms 스택의 처음에 높이가 0인 히스토그램 추가
	continuedHistograms.push(Histogram(-1, 0));
	for(int i = 0 ; i < histograms.size() + 1 ; i++) {
        // 히스토그램의 원소들을 하나씩 조회하며 Histogram h 객체로 할당함
		Histogram h;
		if(i < histograms.size()) {
			h = histograms[i];
		} else { 
            // 종료 조건을 만족하기 위해 continuedHistograms 스택의 마지막에 높이가 0인 히스토그램 추가
			h = Histogram(histograms.size(), 0);
		}

		// 히스토그램의 높이가 오름차순으로 들어오는지 확인함 
		while (continuedHistograms.size() > 1
				&& continuedHistograms.top().height >= h.height){
			// 히스토그램이 오름차순으로 들어오지 않았다면 마지막에 추가된 히스토그램을 lh로 할당하고 pop함
            // 더 이상 확장 가능한 히스토그램이 아니기 때문에 pop 해줘야 함
			Histogram lh = continuedHistograms.top();
			continuedHistograms.pop();

			// 지금까지 확장된 히스토그램 중 마지막 히스토그램을 bh로 할당함
			Histogram bh = continuedHistograms.top();

			// 해당 히스토그램에서 만들어지는 직사각형의 넓이를 계산하여 area에 저장함
			long long width = abs(h.leftX - bh.rightX);
			long long height = lh.height;
			long long area =  width * height;

			// answer와 area 중 최대값을 구하여 answer에 할당함
			answer = max(answer, area);
		}

		// 이번 회차의 히스토그램 h를 스택에 저장함
		continuedHistograms.push(h);
	}

    // 모든 순회를 진행한 후, 최대 넓이를 return함
	return answer;
}

void process(int caseIndex) {
    // 히스토그램을 구성하는 기둥 수를 입력 받아 n에 저장함
	int n;
	cin >> n;

    // Histogram 객체들을 담을 histograms 벡터 생성
	vector<Histogram> histograms;

    // n번 반복하며 히스토그램의 높이를 입력 받아 histograms 벡터에 저장함
	for(int i = 0 ; i < n ; i ++) {
		int height;
		cin >> height;
		histograms.push_back(Histogram(i, height));
	}

    // getLargestRectangleArea() 함수를 호출하여 직사각형의 최대 넓이를 구하고 출력함
	long long answer = getLargestRectangleArea(histograms);
	cout << answer << endl;
}

int main() {
	process(1);
}