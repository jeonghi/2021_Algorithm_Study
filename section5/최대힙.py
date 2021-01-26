def solution(prompt):
    import heapq
    heap = []
    for p in prompt:
        if p > 0 :
            heapq.heappush(heap, -p)
        elif p == 0 :
            if heap :
                print(-1*heapq.heappop(heap))
            else:
                print(-1)
        else:
            return





if __name__ == "__main__" :

    import sys
    sys.stdin = open("testCase/input10.txt")
    prompt = []
    for line in sys.stdin:
        prompt.append(int(line.strip()))
    solution(prompt)