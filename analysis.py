import pandas as pd
import matplotlib.pyplot as plt

# 1. CSV 불러오기
df = pd.read_csv("subway.csv", encoding="utf-8")

# 2. 필요한 컬럼만 선택
# 예시 컬럼: 사용월, 호선명, 역명, 승차총승객수, 하차총승객수
df = df[["사용월", "호선명", "역명", "승차총승객수", "하차총승객수"]]

# 3. 역별 총 이용객수 계산 (승차 + 하차)
df["총이용객"] = df["승차총승객수"] + df["하차총승객수"]

# 4. 상위 10개 혼잡역 찾기
top10 = df.sort_values("총이용객", ascending=False).head(10)

print("🚇 서울 지하철 혼잡역 TOP 10")
print(top10[["역명", "총이용객"]])

# 5. 시각화
plt.figure(figsize=(12, 6))
plt.barh(top10["역명"], top10["총이용객"])
plt.xlabel("이용객 수")
plt.title("서울 지하철 혼잡역 TOP 10")
plt.gca().invert_yaxis()
plt.show()
