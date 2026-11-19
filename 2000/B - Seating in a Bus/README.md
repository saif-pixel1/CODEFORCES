<h2><a href="https://codeforces.com/contest/2000/problem/B" target="_blank" rel="noopener noreferrer">2000B — Seating in a Bus</a></h2>

| | |
|---|---|
| **Difficulty** | 800 |
| **Language** | PyPy 3-64 |
| **Verdict** | ✅ Accepted |
| **Problem Link** | [Codeforces 2000B](https://codeforces.com/contest/2000/problem/B) |

## Topics
`two pointers`

---

## Problem Statement

<div class="header"><div class="title">B. Seating in a Bus</div><div class="time-limit"><div class="property-title">time limit per test</div>2 seconds</div><div class="memory-limit"><div class="property-title">memory limit per test</div>256 megabytes</div><div class="input-file input-standard"><div class="property-title">input</div>standard input</div><div class="output-file output-standard"><div class="property-title">output</div>standard output</div></div><div><p>In Berland, a bus consists of a row of $$$n$$$ seats numbered from $$$1$$$ to $$$n$$$. Passengers are advised to always board the bus following these rules: </p><ul> <li> If there are no occupied seats in the bus, a passenger can sit in any free seat;</li><li> Otherwise, a passenger should sit in any free seat that has at least one occupied neighboring seat. In other words, a passenger can sit in a seat with index $$$i$$$ ($$$1 \le i \le n$$$) only if at least one of the seats with indices $$$i-1$$$ or $$$i+1$$$ is occupied. </li></ul><p>Today, $$$n$$$ passengers boarded the bus. The array $$$a$$$ chronologically records the seat numbers they occupied. That is, $$$a_1$$$ contains the seat number where the first passenger sat, $$$a_2$$$ — the seat number where the second passenger sat, and so on.</p><p>You know the contents of the array $$$a$$$. Determine whether all passengers followed the recommendations.</p><p>For example, if $$$n = 5$$$, and $$$a$$$ = [$$$5, 4, 2, 1, 3$$$], then the recommendations were not followed, as the $$$3$$$-rd passenger sat in seat number $$$2$$$, while the neighboring seats with numbers $$$1$$$ and $$$3$$$ were free.</p></div><div class="input-specification"><div class="section-title">Input</div><p>The first line of input contains a single integer $$$t$$$ ($$$1 \le t \le 10^4$$$) — the number of test cases.</p><p>The following describes the input test cases.</p><p>The first line of each test case contains exactly one integer $$$n$$$ ($$$1 \le n \le 2 \cdot 10^5$$$) — the number of seats in the bus and the number of passengers who boarded the bus.</p><p>The second line of each test case contains $$$n$$$ <span class="tex-font-style-bf">distinct</span> integers $$$a_i$$$ ($$$1 \le a_i \le n$$$) — the seats that the passengers occupied in chronological order.</p><p>It is guaranteed that the sum of $$$n$$$ values across all test cases does not exceed $$$2 \cdot 10^5$$$, and that no passenger sits in an already occupied seat.</p></div><div class="output-specification"><div class="section-title">Output</div><p>For each test case, output on a separate line: </p><ul> <li> "<span class="tex-font-style-tt">YES</span>", if all passengers followed the recommendations; </li><li> "<span class="tex-font-style-tt">NO</span>" otherwise. </li></ul><p>You may output the answer in any case (for example, the strings "<span class="tex-font-style-tt">yEs</span>", "<span class="tex-font-style-tt">yes</span>", "<span class="tex-font-style-tt">Yes</span>", and "<span class="tex-font-style-tt">YES</span>" will be recognized as a positive answer).</p></div><div class="sample-tests"><div class="section-title">Example</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id003041748120766228" id="id0003616693954438721" class="input-output-copier">Copy</div></div><pre data-content="4
5
5 4 2 1 3
3
2 3 1
4
2 3 1 4
5
1 2 3 5 4
" id="id003041748120766228"><div class="test-example-line test-example-line-even test-example-line-0">4</div><div class="test-example-line test-example-line-odd test-example-line-1">5</div><div class="test-example-line test-example-line-odd test-example-line-1">5 4 2 1 3</div><div class="test-example-line test-example-line-even test-example-line-2">3</div><div class="test-example-line test-example-line-even test-example-line-2">2 3 1</div><div class="test-example-line test-example-line-odd test-example-line-3">4</div><div class="test-example-line test-example-line-odd test-example-line-3">2 3 1 4</div><div class="test-example-line test-example-line-even test-example-line-4">5</div><div class="test-example-line test-example-line-even test-example-line-4">1 2 3 5 4</div></pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id005251688924903396" id="id0021414204350264554" class="input-output-copier">Copy</div></div><pre id="id005251688924903396">NO
YES
YES
NO</pre></div></div></div><div class="note"><div class="section-title">Note</div><p>The first test case is explained in the problem statement.</p></div>