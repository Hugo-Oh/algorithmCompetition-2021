import sys
sys.stdin = open("input.txt", "rt")

N = input()

# 9, 6을 한 세트로?
# 흠. dictionary가 가장 직관적이긴 한데....max값을 뽑아내는 느낌으로? count 해서, 각 값의 최댓값, 6이나 9 경우엔? /2가되겟지.
cnt = {}
for n in N:
    if n == "6" or n == "9":
        if "6" not in cnt:
            cnt["6"] = 1
        else:
            cnt["6"] +=1

    else:
        if n not in cnt:
            cnt[n] = 1

        else:
            cnt[n] += 1
if "6" in cnt:
    cnt["6"] = -(-cnt["6"] // 2) #올림

print(max(cnt.values()))