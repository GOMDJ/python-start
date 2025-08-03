text = """
인공지능과 자연어처리는 정말 흥미로운 분야입니다.
자연어처리 기술이 발전하면서 많은 것들이 가능해졌습니다.
"""

# 기존 기능
words = text.split()
print(f"총 단어 개수: {len(words)}")
print(f"가장 긴 단어: {max(words, key=len)}")

# 새로운 기능들
print(f"가장 짧은 단어: {min(words, key=len)}")
print(f"평균 단어 길이: {sum(len(word) for word in words) / len(words):.1f}자")

# 단어 빈도 계산
from collections import Counter
word_count = Counter(words)
print(f"가장 많이 나온 단어: {word_count.most_common(1)[0]}")