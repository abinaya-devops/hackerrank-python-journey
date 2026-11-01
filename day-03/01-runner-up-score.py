n = int(input())
scores = list(map(int, input().split()))

unique_scores = set(scores)
unique_scores.remove(max(unique_scores))

print(max(unique_scores))
