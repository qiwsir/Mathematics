# 可逆矩阵

《机器学习数学基础》第2章2.3.1节阐述了可逆矩阵的定义、性质，并演示了Python中的计算函数及其应用。

若一个矩阵存在逆矩阵，则称之为可逆矩阵，或者非奇异矩阵。

并不是所有的矩阵都是可逆矩阵。

如果矩阵可逆，用手工计算，通过高斯消元法可以得到其逆矩阵。

## 2阶逆矩阵公式

设 $\pmb{A}=\begin{bmatrix}a&b\\c&d\end{bmatrix}$ 是 $2\times2$ 可逆矩阵，则其逆矩阵公式：

$\pmb{A}^{-1}=\frac{1}{ad-bc}\begin{bmatrix}d&-b\\-c&a\end{bmatrix}$

其推导过程如下：

$\begin{split}\left[\begin{array}{c c|c c}a&b&1&0\\c&d&0&1\end{array}\right] &\to \left[\begin{array}{c c|c c}a&b&1&0\\0&ad-bc&-c&a\end{array}\right]\\&\to\left[\begin{array}{c c|c c}a&b&1&0\\0&1&\frac{-c}{ad-bc}&\frac{a}{ad-bc}\end{array}\right]\\&\to\left[\begin{array}{c c|c c}a&0&\frac{ad}{ad-bc}&\frac{-ab}{ad-bc}\\0&1&\frac{-c}{ad-bc}&\frac{a}{ad-bc}\end{array}\right]\\&\to\left[\begin{array}{c c|c c}1&0&\frac{d}{ad-bc}&\frac{-b}{ad-bc}\\0&1&\frac{-c}{ad-bc}&\frac{a}{ad-bc}\end{array}\right]\end{split}$

故，矩阵 $\pmb{A}$ 可逆的充要条件是 $|\pmb{A}|=ad-bc\ne0$ 。

## 3阶你矩阵公式

