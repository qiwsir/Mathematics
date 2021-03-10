# 矩阵的秩

《机器学习数学基础》第2章2.5节“矩阵的秩”，介绍了矩阵的基本概念、性质以及如何用程序计算矩阵的秩。

## 零空间

在数学中，一个算子 $\pmb{A}$ 的零空间是方程 $\pmb{Av}=0$ 的所有解 $\pmb{v}$ 的集合。它也叫做 $\pmb{A}$ 的核或核空间。用集合建造符号表示为

$Null(\pmb{A})=\{\pmb{v}\in\mathbb{V}:\pmb{Av}=\pmb{0}\}$

如果算子是在向量空间上的线性算子，零空间就是线性子空间。因此零空间是向量空间。 

矩阵 $\pmb{A}$ 的零空间就是所有向量的空间的线性子空间。这个线性子空间的维度叫做 $\pmb{A}$ 的**零化度**（nullity），其值为矩阵 $\pmb{A}$ 的行阶梯形矩阵中不包含支点的纵列数$^{[1]}$。

例如矩阵 $\pmb{A}=\begin{bmatrix}-2&-4&4\\2&-8&0\\8&4&-12\end{bmatrix}$ ，首先将 $\pmb{A}$ 变换为简化行阶梯形矩阵：$\pmb{E}=\begin{bmatrix}1&0&-4/3\\0&1&-1/3\\0&0&0\end{bmatrix}$

对所有向量 $\pmb{v}$ 有 $\pmb{Av}=0$ ，等同于 $\pmb{Ev}=0$ ，即：

 $\begin{bmatrix}1&0&-4/3\\0&1&-1/3\\0&0&0\end{bmatrix}\begin{bmatrix}x\\y\\z\end{bmatrix}$

解得：$\begin{cases}x=\frac{4z}{3}\\y=\frac{z}{3}\\0=0\end{cases}$ ，即 $\begin{cases}x=\frac{4s}{3}\\y=\frac{s}{3}\\z=s\end{cases}$

所以，$\pmb{A}$ 的零空间是 $\pmb{v}=\begin{bmatrix}4s/3\\s/3\\s\end{bmatrix}$



## 参考文献

[1]. [https://zh.wikipedia.org/wiki/零空间](https://zh.wikipedia.org/wiki/%E9%9B%B6%E7%A9%BA%E9%97%B4)

