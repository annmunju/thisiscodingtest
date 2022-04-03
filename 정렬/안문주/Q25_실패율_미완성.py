n = 5 # 전체 스테이지 개수
stages = [2, 1, 2, 6, 2, 4, 3, 3] # 게임 이용자의 스테이지 상태
fatal = dict()

# 실패율 : 스테이지에 도달했으나 클리어하지 못한 플레이어 수 / 스테이지 도달 플레이어의 수

stages.sort()
print(stages)

cnt = 0
idx = stages[0]
new_stages = stages

for i,s in enumerate(stages+[0]):

    if idx == s:
        cnt += 1

    elif idx != s:
        fatal[idx] = cnt/len(new_stages)
        new_stages = stages[i:]

        idx += 1
        if s in stages:
            cnt = 1
        else:
            cnt = 0

    # if s == 0:
    #     fatal[idx] = cnt/len(new_stages)

print(fatal)


# print(sorted(fatal.items(), key=lambda x:x[1], reverse=True))