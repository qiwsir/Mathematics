# 矩阵的迹

$n$ 阶方阵 $\pmb{A}$ 的迹：$trace\pmb{A}=\sum_{i=1}^na_{ii}$

迹与行列式都是方阵的函数。

设 $\pmb{A}$ 的特征值 $\lambda_1,\cdots,\lambda_n$ ，则：

$trace\pmb{A}=\lambda_1+\cdots+\lambda_n$

$\det\pmb{A}=\lambda_1\cdots\lambda_n$

## 性质

- $trace(\pmb{A}+\pmb{B})=trace\pmb{A}+trace\pmb{B}$

  $trace(\pmb{A}+\pmb{B})=\sum_{i=1}^n(a_{ii}+b_{ii})=\sum_{i=1}^na_{ii}+\sum_{i=1}^nb_{ii}=trace\pmb{A}+trace\pmb{B}$

- $trace(c\pmb{A})=c(trace\pmb{A})$

  $trace(c\pmb{A})=\sum_{i=1}^nca_{ii}=c\sum_{i=1}^na_{ii}=c(trace\pmb{A})$

- $trace(\pmb{AB})=trace(\pmb{BA})$

  $trace(\pmb{AB})=\sum_{i=1}^n(\pmb{AB})_{ii}=\sum_{i=1}^m\left(\sum_{j=1}^na_{ij}b_{ji}\right)$

  $trace(\pmb{BA})=\sum_{j=1}^n(\pmb{BA})_{jj}=\sum_{j=1}^n\left(\sum_{i=1}^mb_{ji}a_{ij}\right)$

  