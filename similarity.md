# 相似矩阵

*打开本页，如果不能显示公式，请刷新页面*

《机器学习数学基础》第3章3.3节专门介绍了相似矩阵的有关内容，包括相似变换、几何理解和对角化，并给出了用程序实现的方法。

## 用特征值判断矩阵是否相似

设 $\pmb{A}$ 和 $\pmb{B}$ 都是 $n\times n$ 矩阵，且 $\pmb{A}\sim\pmb{B}$ ，即 $\pmb{A}=\pmb{PBP}^{-1}$ 。

> 以 $\pmb{P}$ 的列向量为基向量，线性变换 $\pmb{A}$ 参考此基底的变换矩阵即为 $\pmb{B}$ 。

**命题1：两个相似矩阵包含相同的特征值。**

证明1：

将相似关系代入 $\pmb{Ax}=\lambda\pmb{x}$ ，得：

$\pmb{PBP}^{-1}\pmb{x}=\lambda\pmb{x}$

等号两侧左乘 $\pmb{P}^{-1}$ 得：

$\pmb{BP}^{-1}\pmb{x}=\lambda\pmb{P}^{-1}\pmb{x}$

由此可知 $\pmb{B}$ 有与 $\pmb{A}$ 相同的特征值 $\lambda$ ，但 $\pmb{B}$ 的特征向量为 $\pmb{P}^{-1}\pmb{x}$ 。

证明2：

计算特征多项式：

$\begin{split}p_{\pmb{A}}(\lambda)&= \det(\pmb{A}-\lambda\pmb{I})=\det(\pmb{PBP}^{-1}-\lambda\pmb{I})\\&=\det(\pmb{P}(\pmb{B}-\lambda\pmb{I})\pmb{P}^{-1})\\&=\det(\pmb{P})\det(\pmb{B}-\lambda\pmb{I})(\det(\pmb{P}))^{-1}\\&=\det(\pmb{B}-\lambda\pmb{I})\\&=p_{\pmb{B}}(\lambda)\end{split}$

在“两个矩阵有相同的特征值”条件下，讨论一下三种情况：

**情况1：$\pmb{A}$ 和 $\pmb{B}$ 皆可对角化**

设 $\pmb{A}=\pmb{SDS}^{-1}，\pmb{B}=\pmb{TDT}^{-1}$ ，则 $\pmb{A}\sim\pmb{D}，\pmb{B}\sim\pmb{D}$ 。

由 $\pmb{B}=\pmb{TDT}^{-1}$ 可得：$\pmb{D}=\pmb{T}^{-1}\pmb{BT}$ ，则：

$\pmb{A}=\pmb{S}\pmb{T}^{-1}\pmb{BT}\pmb{S}^{-1}=\pmb{ST}^{-1}\pmb{B}(\pmb{ST}^{-1})^{-1}$

所以：$\pmb{A}\sim\pmb{B}$ 。

**情况2：$\pmb{B}$ 可对角化，$\pmb{A}$ 不可对角化**

此时 $\pmb{A}$ 不相似于 $\pmb{B}$ 。

**情况3：都不可对角化**

两个矩阵有可能相似，也有可能不相似。需要进一步论证。



## 参考文献

[1]. [线代启示录：如何检查量矩阵是否相似](https://ccjou.wordpress.com/2009/06/25/%e5%a6%82%e4%bd%95%e6%aa%a2%e6%9f%a5%e4%ba%8c%e7%9f%a9%e9%99%a3%e6%98%af%e5%90%a6%e7%9b%b8%e4%bc%bc/)



