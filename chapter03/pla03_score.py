english=int(input("英語の点数"))
math=int(input("数学の点数"))
score=""

if english<50 and math<50:
    score="C"
elif 50<=english<70 or 50<=math<70:
    score="B"
elif 70<=english<90 or 70<=math<90:
    score="A"
elif 90<=english or 90<=math:
    score="S"

print(f"あなたの成績は{score}です")
