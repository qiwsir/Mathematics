# 矩阵运算

在《机器学习数学基础》第2章的2.1.3节、2.1.4节和2.1.5节分别介绍了矩阵的加（减）法、数量乘法和矩阵乘法，这些构成了矩阵的基本运算，并且列出了矩阵的所有运算性质。在手工计算或者原理证明中，这些计算性质会经常用到。

此外，作为拓展，以下内容也不妨了解。

## 运算技巧

若 $\pmb{A}$ 和 $\pmb{B}$ 是 $n\times n$ 阶矩阵，且 $\pmb{A} + \pmb{B}$ 是可逆的，则：

$\pmb{A}(\pmb{A}+\pmb{B})^{-1}\pmb{B}=\pmb{B}(\pmb{A}+\pmb{B})^{-1}\pmb{A}$

上述运算技巧来自参考文献[1]。

**证明：**

因为 $\pmb{A}+\pmb{B}$ 可逆，所以 $(\pmb{A}+\pmb{B})(\pmb{A}+\pmb{B})^{-1}=\pmb{I}$ ，即：

$\pmb{A}(\pmb{A}+\pmb{B})^{-1}+\pmb{B}(\pmb{A}+\pmb{B})^{-1}=\pmb{I}$

$\pmb{A}(\pmb{A}+\pmb{B})^{-1}=\pmb{I}-\pmb{B}(\pmb{A}+\pmb{B})^{-1}$

计算：

$\begin{split}\pmb{A}(\pmb{A}+\pmb{B})^{-1}\pmb{B}-\pmb{B}(\pmb{A}+\pmb{B})^{-1}\pmb{A}&=(\pmb{I}-\pmb{B}(\pmb{A}+\pmb{B})^{-1})\pmb{B}-\pmb{B}(\pmb{A}+\pmb{B})^{-1}\pmb{A}\\&=\pmb{B}-\pmb{B}(\pmb{A}+\pmb{B})^{-1}\pmb{B}-\pmb{B}(\pmb{A}+\pmb{B})^{-1}\pmb{A}\\&=\pmb{B}-\pmb{B}(\pmb{A}+\pmb{B})^{-1}(\pmb{B}+\pmb{A})\\&=\pmb{B}-\pmb{B}\quad(\because\pmb{A}+\pmb{B}可逆)\\&=0\end{split}$

所以：$\pmb{A}(\pmb{A}+\pmb{B})^{-1}\pmb{B}=\pmb{B}(\pmb{A}+\pmb{B})^{-1}\pmb{A}$

证毕。



## 参考文献

[1]. [https://ccjou.wordpress.com/2010/10/04/矩陣運算的基本技巧/](https://ccjou.wordpress.com/2010/10/04/%e7%9f%a9%e9%99%a3%e9%81%8b%e7%ae%97%e7%9a%84%e5%9f%ba%e6%9c%ac%e6%8a%80%e5%b7%a7/)