# 求解线性方程组

《机器学习数学基础》中并没有将解线性方程组作为重点，只是在第2章2.4.2节做了比较完整的概述。这是因为，如果用程序求解线性方程组，相对于高等数学教材中强调的手工求解，要简单得多了。

这里拓展一下与线性方程组有关或者由线性方程组引发的知识。

## 线性方程组的解位于一条直线

不是一般性，这里讨论三维空间的情况，对于多维空间，可以由此外推，毕竟三维空间便于想象和作图说明。

设矩阵 $\pmb{A}=\begin{bmatrix}1&2&4\\1&3&5\end{bmatrix}$ ，线性方程

$\begin{bmatrix}1&2&4\\1&3&5\end{bmatrix}\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}=\begin{bmatrix}0\\0\end{bmatrix} \tag{1.1}$

的解是：

$\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}=\begin{bmatrix}0\\0\\0\end{bmatrix},\begin{bmatrix}2\\1\\-1\end{bmatrix},\begin{bmatrix}4\\2\\-2\end{bmatrix},\cdots$

可以将上述解写成：

$\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}=\alpha\begin{bmatrix}2\\1\\-1\end{bmatrix} \tag{1.2}$

其中 $\alpha$ 为任意数。

很显然，（1.1）式是一条通过坐标系原点的直线。推而广之，可以说 $\pmb{Ax}=\pmb{0}$ 的解集是**一条过原点的直线**（记作：$l_1$ ）。

如果是非齐次线性方程组，例如：

$\begin{bmatrix}1&2&4\\1&3&5\end{bmatrix}\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}=\begin{bmatrix}4\\5\end{bmatrix} \tag{1.3}$

解为：

$\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}=\begin{bmatrix}2\\1\\0\end{bmatrix},\begin{bmatrix}0\\0\\1\end{bmatrix},\begin{bmatrix}4\\2\\-1\end{bmatrix},\cdots$

这些点的集合是一条不过原点的直线。即 $\pmb{Ax}=\pmb{b}$ 的解集是**一条不过原点的直线**（记作：$l_2$ ）。并且，这条直线与 $\pmb{Ax}=\pmb{0}$ 的解集所在直线平行。对此结论证明如下：

设 $\pmb{u}$ 和 $\pmb{v}$ 是 $\pmb{Ax}=\pmb{b}$ 的两个解，则：

$\begin{split}&\pmb{Au}=\pmb{b}\\&\pmb{Av}=\pmb{b}\end{split}$

上面二式相减，得：

$\pmb{A}(\pmb{u}-\pmb{v})=\pmb{0}$

即 $\pmb{u}-\pmb{v}$ 是 $\pmb{Ax}=\pmb{0}$ 的一个解。

$\pmb{u}$ 和 $\pmb{v}$ 是 $\pmb{Ax}=\pmb{b}$ 解集对应的直线上（ $l_2$ ）的两个点，则 $\pmb{u}-\pmb{v}$ 的方向必然在直线 $l_2$ 的方向上（或者在直线 $l_2$ 上，或者在于 $l_2$ 平行的直线上）。

又因为 $\pmb{u}-\pmb{v}$ 也是 $\pmb{Ax}=\pmb{0}$ 的解，所以 $\pmb{u}-\pmb{v}$ 在过原点的直线 $l_1$ 上。

因此，$l_1$ 平行于 $l_2$ ，即 $\pmb{Ax}=\pmb{b}$ 的解集所在直线不过原点，且平行于过原点的 $\pmb{Ax}=\pmb{0}$ 的解集所在直线。







## 参考文献

[1]. [https://ccjou.wordpress.com/2009/03/20/axb-和-ax0-的解集合有什麼關係？/](https://ccjou.wordpress.com/2009/03/20/axb-%e5%92%8c-ax0-%e7%9a%84%e8%a7%a3%e9%9b%86%e5%90%88%e6%9c%89%e4%bb%80%e9%ba%bc%e9%97%9c%e4%bf%82%ef%bc%9f/)

