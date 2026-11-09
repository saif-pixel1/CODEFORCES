<h2><a href="https://codeforces.com/contest/2065/problem/B" target="_blank" rel="noopener noreferrer">2065B — Skibidus and Ohio</a></h2>

| | |
|---|---|
| **Difficulty** | 800 |
| **Language** | PyPy 3-64 |
| **Verdict** | ✅ Accepted |
| **Problem Link** | [Codeforces 2065B](https://codeforces.com/contest/2065/problem/B) |

## Topics
`strings`

---

## Problem Statement

<div class="header"><div class="title">B. Skibidus and Ohio</div><div class="time-limit"><div class="property-title">time limit per test</div>1 second</div><div class="memory-limit"><div class="property-title">memory limit per test</div>256 megabytes</div><div class="input-file input-standard"><div class="property-title">input</div>standard input</div><div class="output-file output-standard"><div class="property-title">output</div>standard output</div></div><div><p>Skibidus is given a string $$$s$$$ that consists of lowercase Latin letters. If $$$s$$$ contains more than $$$1$$$ letter, he can:</p><ul> <li> Choose an index $$$i$$$ ($$$1 \leq i \leq |s| - 1$$$, $$$|s|$$$ denotes the current length of $$$s$$$) such that $$$s_i = s_{i+1}$$$. Replace $$$s_i$$$ with any lowercase Latin letter of his choice. Remove $$$s_{i+1}$$$ from the string. </li></ul><p>Skibidus must determine the minimum possible length he can achieve through any number of operations.</p></div><div class="input-specification"><div class="section-title">Input</div><p>The first line contains an integer $$$t$$$ ($$$1 \leq t \leq 100$$$) — the number of test cases.</p><p>The only line of each test case contains a string $$$s$$$ ($$$1 \leq |s| \leq 100$$$). It is guaranteed $$$s$$$ only contains lowercase Latin letters.</p></div><div class="output-specification"><div class="section-title">Output</div><p>For each test case, output an integer on the new line, the minimum achievable length of $$$s$$$.</p></div><div class="sample-tests"><div class="section-title">Example</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id004747343567680863" id="id004737187439121334" class="input-output-copier">Copy</div></div><pre id="id004747343567680863"><div class="test-example-line test-example-line-even test-example-line-0">4</div><div class="test-example-line test-example-line-odd test-example-line-1">baa</div><div class="test-example-line test-example-line-even test-example-line-2">skibidus</div><div class="test-example-line test-example-line-odd test-example-line-3">cc</div><div class="test-example-line test-example-line-even test-example-line-4">ohio</div></pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id005426623321844594" id="id009119950087203078" class="input-output-copier">Copy</div></div><pre id="id005426623321844594">1
8
1
4
</pre></div></div></div><div class="note"><div class="section-title">Note</div><p>In the first test case, Skibidus can:</p><ul> <li> Perform an operation on $$$i = 2$$$. He replaces $$$s_2$$$ with <span class="tex-font-style-tt">b</span> and removes $$$s_3$$$ from the string. Then, $$$s$$$ becomes <span class="tex-font-style-tt">bb</span>. </li><li> Perform an operation on $$$i = 1$$$. He replaces $$$s_1$$$ with <span class="tex-font-style-tt">b</span> and removes $$$s_2$$$ from the string. Then, $$$s$$$ becomes <span class="tex-font-style-tt">b</span>. </li><li> Because $$$s$$$ only contains $$$1$$$ letter, Skibidus cannot perform any more operations. </li></ul><p>Therefore, the answer is $$$1$$$ for the first test case.</p><p>In the second test case, he cannot perform an operation on any index. Therefore, the answer is still the length of the initial string, $$$8$$$.</p></div>