<h2><a href="https://codeforces.com/contest/2284/problem/B" target="_blank" rel="noopener noreferrer">2284B — Introduction to the Niche Internet</a></h2>

| | |
|---|---|
| **Difficulty** | Unrated |
| **Language** | PyPy 3-64 |
| **Verdict** | ✅ Accepted |
| **Problem Link** | [Codeforces 2284B](https://codeforces.com/contest/2284/problem/B) |

## Topics
_No tags available_

---

## Problem Statement

<div class="header"><div class="title">B. Introduction to the Niche Internet</div><div class="time-limit"><div class="property-title">time limit per test</div>1.5 seconds</div><div class="memory-limit"><div class="property-title">memory limit per test</div>256 megabytes</div><div class="input-file input-standard"><div class="property-title">input</div>standard input</div><div class="output-file output-standard"><div class="property-title">output</div>standard output</div></div><div><p>  </p><p>Having failed to become a grandmaster in two months, Nikolai was completely disappointed in a career in competitive programming and decided to switch to political streaming.</p><p>It's known that no streamer can exist without the support of their beloved viewers, so every stream Nikolai necessarily receives some number of donations, forming a sequence $$$a$$$. Note that Nikolai is watched by a large number of hackers, so some donations may have negative values.</p><p>Nikolai considers the $$$m$$$-th donation to be <span class="tex-font-style-it">very pleasant</span> if its size is at least the average of all previous donations, that is, $$$a_m \cdot (m - 1) \ge \sum\limits_{i=1}^{m-1} a_i$$$. In particular, the first donation is always <span class="tex-font-style-it">very pleasant</span>.</p><p>Nikolai considers the stream to have paid off if during the broadcast he receives <span class="tex-font-style-bf">exactly</span> $$$k$$$ <span class="tex-font-style-it">very pleasant</span> donations.</p><p>Nikolai knows that today he will receive $$$n$$$ donations from viewers, but he does not know in which order. Please help the viewers choose the order of sending donations so as to please Nikolai and make the stream pay off!</p></div><div class="input-specification"><div class="section-title">Input</div><p>Each test contains multiple test cases. The first line contains the number of test cases $$$t$$$ ($$$1 \le t \le 10^4$$$). The description of the test cases follows.</p><p>The first line of each test case contains two integers $$$n$$$ and $$$k$$$ ($$$1 \le k \le n \le 2 \cdot 10^5$$$) — the number of donations and the required number of <span class="tex-font-style-it">very pleasant</span> donations.</p><p>The second line of each test case contains $$$n$$$ integers $$$a_1, a_2, \ldots, a_n$$$ ($$$-10^9 \le a_i \le 10^9$$$) — the donation sizes.</p><p>It is guaranteed that the sum of $$$n$$$ over all test cases does not exceed $$$2 \cdot 10^5$$$.</p></div><div class="output-specification"><div class="section-title">Output</div><p>For each test case, output "<span class="tex-font-style-tt">NO</span>" if there is no suitable order of sending the donations.</p><p>Otherwise, output "<span class="tex-font-style-tt">YES</span>" on the first line, and on the second line output $$$n$$$ integers: the donation sizes in the order they are sent. If there are multiple solutions, output any of them.</p><p>You can output the answer in any case (upper or lower). For example, the strings "<span class="tex-font-style-tt">yEs</span>", "<span class="tex-font-style-tt">yes</span>", "<span class="tex-font-style-tt">Yes</span>", and "<span class="tex-font-style-tt">YES</span>" will be recognized as positive responses.</p></div><div class="sample-tests"><div class="section-title">Example</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id0022285048396251161" id="id0038880854731810854" class="input-output-copier">Copy</div></div><pre data-content="4
3 1
1 2 3
3 1
5 5 5
3 2
-1 -2 -3
4 3
0 0 10 -10
" id="id0022285048396251161"><div class="test-example-line test-example-line-even test-example-line-0">4</div><div class="test-example-line test-example-line-odd test-example-line-1">3 1</div><div class="test-example-line test-example-line-odd test-example-line-1">1 2 3</div><div class="test-example-line test-example-line-even test-example-line-2">3 1</div><div class="test-example-line test-example-line-even test-example-line-2">5 5 5</div><div class="test-example-line test-example-line-odd test-example-line-3">3 2</div><div class="test-example-line test-example-line-odd test-example-line-3">-1 -2 -3</div><div class="test-example-line test-example-line-even test-example-line-4">4 3</div><div class="test-example-line test-example-line-even test-example-line-4">0 0 10 -10</div></pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id00036041695016502895" id="id0014934585410098566" class="input-output-copier">Copy</div></div><pre id="id00036041695016502895">YES
3 2 1
NO
YES
-1 -3 -2
YES
10 -10 0 0</pre></div></div></div><div class="note"><div class="section-title">Note</div><p>In the first test case, one suitable order is $$$[3, 2, 1]$$$. The first donation is always <span class="tex-font-style-it">very pleasant</span>. The second is not <span class="tex-font-style-it">very pleasant</span>, since $$$2 \cdot 1  \lt  3$$$, and the third is not, since $$$1 \cdot 2  \lt  3 + 2$$$. Thus, exactly $$$1$$$ donation is <span class="tex-font-style-it">very pleasant</span>.</p><p>In the second test case, it can be shown that no suitable order exists.</p><p>In the third test case, one suitable order is $$$[-1, -3, -2]$$$. The first donation is <span class="tex-font-style-it">very pleasant</span>. The second is not <span class="tex-font-style-it">very pleasant</span>, since $$$(-3) \cdot 1  \lt  -1$$$, while the third is, since $$$(-2) \cdot 2 \ge -1 + (-3)$$$. Thus, exactly $$$2$$$ donations are <span class="tex-font-style-it">very pleasant</span>.</p></div>