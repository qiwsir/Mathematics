# 特征值的代数重数与几何重数

*打开本页，如果没有显示公式，请刷新页面。*

## 定义

令 $\pmb{A}$ 为一个 $n\times n$ 阶矩阵，非零向量 $\pmb{x}$ ，有：

$\pmb{Ax}=\lambda\pmb{x}\tag{1.1}$

则 $\lambda$ 是 $\pmb{A}$ 的特征值，$\pmb{x}$ 是对应的特征向量。

由（1.1）可得：

$(\pmb{A}-\lambda\pmb{I})\pmb{x}=\pmb{0}\tag{1.2}$

故 $\pmb{A}-\lambda\pmb{I}$ 的零空间 $N(\pmb{A}-\lambda\pmb{I})$ $^{[2]}$（或称对应 $\lambda$ 的特征空间）包括非零向量 $\pmb{x}$ ，所以 $\pmb{A}-\lambda\pmb{I}$ 是不可逆矩阵，即 

$det(\pmb{A}-\lambda\pmb{I})=0\tag{1.3}$ 

定义 $\pmb{A}$ 的特征多项式为：

$p(t)=det(\pmb{A}-t\pmb{I}) \tag{1.4}$

$\lambda$ 即为 $p(t)$ 的根。

设 $\pmb{A}$ 有 $k$ 个相异的特征值 $\lambda_1,\lambda_2,\cdots,\lambda_k,1\le k\le n$ ，特征多项式可以分解为：

$p(t)=det(\pmb{A}-t\pmb{I})=(\lambda_1-t)^{\beta_1}\cdots(\lambda_k-t)^{\beta_k} \tag{1.5}$

其中特征值 $\lambda_i$ 的重根数 $\beta_i$ 称为**代数重数**（algebraic multiplicity）。

$n$ 次多项式 $p(t)$ 有 $n$ 个根（包含重根），则：$\beta_1+\cdots+\beta_k=n$ 。

特征空间 $N(\pmb{A}-\lambda\pmb{I})$ 的维数 $\dim N(\pmb{A}-\lambda\pmb{I})$ 称为 $\lambda_i$ 的**几何重数**（geometric multiplicity），也就是对应 $\lambda_i$ 的最大线性无关的特征向量数。





## 参考文献

[1]. [线代启示录：特征值的代数重数与几何重数](https://ccjou.wordpress.com/2015/11/19/%e7%89%b9%e5%be%b5%e5%80%bc%e7%9a%84%e4%bb%a3%e6%95%b8%e9%87%8d%e6%95%b8%e8%88%87%e5%b9%be%e4%bd%95%e9%87%8d%e6%95%b8/)

[2]. [矩阵的秩：零空间](./rank.html)