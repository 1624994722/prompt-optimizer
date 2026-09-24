<div align="center">

# ⚡ Prompt Optimizer

**Turn casual words into prompts AI can actually execute.**

An intelligent AI Skill that transforms rough, colloquial input into well-structured, information-complete, token-efficient prompts

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Skill](https://img.shields.io/badge/Type-AI%20Skill-blueviolet)]()
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)]()

**English | [简体中文](README.md)**

</div>

---

## 📖 Introduction

Sound familiar?

- You type a quick "help me build something" — and the AI needs three rounds of clarification before it even starts?
- Your research question uses slightly wrong terminology, and the AI confidently runs in the wrong direction?
- Your prompts are polite and lengthy, burning tokens while the answers stay mediocre?

**Prompt Optimizer** is built for exactly this. It's an installable AI Skill that automatically rewrites any casual, incomplete, colloquial input into a **well-structured, information-complete, token-efficient** prompt — so the AI **gets it right on the first try**, with far fewer back-and-forth clarification rounds.

It incorporates **Anthropic's official prompt engineering best practices**, ships with dual template libraries for **research** and **coding**, infers your role and intent from context before rewriting, and self-learns domain knowledge before touching highly specialized research topics.

## ✨ Core Features

### 🧠 Automatic User Profiling & Granularity Alignment

Silently infers your **role, expertise depth, true goal, and desired outcome** from conversation context, then aligns the communication granularity:

| Granularity | Audience | Prompt Strategy |
|---|---|---|
| Coarse | Beginners / exploring | Asks the AI to offer options before diving in |
| Medium | Regular tasks | Direct, complete execution |
| Fine | Experts / urgent work | High information density, skip explanations |

No forms to fill. The profiling conclusion is delivered as a one-liner so you can correct any misjudgment.

### 🔬 Domain Self-Learning (Research Scenarios)

For highly specialized research topics, the skill **learns before it rewrites**:

1. Extracts core domain keywords and checks recent surveys to calibrate its understanding;
2. Verifies standard terminology, mainstream approaches, common datasets & metrics, and established baselines;
3. Digests findings into an internal "domain card" used to fix terminology drift, fill in accurate baselines/metrics, and set realistically achievable acceptance criteria.

> Say "help me with that batch effect thing in single-cell sequencing" — it calibrates to a professional prompt centered on scVI/scANVI, with Harmony as baseline and the scIB benchmark as the evaluation framework.

### 🏗️ Anthropic Official Prompt Engineering System

Eleven official core techniques built in, applied on demand rather than stacked blindly:

- **The Golden Rule of Clarity** — treat the AI as a "brilliant new employee with zero context"
- **XML Tag Structuring** — partition complex prompts with `<instructions>/<context>/<examples>`
- **Positive Framing** — tell the AI what to do, not what to avoid
- **Countable Hard Constraints** — "under 150 words, 3 bullet points" beats "be concise"
- **Few-shot examples, quote-grounding against hallucination, prompt chaining, think-and-verify, style mirroring**, and more

### 📚 Dual Scenario Template Libraries

- **Research ×7**: literature review, topic refinement, experiment design, paper polishing, statistical analysis, peer review, abstract writing
- **Coding ×7**: new features, bug fixing, code review, refactoring, code explanation, automation scripts, architecture decisions

Every scenario includes a complete "colloquial input → optimized output" example.

### 📊 Token Cost Comparison

Ships with `token_stats.py` to estimate token usage before and after optimization — quantifiable results at a glance.

## 🚀 Usage

### Installation

1. Download `prompt-optimizer.skill` from this repository;
2. Install it in an AI platform that supports Skills (e.g., Kimi).

### Triggering

No commands to memorize. Any of these will activate it:

- "Help me optimize this prompt: ..."
- "Turn this into an instruction for AI"
- "What's the best way to ask the AI?"
- Simply paste a rough idea you intended to send to an AI

### Example

**Input (colloquial):**

> Hi, could you help me write something to compress a bunch of images in a folder? They're too big to send. Thanks!

**Output (optimized prompt):**

```
Task: Write a Python CLI script to batch-compress images in a given folder.
Stack: Python 3.10+, Pillow only.
Requirements:
- Input: folder path (CLI arg); process all jpg/png/webp, including subfolders
- Output: save to compressed/ directory, preserving filenames and structure
- Target: ≤ 1MB per file, longest edge ≤ 1920px, JPEG quality stepped down from 85
- Edge cases: skip compliant files; report corrupt files but continue; print summary
Output: complete runnable script + one usage example.
Self-check against every requirement before finishing.
```

Politeness overhead removed, missing specs filled in, acceptance criteria defined — the AI delivers runnable code in one shot.

## 🗂️ Project Structure

```
prompt-optimizer/
├── SKILL.md                          # Core logic: seven-step workflow
├── references/
│   ├── official-techniques.md        # Anthropic official techniques library (11 entries)
│   ├── research-prompts.md           # Research templates + domain self-learning protocol
│   └── coding-prompts.md             # Coding templates
└── scripts/
    └── token_stats.py                # Token cost estimation & comparison
```

## 💡 Why It Matters

> **A great prompt isn't polite — it's precise.**

Every vague question accrues interest paid in clarification rounds. Prompt Optimizer automates the "think clearly before asking" part: it fills in context, calibrates terminology, aligns granularity, and compresses redundancy — you just say what you want, it handles the rest.

Whether you're a student racing a thesis deadline, a researcher chasing the frontier, or an engineer shipping against the clock — **make every conversation with AI hit the mark on the first try.**

If this project helps you, a ⭐ **Star** means a lot — and Issues/PRs to improve the template libraries are always welcome!

## 📄 License

[MIT](LICENSE)
