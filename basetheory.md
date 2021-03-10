# 线性代数基本定理

Gilbert Strang认为线性代数有四个基本定理$^{[1]}$。

线性代数的核心问题是向量空间的线性变换，向量空间是线性代数的研究对象，线性变换是研究向量空间的基本方法。线性变换将一个向量空间的子空间映射到另一个向量空间中的子空间。

## 秩-零化度定理

以下关于“秩-零化度定理”（rank-nullity theorem）的阐述。以下内容主要参考文献[2]和[3]。

如下图所示，线性变换 $\pmb{T}:\mathbb{V}\to\mathbb{W}$ ，$\mathbb{V}$ 是有限维向量空间，称为**定义域**；$\mathbb{W}$ 也是有限维向量空间，称为**值域**，记作：$ran(\pmb{T})$ 或 $R(\pmb{T})$ 。 

![](https://gitee.com/qiwsir/images/raw/master/2021-3-10/1615346372410-base01.png)

- **核**：若 $\mathbb{V}$ 里面有一个向量集合，其中每个向量 $\pmb{u}$ 经 $\pmb{T}$ 映射之后为零向量，即 $\pmb{T}(\pmb{u})=\pmb{0}$ ，则此向量集合称为 $\pmb{T}$ 的**核**（kernel），记作：$\ker(\pmb{T})$ 。$ker(\pmb{T})$ 满足向量加法和数量乘法封闭性，是 $\mathbb{V}$ 的一个子空间。

- **零化度**：核的维度（dimension），称为**零化度**（nullity），记作：$\dim\ker(\pmb{T})$ 。可以度量核的大小。
- **秩**：线性变换 $\pmb{T}$ 的值域的维度，称为**秩**（rank），记作：$rank\pmb{T}=\dim R(\pmb{T})$ 。

### 秩—零化度定理

$\dim\mathbb{V}=\dim\ker(\pmb{T})+rank\pmb{T}$

其中： $\dim\mathbb{V}$ 是线性变换 $\pmb{T}$ 的定义域、向量空间 $\mathbb{V}$ 的维度；$\dim\ker(\pmb{T})$ 是核的维度，即零化度；$rank\pmb{T}$ 是值域的维度，即秩。

### 证明

**证明1：通过矩阵**

将线性变换 $\pmb{T}:\mathbb{V}\to\mathbb{W}$ 用 $m\times n$ 的矩阵 $\pmb{A}$ 表示，其中：$n = \dim\mathbb{V}, m=\dim\mathbb{W}$ 。

线性变换 $\pmb{T}$ 的核 $\ker(\pmb{T})$ 即为矩阵的零空间（null space）$N(\pmb{A})$ ，它的维度即矩阵的零化度，记作 $\dim N(\pmb{A})$ 。关于零空间的详细内容，参阅[4]。

值域 $ran(\pmb{T})$ 即为矩阵的列空间（column space）$C(\pmb{A})$ 。

将矩阵 $\pmb{A}$ 化简为行梯形形式，用分块矩阵表示为：

$\pmb{R}=\begin{bmatrix}\pmb{I}_r&\pmb{F}\\\pmb{0}&\pmb{0}\end{bmatrix}$

其中 $\pmb{R}$ 的秩 $r=rank\pmb{R}$ ，$\pmb{F}$ 是 $r\times(n-r)$ 阶矩阵。

因为矩阵行运算不改变轴数量，也不改变零空间，所以：$rank\pmb{A}=rank\pmb{R}=r$ 且 $N(\pmb{A})=N(\pmb{R})$ 。

根据 $\pmb{R}$ 的形状，写出 $n\times(n-r)$ 阶零空间矩阵 $\pmb{P}$ ：

$\pmb{P} = \begin{bmatrix}-\pmb{F}\\\pmb{I}_{n-r}\end{bmatrix}$

用上述结果可以计算得到 $\pmb{RP}=0$ ，故确认 $\pmb{P}$ 是零空间矩阵。

$\pmb{RP}=\begin{bmatrix}\pmb{I}_r&\pmb{F}\\\pmb{0}&\pmb{0}\end{bmatrix}\begin{bmatrix}-\pmb{F}\\\pmb{I}_{n-r}\end{bmatrix}=\begin{bmatrix}-\pmb{F}+\pmb{F}\\\pmb{0}+\pmb{0}\end{bmatrix}=0$

设 $\pmb{x}=\begin{bmatrix}\pmb{x}_1\\\pmb{x}_2\end{bmatrix}$ ，其中 $\pmb{x}_1$ 是 $r$ 维向量，$\pmb{x}_2$ 是 $n-r$ 维向量，欲使 $\pmb{Rx}=\pmb{0}$ 成立，即：

$\pmb{Rx}=\begin{bmatrix}\pmb{I}_r&\pmb{F}\\\pmb{0}&\pmb{0}\end{bmatrix}\begin{bmatrix}\pmb{x}_1\\\pmb{x}_2\end{bmatrix}=\begin{bmatrix}\pmb{x}_1+\pmb{Fx}_2\\\pmb{0}\end{bmatrix}=\pmb{0}$

所以：$\pmb{x}_1=-\pmb{Fx}_2$ ，

于是：$\pmb{x}=\begin{bmatrix}-\pmb{Fx}_2\\\pmb{x}_2\end{bmatrix}=\begin{bmatrix}-\pmb{F}\\\pmb{I}_{n-r}\end{bmatrix}\pmb{x}_2=\pmb{Px}_2$

所以：$C(\pmb{P})=N(\pmb{R})$

即：$\dim N(\pmb{R})=\dim C(\pmb{P})=n-r$ 。从而证明：

$n = \dim N(\pmb{A}) + rank\pmb{A}$

$m\times n$ 的矩阵 $\pmb{A}$ 的秩 $rank\pmb{A}$ 和零化度 $\dim N(\pmb{A})$ 之和等于 $n$ 

**证明2：线性变换的向量空间分析**

令 $\dim\mathbb{V} = n,\dim\ker(\pmb{T})=p,p\le n$ 。

设 $\ker(\pmb{T})$ 的一组基底为 $\{\pmb{u}_1,\cdots,\pmb{u}_p\}$ ，扩充此基底为向量空间 $\mathbb{V}$ 的基底 $\{\pmb{u}_1,\cdots,\pmb{u}_p,\pmb{w}_1,\cdots,\pmb{w}_r\}$ 且 $n=p+r$。

向量空间 $\mathbb{V}$ 中任一向量 $\pmb{v}$ 可表示为基底向量的唯一线性组合：

$\pmb{v}=a_1\pmb{u}_1+\cdots+a_p\pmb{u}_p+b_1\pmb{w}_1+\cdots+b_r\pmb{w}_r$

因为 $\pmb{T}(\pmb{u})=\pmb0$ ，即 $\pmb{T}(\pmb{u}_1)=\cdots=\pmb{T}(\pmb{u}_p)=\pmb0$ （如下图所示）

![](https://gitee.com/qiwsir/images/raw/master/2021-3-10/1615361607051-base02.png)

所以：

$\begin{split}\pmb{T}(\pmb{v})&=\pmb{T}(a_1\pmb{u}_1+\cdots+a_p\pmb{u}_p+b_1\pmb{w}_1+\cdots+b_r\pmb{w}_r)\\&=a_1\pmb{T}(\pmb{u}_1)+\cdots+a_p\pmb{T}(\pmb{u}_p)+b_1\pmb{T}(\pmb{w}_1)+\cdots+b_r\pmb{T}(\pmb{w}_r)\\&=b_1\pmb{T}(\pmb{w}_1)+\cdots+b_r\pmb{T}(\pmb{w}_r)\end{split}$

$\pmb{T}(\pmb{w}_1),\cdots,\pmb{T}(\pmb{w}_r)$ 张成了值域空间 $ran(\pmb{T})$ 。

设：$c_1\pmb{T}(\pmb{w}_1)+\cdots+c_r\pmb{T}(\pmb{w}_r)=0$ ，也可以写成：$\pmb{T}(c_1\pmb{w}_1+\cdots+c_r\pmb{w}_r)=0$ ，所以 $c_1\pmb{w}_1+\cdots+c_r\pmb{w}_r$ 属于零空间 $\ker(\pmb{T})$ 。

因为 $\{\pmb{u}_1,\cdots,\pmb{u}_p\}$ 是 $\ker(\pmb{T})$ 的基底，故可以有如下表达式：

$c_1\pmb{w}_1+\cdots+c_r\pmb{w}_r=d_1\pmb{u}_1+\cdots+d_p\pmb{u}_p$

又因为 $\{\pmb{u}_1,\cdots,\pmb{u}_p,\pmb{w}_1,\cdots,\pmb{w}_r\}$ 是 $\mathbb{V}$ 的基，也就是各个向量之间线性无关，所以上式中的系数都是 $0$ 。

故 $\pmb{T}(\pmb{w}_1),\cdots,\pmb{T}(\pmb{w}_r)$ 是线性无关的向量集合，是 $ran(\pmb{T})$ 的基。

所以：$r=\dim ran(\pmb{T})=rank\pmb{T}$

由 $n=p+r$ 以及前面的假设，可得：

$\dim\mathbb{V}=\dim\ker\pmb{T})+rank\pmb{T}$

### 推论

- 若 $\dim\mathbb{V}\gt\dim\mathbb{W}$ ，则：

  $\dim\ker(\pmb{T})=\dim\mathbb{V}-\dim ran(\pmb{T})\ge\dim\mathbb{V}-\dim\mathbb{W}\gt0$

  即存在非零向量 $\pmb{x}\in\mathbb{V}$ 使得 $\pmb{T}(\pmb{x})=\pmb{0}$ ，或曰 $\pmb{T}$ 不是一对一（因为 $\pmb{T}(\pmb{0})=\pmb{0}$ ）。

- 若 $\dim\mathbb{V}\lt\dim\mathbb{W}$ ，则：

  $\dim ran(\pmb{T})=\dim\mathbb{V}-\dim\ker(\pmb{T})\le\dim\mathbb{V}\lt\dim\mathbb{W}$

  即存在非零向量 $y\in\mathbb{W}$ 使得 $\pmb{y}\notin ran(\pmb{T})$ ，或曰 $\pmb{T}$ 不是满射。

如果用矩阵表述：将线性变换 $\pmb{T}:\mathbb{V}\to\mathbb{W}$ 用 $m\times n$ 的矩阵 $\pmb{A}$ 表示，其中：$n = \dim\mathbb{V}, m=\dim\mathbb{W}$ 。

- $n\gt m$ ，则：$\dim N(\pmb{A})=n-\dim C(\pmb{A})\ge n-m \gt 0$ 。即零空间 $N(\pmb{A})$ 包含非零向量，或者说 $\pmb{Ax}=0$ 有无穷多组解。
- $n\lt m$ ，则：$\dim C(\pmb{A})=n-\dim N(\pmb{A})\le n \lt m$ 。即列空间 $C(\pmb{A})$ 未能充满整个 $\mathbb{R}^m$ （或 $\mathbb{C}^m$），或者说 $\pmb{Ax}=\pmb{b}$ 不总是有解。



## 参考文献

[1]. Gilbert Strang, The Fundamental Theorem of Linear Algebra, *American Mathematical Monthly*, 100, 1993, 848-855.

[2]. [https://ccjou.wordpress.com/2009/03/23/線性代數基本定理-一/](https://ccjou.wordpress.com/2009/03/23/%e7%b7%9a%e6%80%a7%e4%bb%a3%e6%95%b8%e5%9f%ba%e6%9c%ac%e5%ae%9a%e7%90%86-%e4%b8%80/)

[3]. [https://zh.wikipedia.org/wiki/秩－零化度定理](https://zh.wikipedia.org/wiki/%E7%A7%A9%EF%BC%8D%E9%9B%B6%E5%8C%96%E5%BA%A6%E5%AE%9A%E7%90%86)

[4]. [零空间](./rank.html)



