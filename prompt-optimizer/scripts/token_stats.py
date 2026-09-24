#!/usr/bin/env python3
"""估算并对比优化前后 prompt 的 token 开销。

用法:
    python3 token_stats.py --before before.txt --after after.txt
    python3 token_stats.py --text "直接传入的文本"

说明: 优先使用 tiktoken (cl100k_base) 精确计数; 未安装时退回启发式估算
(中文≈1 token/字, 英文≈0.75 token/词), 估算值仅供参考。
"""
import argparse
import re
import sys

def count_tokens(text: str) -> tuple[int, str]:
    try:
        import tiktoken
        enc = tiktoken.get_encoding("cl100k_base")
        return len(enc.encode(text)), "tiktoken(cl100k_base) 精确计数"
    except ImportError:
        zh = len(re.findall(r"[一-鿿　-〿＀-￯]", text))
        en_words = len(re.findall(r"[a-zA-Z0-9_]+", text))
        est = zh + int(en_words * 0.75)
        return est, "启发式估算(中文≈1token/字, 英文≈0.75token/词)"

def main() -> None:
    p = argparse.ArgumentParser(description="prompt token 开销估算与对比")
    p.add_argument("--before", help="优化前文本文件路径")
    p.add_argument("--after", help="优化后文本文件路径")
    p.add_argument("--text", help="直接传入一段文本统计")
    args = p.parse_args()

    if args.text is not None:
        n, method = count_tokens(args.text)
        print(f"token 数: {n}  ({method})")
        return

    if not (args.before and args.after):
        p.error("需要 --before 和 --after, 或 --text")

    b = open(args.before, encoding="utf-8").read()
    a = open(args.after, encoding="utf-8").read()
    nb, mb = count_tokens(b)
    na, _ = count_tokens(a)
    diff = nb - na
    pct = (diff / nb * 100) if nb else 0.0
    sign = "节省" if diff >= 0 else "增加"
    print(f"计数方式: {mb}")
    print(f"优化前: {nb} tokens | 优化后: {na} tokens | {sign} {abs(diff)} ({abs(pct):.1f}%)")
    if diff < 0:
        print("提示: 优化后变长通常是因为补全了必要上下文——只要换来一次命中, 总 token 仍可能更省。", file=sys.stderr)

if __name__ == "__main__":
    main()
