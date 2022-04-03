from sys import stdin

n = int(stdin.readline())
scores = dict()

for _ in range(n):
    name, kor, eng, math = stdin.readline().split()
    scores[name] = [int(kor), int(eng), int(math)]

def tuple_to_dict(sort_scores):
    scores = dict()
    for score in sort_scores:
        scores[score[0]] = [score[1][0], score[1][1], score[1][2]]
    return scores

# 이름 사전 순으로 증가하는 순서로
sort_scores = sorted(scores.items(), key=lambda x: x[0], reverse=False)

scores = tuple_to_dict(sort_scores)

# 수학점수 감소하는 순서로
sort_scores = sorted(scores.items(), key=lambda x: x[1][2], reverse=True)

scores = tuple_to_dict(sort_scores)

# 영어점수 증가하는 순서로
sort_scores = sorted(scores.items(), key=lambda x: x[1][1], reverse=False)

scores = tuple_to_dict(sort_scores)

# 국어점수 감소하는 순서로
sort_scores = list(sorted(scores.items(), key=lambda x: x[1][0], reverse=True))

for name in sort_scores:
    print(name[0])