# permutation 구현
# permutation: 서로 다른 n개의 원소에서 r개를 중복없이 골라 순서대로 나열하는 경우의 수

# 재귀를 이용한 구현 - 원소를 하나씩 뽑아서 수열을 구성하고 출력

def permutation(arr,r):
    arr=sorted(arr)
    # used: i번째 값을 썻는지 저장하는데 쓰인다.
    used=[0 for _ in range(len(arr))]

    # 실제 순열을 만들 generate 함수를 생성
    # chosen: 순열의 원소가 저장되는 변수
    def generate(chosen,used):
        if len(chosen)==r:
            print(chosen)
            return

        for i in range(len(arr)):
            # chosen에 값을 하나씩 저장하다가 그 개수가 r이 되는 순간
            # 하나의 순열이 만들어진 것이므로
            # 출력 후 종료한다.
            if not used[i]:
                # chosen에 값 추가 후 해당 i번째 변수를 사용했다고 1로 표시
                chosen.append(arr[i])
                used[i]=1
                # generate 반복
                generate(chosen,used)
                # 순열 하나가 만들어 지면 0으로 사용안함으로 표시
                used[i]=0
                chosen.pop()

    generate([], used)

print(permutation('ABCD', 2))