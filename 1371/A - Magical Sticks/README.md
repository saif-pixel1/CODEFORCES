<h2><a href="https://codeforces.com/contest/1371/problem/A" target="_blank" rel="noopener noreferrer">1371A — Magical Sticks</a></h2>

| | |
|---|---|
| **Difficulty** | 800 |
| **Language** | PyPy 3-64 |
| **Verdict** | ✅ Accepted |
| **Problem Link** | [Codeforces 1371A](https://codeforces.com/contest/1371/problem/A) |

## Topics
`math`

---

## Problem Statement

<div class="header"><div class="title">A. Magical Sticks</div><div class="time-limit"><div class="property-title">time limit per test</div>1 second</div><div class="memory-limit"><div class="property-title">memory limit per test</div>256 megabytes</div><div class="input-file input-standard"><div class="property-title">input</div>standard input</div><div class="output-file output-standard"><div class="property-title">output</div>standard output</div></div><div><p>A penguin Rocher has $$$n$$$ sticks. He has exactly one stick with length $$$i$$$ for all $$$1 \le i \le n$$$.</p><p>He can connect some sticks. If he connects two sticks that have lengths $$$a$$$ and $$$b$$$, he gets one stick with length $$$a + b$$$. Two sticks, that were used in the operation disappear from his set and the new connected stick appears in his set and can be used for the next connections.</p><p>He wants to create the maximum number of sticks that have the same length. It is not necessary to make all sticks have the same length, some sticks can have the other length. How many sticks with the equal length he can create?</p></div><div class="input-specification"><div class="section-title">Input</div><p>The input consists of multiple test cases. The first line contains a single integer $$$t$$$ ($$$1 \le t \le 1000$$$) — the number of test cases. Next $$$t$$$ lines contain descriptions of test cases.</p><p>For each test case, the only line contains a single integer $$$n$$$ ($$$1 \le n \le 10^{9}$$$).</p></div><div class="output-specification"><div class="section-title">Output</div><p>For each test case, print a single integer  — the answer to the problem.</p></div><div class="sample-tests"><div class="section-title">Example</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id00044486619401316374" id="id0004907699716901748" class="input-output-copier">Copy</div></div><pre id="id00044486619401316374">4
1
2
3
4
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id008181916926838443" id="id008371492447474058" class="input-output-copier">Copy</div></div><pre id="id008181916926838443">1
1
2
2
</pre></div></div></div><div class="note"><div class="section-title">Note</div><p>In the third case, he can connect two sticks with lengths $$$1$$$ and $$$2$$$ and he will get one stick with length $$$3$$$. So, he will have two sticks with lengths $$$3$$$.</p><p>In the fourth case, he can connect two sticks with lengths $$$1$$$ and $$$3$$$ and he will get one stick with length $$$4$$$. After that, he will have three sticks with lengths $$$\{2, 4, 4\}$$$, so two sticks have the same length, and one stick has the other length.</p></div>