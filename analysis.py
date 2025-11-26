import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

font_path = "C:/Windows/Fonts/malgun.ttf"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv("subway.csv", encoding="utf-8-sig", index_col=False)

df["승차총승객수"] = pd.to_numeric(df["승차총승객수"], errors="coerce")
df["하차총승객수"] = pd.to_numeric(df["하차총승객수"], errors="coerce")

df["총이용객"] = df["승차총승객수"] + df["하차총승객수"]

# ⭐ 역명 기준으로 합계 묶기 (이게 핵심)
df_grouped = df.groupby("역명")["총이용객"].sum().reset_index()

# ⭐ 여기서 TOP10 뽑기
top10 = df_grouped.sort_values("총이용객", ascending=False).head(10)

print(top10)

plt.figure(figsize=(12, 6))
plt.barh(top10["역명"], top10["총이용객"])
plt.xlabel("이용객 수")
plt.ylabel("역 이름")
plt.title("서울 지하철 혼잡역 TOP 10 (역별 합계 기준)")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()
