#include <cstdio>
#include <vector>

using namespace std;

int main(){
    /*
    사용자의 입력을 저장할 변수 선언
    n = 논문의 마지막 페이지
    m = 바닥에 떨어진 논문의 장 수
    data = 바닥에 떨어진 논문의 페이지 번호
    */ 
    int n, m;
    int *data;

    // n, m에 해당하는 값을 입력 받음
    scanf("%d %d", &n, &m);
    
    // 떨어진 논문의 페이지의 방문 처리를 위해 n+1의 크기를 갖도록 data 배열을 할당함
    data = new int[n+1]();    
    
    // 떨어진 논문의 페이지를 한 장씩 입력 받아서 data 배열에서 해당 페이지(인덱스)의 값을 1로 바꿈 (방문 처리)
    for(int i = 0; i < m; i++) {
        int temp;
        scanf("%d", &temp);
        data[temp] = 1;
    }

    // 잃어버린 페이지를 저장할 lost vector 선언
    vector<int> lost;

    // data 배열을 돌면서 배열의 값이 0이라면(잃어버린 페이지라는 의미) lost 벡터에 현재 i값을 push해줌.
    for(int i = 1; i <= n; i++) {
        if(data[i] == 0) {
            lost.push_back(i);
        }
    }

    // ink = 사용해야 하는 잉크량 (초기값 = 0)
    // index = 출력해야하는 페이지를 저장할 변수 (초기값 = 0)
    int ink = 0;
    int index = 0;

    /* 
    lost 배열의 1번 인덱스부터 탐색을 시작함
    i번째 인덱스와 i-1번째 인덱스의 원소의 차이가(잃어버린 페이지들의 차이) 4 이상이라면 이들은 따로 출력해야 하는 경우임
    출력해야하는 페이지를 뜻하는 index와 i-1번째 페이지의 차이만큼 잉크량을 더해주고 index의 값을 현재 i로 바꿔줘서 다음 잉크량을 더할 때 해당 i부터 연산하도록 함
    */
    for (int i = 1; i < lost.size(); i++) {
        if((lost[i] - lost[i-1]) >= 4) {
            ink += (lost[i-1] - lost[index] + 1) * 2 + 5;
            index = i;
        }
    }
    
    // for문을 끝낸 후, index로 저장된 페이지부터 lost 벡터에 저장된 마지막 페이지까지 출력을 처리함
    // lost의 크기가 0일 경우 예외 처리를 해줘야 lost.back()에서 에러가 발생하지 않음
    if (lost.size() != 0) {
        ink += (lost.back() - lost[index] + 1) * 2 + 5;
    }
    
    // 위에서 구한 잉크량의 총합을 출력함
    printf("%d", ink);

    delete[] data;
    return 0;

}