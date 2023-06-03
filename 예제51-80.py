# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# +
#51

movie_rank = ['닥터 스트레인지','스플릿','럭키']
# -

movie_rank.append("베트맨")
print(movie_rank)

movie_rank.insert(1, "슈퍼맨")
print(movie_rank)

del movie_rank[3]
print(movie_rank)

del movie_rank[2]
del movie_rank[2]
print(movie_rank)

# +
lang1 = ["C","C++","JAVA"]
lang2 = ["Python","Go","C#"]

langs = lang1 + lang2
print(langs)

# +
nums = [1, 2, 3, 4, 5, 6, 7]

print("max:", max(nums))
print("min:", min(nums))
# -

nums = [1, 2, 3, 4, 5]
print(sum(nums))

# +
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]

print(len(cook))
# -

nums = [1, 2, 3, 4, 5]
average = sum(nums)/len(nums)
print(average)

price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2]) # 리스트 전체에서 인덱스 0부터 2씩 증가시키면서 요소를 가져옴

print(nums[1::2])

print(nums[::-1])

interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[::2])

interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(" ".join(interest))

print("/".join(interest))

print("\n".join(interest))

string = "삼성전자/LG전자/Naver"
interest = string.split("/")
print(interest)

data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
print(data)

#71
my_variable = ()
print(type(my_variable))

movie_rank={'닥터 스트레인지','스플릿','럭키'}

movie_rank

my_tuple=(1)
type(my_tuple)

mu_tuple=(1,)

interest = ('삼성전자', 'LG전자', 'SK Hynix')
data = list(interest)

data = tuple(interest)

temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)

data = tuple(range(2,100,2))
print(data)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[1:5:2])

print(nums[3:5:2])


