<h2><a href="https://codeforces.com/contest/1527/problem/A" target="_blank" rel="noopener noreferrer">1527A — And Then There Were K</a></h2>

| | |
|---|---|
| **Difficulty** | 800 |
| **Language** | PyPy 3-64 |
| **Verdict** | ✅ Accepted |
| **Problem Link** | [Codeforces 1527A](https://codeforces.com/contest/1527/problem/A) |

## Topics
`bitmasks`

---

## Problem Statement

<div class="header"><div class="title">A. And Then There Were K</div><div class="time-limit"><div class="property-title">time limit per test</div>1 second</div><div class="memory-limit"><div class="property-title">memory limit per test</div>256 megabytes</div><div class="input-file input-standard"><div class="property-title">input</div>standard input</div><div class="output-file output-standard"><div class="property-title">output</div>standard output</div></div><div><p>Given an integer $$$n$$$, find the maximum value of integer $$$k$$$ such that the following condition holds: </p><center> $$$n$$$ & ($$$n-1$$$) & ($$$n-2$$$) & ($$$n-3$$$) & ... ($$$k$$$) = $$$0$$$ </center> where & denotes the <a href="https://en.wikipedia.org/wiki/Bitwise_operation#AND">bitwise AND operation.</a></div><div class="input-specification"><div class="section-title">Input</div><p>The first line contains a single integer $$$t$$$ ($$$1 \le t \le 3 \cdot 10^4$$$). Then $$$t$$$ test cases follow.</p><p>The first line of each test case contains a single integer $$$n$$$ ($$$1 \le n \le 10^9$$$).</p></div><div class="output-specification"><div class="section-title">Output</div><p>For each test case, output a single integer — the required integer $$$k$$$.</p></div><div class="sample-tests"><div class="section-title">Example</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id0000985968801470316" id="id008210519619204176" class="input-output-copier">Copy</div></div><pre id="id0000985968801470316">3
2
5
17
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id008627818856362895" id="id009728548470547473" class="input-output-copier">Copy</div></div><pre id="id008627818856362895">1
3
15
</pre></div></div></div><div class="note"><div class="section-title">Note</div><p>In the first testcase, the maximum value for which the continuous & operation gives 0 value, is 1.</p><p>In the second testcase, the maximum value for which the continuous & operation gives 0 value, is 3. No value greater then 3, say for example 4, will give the & sum 0. </p><ul> <li> $$$5 \, \& \, 4 \neq 0$$$, </li><li> $$$5 \, \& \, 4 \, \& \, 3 = 0$$$. </li></ul><p>Hence, 3 is the answer.</p></div>