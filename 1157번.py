# 알파벳 대소문자 단어 -> 가장 많이 사용된 알파벳 출력 프로그램
# 첫째 줄에 알파벳 대소문자로 이루어진 단어 입력
# 첫째 줄에 단어에서 가장 많이 사용된 알파벳 대문자로 출력
# 가장 많이 사용된 알파벳이 여러개 존재할 경우 ?를 출

word = input().upper()
words = list(set(word))

cnt_list = []
for i in words :
    cnt = word.count(i)
    cnt_list.append(cnt)

if cnt_list.count(max(cnt_list)) > 1 :
    print("?")

else :
    max_index = cnt_list.index(max(cnt_list))
    print(words[max_index])
