<h2><a href="https://codeforces.com/contest/1843/problem/C" target="_blank" rel="noopener noreferrer">1843C — Sum in Binary Tree</a></h2>

| | |
|---|---|
| **Difficulty** | 800 |
| **Language** | PyPy 3-64 |
| **Verdict** | ✅ Accepted |
| **Problem Link** | [Codeforces 1843C](https://codeforces.com/contest/1843/problem/C) |

## Topics
`bitmasks` `combinatorics` `math` `trees`

---

## Problem Statement

<div class="header"><div class="title">C. Sum in Binary Tree</div><div class="time-limit"><div class="property-title">time limit per test</div>1 second</div><div class="memory-limit"><div class="property-title">memory limit per test</div>256 megabytes</div><div class="input-file input-standard"><div class="property-title">input</div>standard input</div><div class="output-file output-standard"><div class="property-title">output</div>standard output</div></div><div><p>Vanya really likes math. One day when he was solving another math problem, he came up with an interesting tree. This tree is built as follows.</p><p>Initially, the tree has only one vertex with the number $$$1$$$ — the root of the tree. Then, Vanya adds two children to it, assigning them consecutive numbers — $$$2$$$ and $$$3$$$, respectively. After that, he will add children to the vertices in increasing order of their numbers, starting from $$$2$$$, assigning their children the minimum unused indices. As a result, Vanya will have an infinite tree with the root in the vertex $$$1$$$, where each vertex will have exactly two children, and the vertex numbers will be arranged sequentially by layers.</p><center> <img class="tex-graphics" src="https://espresso.codeforces.com/19767bb6961374fcead1e1f59f5391d1b3248808.png" style="max-width: 100.0%;max-height: 100.0%;">   <span class="tex-font-size-small">Part of Vanya's tree.</span> </center><p>Vanya wondered what the sum of the vertex numbers on the path from the vertex with number $$$1$$$ to the vertex with number $$$n$$$ in such a tree is equal to. Since Vanya doesn't like counting, he asked you to help him find this sum.</p></div><div class="input-specification"><div class="section-title">Input</div><p>The first line contains a single integer $$$t$$$ ($$$1 \le t \le 10^4$$$) — the number of test cases.</p><p>This is followed by $$$t$$$ lines — the description of the test cases. Each line contains one integer $$$n$$$ ($$$1 \le n \le 10^{16}$$$) — the number of vertex for which Vanya wants to count the sum of vertex numbers on the path from the root to that vertex.</p></div><div class="output-specification"><div class="section-title">Output</div><p>For each test case, print one integer — the desired sum.</p></div><div class="sample-tests"><div class="section-title">Example</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id0008251525771791401" id="id009088262166117533" class="input-output-copier">Copy</div></div><pre id="id0008251525771791401"><div class="test-example-line test-example-line-even test-example-line-0">6</div><div class="test-example-line test-example-line-odd test-example-line-1">3</div><div class="test-example-line test-example-line-even test-example-line-2">10</div><div class="test-example-line test-example-line-odd test-example-line-3">37</div><div class="test-example-line test-example-line-even test-example-line-4">1</div><div class="test-example-line test-example-line-odd test-example-line-5">10000000000000000</div><div class="test-example-line test-example-line-even test-example-line-6">15</div></pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id006723949683937671" id="id007989027893941042" class="input-output-copier">Copy</div></div><pre id="id006723949683937671">4
18
71
1
19999999999999980
26
</pre></div></div></div><div class="note"><div class="section-title">Note</div><p>In the first test case of example on the path from the root to the vertex $$$3$$$ there are two vertices $$$1$$$ and $$$3$$$, their sum equals $$$4$$$.</p><p>In the second test case of example on the path from the root to the vertex with number $$$10$$$ there are vertices $$$1$$$, $$$2$$$, $$$5$$$, $$$10$$$, sum of their numbers equals $$$1+2+5+10 = 18$$$. </p></div>