# 用字典存成绩
scores = {}
n = int(input("要录入几个同学？"))

for i in range(n):
    name = input(f"第{i+1}个同学姓名：")
    score = float(input(f"{name}的成绩："))
    scores[name] = score

# 分析
score_list = list(scores.values())   # 所有成绩的列表
avg = sum(score_list) / len(score_list)
highest_name = max(scores, key=scores.get)  # 最高分是谁？

print("\n=== 成绩分析 ===")
print(f"总人数：{len(scores)}")
print(f"平均分：{avg:.1f}")           # 保留1位小数
print(f"最高分：{scores[highest_name]}（{highest_name}）")
print(f"最低分：{min(score_list)}")
print(f"及格人数：{sum(1 for s in score_list if s >= 60)}")

# 等级分类
for name, score in scores.items():
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 60:
        grade = "C"
    else:
        grade = "D"
    print(f"  {name}: {score} → {grade}")