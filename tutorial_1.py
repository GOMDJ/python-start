text = """
인공지능과 자연어처리는 정말 흥미로운 분야입니다.
자연어처리 기술이 발전하면서 많은 것들이 가능해졌습니다.
"""

words = text.split()
print(f"총 단어 개수: {len(words)}")
print(f"가장 긴 단어: {max(words, key=len)}")