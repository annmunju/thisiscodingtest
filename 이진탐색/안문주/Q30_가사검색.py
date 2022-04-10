words = ['frodo', 'front', 'frost', 'frozen', 'frame', 'kakao']
queries = ['fro??', '????o', 'fr???', 'fro???', 'pro?']


def solution(words, queries):

    answer = []

    for query in queries:

        same_cnt = []
        for word in words:
            if len(word) == len(query):
                same_cnt.append(word)

        if query[0] == '?':
            # 왼쪽 물음표
            key = query.split('?')[-1]
            end = len(query)
            start = end-len(key)
            cnt = 0

            for i in same_cnt:
                if i[start:end] == key:
                    cnt += 1

        else:
            # 오른쪽 물음표
            key = query.split('?')[0]
            start = 0
            end = len(key)
            cnt = 0

            for i in same_cnt:
                if i[start:end] == key:
                    cnt += 1

        answer.append(cnt)

    return answer

print(solution(words, queries))