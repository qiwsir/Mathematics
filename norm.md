# 向量范数

*打开本页，如果不能显示公式，请刷新页面。*

《机器学习数学基础》第1章1.5.3节介绍了向量范数的基本定义。

本文在上述基础上，介绍向量范数的有关性质。

**注意：**以下均在欧几里得空间塔伦，即欧氏范数。

## 性质

- 实（或复）向量 $\pmb{x}$ ，范数 $\begin{Vmatrix}x\end{Vmatrix}$ 满足：

  - $\begin{Vmatrix}x\end{Vmatrix}\ge0$
  - $\begin{Vmatrix}x\end{Vmatrix}=0 \Leftrightarrow \pmb{x}=\pmb{0}$
  - $\begin{Vmatrix}cx\end{Vmatrix}=|c|\begin{Vmatrix}x\end{Vmatrix}$ ，$c$ 是标量

- 设 $\pmb{x,y}\in\mathbb{C}^n$ ，根据[施瓦茨不等式](./cauchy-schwarz.html)：$|\pmb{x}^*\pmb{y}|\le\begin{Vmatrix}x\end{Vmatrix}\begin{Vmatrix}y\end{Vmatrix}$ 。

  若 $n=1$ ，则上式退化为 $|\overline{x}y|\le|x||y|$ ，其中 $x,y\in\mathbb{C}$ 。因为 $|\overline{x}|=|x|$ ，所以 $|\overline{x}y|\le|\overline{x}||y|$

- 三角不等式：$\pmb{x}+\pmb{y}\le \begin{Vmatrix}\pmb{x}\end{Vmatrix}+\begin{Vmatrix}\pmb{y}\end{Vmatrix}$

  **证明**

  $\begin{split}\begin{Vmatrix}\pmb{x}+\pmb{y}\end{Vmatrix}^2 &= (\pmb{x}+\pmb{y})^*(\pmb{x}+\pmb{y})\\ &= \pmb{x}^*\pmb{x}+\pmb{x}^*\pmb{y}+\pmb{y}^*\pmb{x}+\pmb{y}^*\pmb{y}\\&=\begin{Vmatrix}\pmb{x}\end{Vmatrix}^2+\pmb{x}^*\pmb{y}+\pmb{y}^*\pmb{x}+\begin{Vmatrix}\pmb{y}\end{Vmatrix}^2\end{split}$

  根据复数的性质和施瓦茨不等式：

  $\pmb{x}^*\pmb{y}+\pmb{y}^*\pmb{x}=\pmb{x}^*\pmb{y}+\overline{\pmb{x}^*\pmb{y}}=2Re(\pmb{x}^*\pmb{y})\le 2|\pmb{x}^*\pmb{y}|\le2\begin{Vmatrix}\pmb{x}\end{Vmatrix}\begin{Vmatrix}\pmb{y}\end{Vmatrix}$

  由上述结果，可得：

  $\begin{Vmatrix}\pmb{x}+\pmb{y}\end{Vmatrix}^2 \le \begin{Vmatrix}\pmb{x}\end{Vmatrix}^2+2\begin{Vmatrix}\pmb{x}\end{Vmatrix}\begin{Vmatrix}\pmb{y}\end{Vmatrix}+\begin{Vmatrix}\pmb{y}\end{Vmatrix}^2=(\begin{Vmatrix}\pmb{x}\end{Vmatrix}+\begin{Vmatrix}\pmb{y}\end{Vmatrix})^2$

  证毕。



