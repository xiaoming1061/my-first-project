# -*- coding: utf-8 -*-
"""
我的第一个 Python 程序
用 Git 管理，推送到 GitHub
"""

def greet():
    """跟用户打招呼"""
    name = input("👉 你叫什么名字？ ")
    print(f"\n✨ 你好，{name}！欢迎来到 Python 的世界 🐍\n")


def show_fruits():
    """演示列表和循环"""
    fruits = ["🍎 苹果", "🍌 香蕉", "🍊 橘子", "🍇 葡萄", "🥝 猕猴桃"]
    
    print("我最喜欢的水果有：")
    for i, fruit in enumerate(fruits, start=1):
        print(f"  {i}. {fruit}")
    print()


def calculator():
    """演示简单的计算"""
    print("📝 来个快速加法：")
    try:
        a = float(input("  第一个数字："))
        b = float(input("  第二个数字："))
        result = a + b
        print(f"  ✅ {a} + {b} = {result}\n")
    except ValueError:
        print("  ❌ 请输入数字哦！\n")


def main():
    """主函数——程序入口"""
    print("=" * 40)
    print("   🐍 欢迎来到我的第一个 Python 程序")
    print("=" * 40)
    print()

    greet()
    show_fruits()
    calculator()

    print("-" * 40)
    print("程序运行结束，谢谢体验！👋")


# 程序从这里开始执行
if __name__ == "__main__":
    main()