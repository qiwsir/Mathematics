# 矩阵的QR分解

QR分解是一种重要的矩阵分解方式，《机器学习数学基础》的第3章3.5.1节“QR分解”对此做了最基本的介绍，此处在该基础上，对QR分解给予适当拓展。

QR分解目前已知三种算法$^{[1]}$：

- 格拉姆-施密特正交化(Gram-Schmidt)方法，这种方法在《机器学习数学基础》中有详细介绍。
- 豪斯霍尔德变换（Householder transformation）
- 吉文斯旋转法（Givens）

## 豪斯霍尔德变换

豪斯霍尔德变换（Householder transformation），又称初等反射（elementary reflection）。最初由A.C Aitken在1932年提出。阿尔斯通·斯科特·豪斯霍尔德在1958年指出了这一变换在数值线性代数上的意义 $^{[2]}$。

通过豪斯霍尔德变换，一个向量能实现“超平面反射”的线性变换，实现这种线性变换的矩阵被称作**豪斯霍尔德矩阵**，超平面的法向量被称作**豪斯霍尔德向量**。

### 定义

设 $\pmb{v}$ 是单位向量，$\pmb{I}$ 是单位矩阵，豪斯霍尔德矩阵为：

$\pmb{H} = \pmb{I}-2\pmb{vv}^*$

其中 $\pmb{v}^*$ 是 $\pmb{v}$ 的共轭转置（在实数范围内，即转置 $\pmb{v}^T$ 。

### 性质

-  是对称矩阵，$\pmb{H}^T=\pmb{H}$
- 是正交矩阵，$\pmb{H}^T=\pmb{H}^{-1}$
- 是埃尔米特矩阵，$\pmb{H}^*=\pmb{H}$
- 是对合的$^{[3]}$，$\pmb{H}^2=\pmb{I}$

### 应用

豪斯霍尔德变换可以将向量的某些元素变成零，同时保持该向量的范数不变。例如，列向量 $\pmb{x}=\begin{bmatrix}x_1\\\vdots\\x_n\end{bmatrix}$ ，通过豪斯霍尔德变换，成为单位向量 $\pmb{e}=\begin{bmatrix}1\\0\\\vdots\\0\end{bmatrix}$ 乘以一个常数的豪斯霍尔德矩阵：

$\pmb{H}=\pmb{I}-\frac{2}{\langle\pmb{v,v}\rangle}\pmb{vv}^H$

其中豪斯霍尔德向量 $\pmb{v}$ ：

$\pmb{v}=\pmb{x}+sgn(x_1)\begin{Vmatrix}x\end{Vmatrix}_2\pmb{e}_1$

对一个矩阵的各个列向量逐一进行相应的豪斯霍尔德变换，可以将这个矩阵变换为上海森伯格矩阵、上三角矩阵等形式。后者就是QR分解的豪斯霍尔德算法。

### 用豪斯霍尔德变换对矩阵 $\pmb{A}$ 进行QR分解$^{[4]}$

令 $\pmb{x}$ 为 $m\times n$ 矩阵 $\pmb{A}$ 的任一 $m$ 维列向量（$m\ge n$），且 $\begin{Vmatrix}x\end{Vmatrix}=|a|$ （其中 $a$ 为标量）。（以下演示中，假设 $\pmb{A}$ 为实矩阵）

设单位向量 $\pmb{e}_1=\begin{bmatrix}1\\0\\\vdots\\0\end{bmatrix}$ ，令：

$\pmb{u} = \pmb{x}-a\pmb{e}_1,\pmb{v}=\frac{\pmb{u}}{\begin{Vmatrix}\pmb{u}\end{Vmatrix}}$

则豪斯霍尔德矩阵为：$\pmb{H}=\pmb{I}-2\pmb{vv}^T$

满足：$\pmb{Hx}=\begin{bmatrix}\alpha\\0\\\vdots\\0\end{bmatrix}$



例如：$\pmb{A}=\begin{bmatrix}0&3&1\\0&4&-2\\2&1&1\end{bmatrix}$ ，进行QR分解。

列向量 $\pmb\alpha_1=\begin{bmatrix}0\\0\\2\end{bmatrix}$ ，令 $a_1=\begin{Vmatrix}\pmb\alpha_1\end{Vmatrix}_2=2$ ，则：

$\pmb{v}_1=\frac{\pmb{\alpha}_1-a_1\pmb{e}_1}{\begin{Vmatrix}\pmb{\alpha}_1-\alpha_1\pmb{e}_1\end{Vmatrix}}=\frac{1}{\sqrt{2}}\begin{bmatrix}-1\\0\\1\end{bmatrix}$

所以：

$\pmb{H}_1=\pmb{I}-2\pmb{v}_1\pmb{v}_1^T=\begin{bmatrix}0&0&1\\0&1&0\\1&0&0\end{bmatrix}$

从而：

$\pmb{H}_1\pmb{A}=\begin{bmatrix}2&1&1\\0&4&-2\\0&3&1\end{bmatrix}$

对上述所得矩阵，令 $\pmb\alpha_2=\begin{bmatrix}4\\3\end{bmatrix}$ ，则 $a_2=\begin{Vmatrix}\alpha_2\end{Vmatrix}_2=5$ ，则：

$\pmb{v}_2=\frac{\pmb{\alpha}_2-a_2\pmb{e}_2}{\begin{Vmatrix}\pmb{\alpha}_2-a_2\pmb{e}_2\end{Vmatrix}_2}=\frac{1}{\sqrt{10}}\begin{bmatrix}-1\\3\end{bmatrix}$

$\hat{\pmb{H}}_2=\pmb{I}-2\pmb{v}_2\pmb{v}_2^T=\frac{1}{5}\begin{bmatrix}4&3\\3&-4\end{bmatrix}$

记：

$\pmb{H}_2=\begin{bmatrix}1&\pmb{0}^T\\0&\hat{\pmb{H}}_2\end{bmatrix}=\begin{bmatrix}1&0&0\\0&4/5&3/5\\0&3/5&-4/5\end{bmatrix}$

则：

$\pmb{R}=\pmb{H}_2(\pmb{H}_1\pmb{A})=\begin{bmatrix}2&1&1\\0&5&-1\\0&0&-2\end{bmatrix}$

$\pmb{Q}=\pmb{H}_1^T\pmb{H}_2^T=\frac{1}{5}\begin{bmatrix}0&3&-4\\0&4&3\\5&0&0\end{bmatrix}$

通过上述示例，总结利用豪斯霍尔德变换进行QR分解的步骤：

1. 选矩阵第一列的列向量，计算出相应的豪斯霍尔德矩阵 $\pmb{H}_1$ ；

2. 计算：$\pmb{H}_1\pmb{A}$ ，得到第一列除第一个值之外其余都为零的矩阵，如下图所示：

   ![](https://gitee.com/qiwsir/images/raw/master/2021-3-23/1616467018792-house1.png)

3. 对于上图中的分块矩阵 $\pmb{A}'$ ，重复执行以上两步。从而得到 $\pmb{H}_2$ ；

4. 加上以上迭代过程为 $t$ 次，则：

   $\pmb{R}=\pmb{H}_t\cdots\pmb{H}_2\pmb{H}_1\pmb{A}$

   $\pmb{Q}=\pmb{H}_1^T\pmb{H}_2^T\cdots\pmb{H}_t^T$

### 优势

相比于格拉姆-施密特正交化方法，豪斯霍尔德变换具有更好的数值稳定性$^{[4]}$ 。

## 吉文斯旋转

对 $\mathbb{R}^n$ 选两个坐标轴 $i,j$ ，$i\ne j$ 。吉文斯旋转的 $n$ 阶矩阵：

![](https://gitee.com/qiwsir/images/raw/master/2021-3-23/1616469793321-givens1.png)

其中，$c=\cos\theta,s=\sin\theta$ ，吉文斯旋转矩阵 $\pmb{G}$ 的所有非零元：

- $g_{kk}=1(k\ne i,j);g_{ii}=c;g_{jj}=c;g_{ij}=s;g_{ji}=-s$

乘积 $\pmb{Gx}$ 表示向量 $\pmb{x}$ 在 $(i,j)$ 平面中逆时针旋转 $\theta$ 弧度。

例如 $3$ 阶吉文斯旋转矩阵：$\pmb{G}_{31}=\begin{bmatrix}c&0&-s\\0&1&0\\s&0&c\end{bmatrix},\pmb{G}_{23}=\begin{bmatrix}1&0&0\\0&c&s\\0&-s&c\end{bmatrix}$

以向量 $\pmb{x}=\begin{bmatrix}a\\b\end{bmatrix}$ 为例，分别计算：

$\begin{split}r &= \sqrt{a^2+b^2}\\c&=\frac{a}{r}\\s&=-\frac{b}{r}\end{split}$ 

吉文斯旋转矩阵 $\pmb{G}=\begin{bmatrix}c&-s\\s&c\end{bmatrix}$ 乘以此向量：$\begin{bmatrix}c&-s\\s&c\end{bmatrix}\begin{bmatrix}a\\b\end{bmatrix}=\begin{bmatrix}r\\0\end{bmatrix}$ ，如此将原向量底部的元素转换为 $0$ 。每次用吉文斯旋转矩阵对向量（矩阵）进行旋转，都可以将一个元素化成 $0$ ，直到将原始矩阵转成一个上三角矩阵，则实现了分解。

例如$^{[1]}$：$3$ 阶矩阵：

$\pmb{A}=\begin{bmatrix}0&-15&14\\4&32&2\\3&-1&4\end{bmatrix}$

用吉文斯旋转矩阵的目标是将矩阵主对角线以下的所有元变为 $0$ ，按照如下步骤依次进行。

1. 将 $\pmb{A}$ 的 $(2,1)$ 位置元素变为 $0$ ，对应的吉文斯旋转矩阵设为 $\pmb{H}_{21}$ ，即 $i=2,j=1$ 。以 $\pmb{A}$ 的第一列 $\begin{bmatrix}0\\4\\3\end{bmatrix}$ 来设定 $\pmb{H}_{21}$ 的参数：

   $\begin{split}c&=\frac{x_j}{\sqrt{x_i^2+x_j^2}}=\frac{0}{\sqrt{0^2+4^2}}=0\\s&=-\frac{x_i}{\sqrt{x_i^2+x_j^2}}=\frac{4}{\sqrt{0^2+4^2}}=-1\\\pmb{G}_{21}&=\begin{bmatrix}c&-s&0\\s&c&0\\0&0&1\end{bmatrix}=\begin{bmatrix}0&1&0\\-1&0&0\\0&0&1\end{bmatrix}\end{split}$

   旋转后得到：

   $\pmb{G}_{21}\pmb{A}=\begin{bmatrix}0&1&0\\-1&0&0\\0&0&1\end{bmatrix}\begin{bmatrix}0&-15&14\\4&32&2\\3&-1&4\end{bmatrix}=\begin{bmatrix}4&32&2\\0&15&-14\\3&-1&4\end{bmatrix}$

2. 上一步中所得到的矩阵 $\pmb{G}_{21}\pmb{A}$ 中 $(3,1)$ 位置的元素再转换为 $0$ ，其所在列向量 $\begin{bmatrix}4\\0\\3\end{bmatrix}$ ，设定相应的吉文斯旋转矩阵 $\pmb{H}_{31}$ ：

   $\begin{split}c &= \frac{4}{\sqrt{4^2+3^2}}=\frac{4}{5}\\s&=-\frac{3}{\sqrt{4^2+3^2}}=-\frac{3}{5}\\\pmb{G}_{31}&=\begin{bmatrix}c&0&-s\\0&1&0\\s&0&c\end{bmatrix}=\begin{bmatrix}4/5&0&3/5\\0&1&0\\-3/5&0&4/5\end{bmatrix}\end{split}$

   旋转后得：

   $\pmb{G}_{31}\pmb{G}_{21}\pmb{A}=\begin{bmatrix}4/5&0&3/5\\0&1&0\\-3/5&0&4/5\end{bmatrix}\begin{bmatrix}4&32&2\\0&15&-14\\3&-1&4\end{bmatrix}=\begin{bmatrix}5&25&4\\0&15&-14\\0&-20&2\end{bmatrix}$

3. 上面所得矩阵中的 $(3,2)$ 位置的元素，转换为 $0$ ，所在列向量 $\begin{bmatrix}25\\15\\-20\end{bmatrix}$ ，则：

   $\begin{split}c&=\frac{15}{\sqrt{15^2+(-20)^2}}=\frac{3}{5}\\s&=-\frac{-20}{\sqrt{15^2+(-20)^2}}=\frac{4}{5}\end{split}$

   旋转后得：

   $\pmb{G}_{32}\pmb{G}_{31}\pmb{G}_{21}\pmb{A}=\begin{bmatrix}1&0&0\\0&3/5&-4/5\\0&4/5&3/5\end{bmatrix}\begin{bmatrix}5&25&4\\0&15&-14\\0&-20&2\end{bmatrix}=\begin{bmatrix}5&25&4\\0&25&-10\\0&0&-10\end{bmatrix}$

经过连续三次旋转那之后，可以表示为：

$\pmb{G}_{32}\pmb{G}_{31}\pmb{G}_{21}\pmb{A}=\pmb{R}$

则矩阵 $\pmb{A}$ 可以分解为：

$\pmb{A}=(\pmb{G}_{32}\pmb{G}_{31}\pmb{G}_{21})^{-1}\pmb{R}=\pmb{G}_{21}^{-1}\pmb{G}_{31}^{-1}\pmb{G}_{32}^{-1}\pmb{R}$

因为吉文斯旋转矩阵是正交矩阵，$\pmb{G}_{ij}^T=\pmb{G}_{ij}^{-1}$ ，因此矩阵 $\pmb{A}$ 的QR分解为：

$\pmb{A}=\pmb{G}_{21}^{T}\pmb{G}_{31}^{T}\pmb{G}_{32}^{T}\pmb{R}=\pmb{QR}$

其中 $\pmb{Q}=\pmb{G}_{21}^{T}\pmb{G}_{31}^{T}\pmb{G}_{32}^{T}$  。正交矩阵的积还是正交矩阵，即 $\pmb{Q}^T=\pmb{Q}^{-1}$ 。

注意，通过吉文斯旋转得到的 QR分解形式，与格拉姆-施密特正交化所得形式有所不同。



## 参考文献

[1]. [https://ccjou.wordpress.com/2010/02/18/givens-旋轉於-qr-分解的應用/](https://ccjou.wordpress.com/2010/02/18/givens-%e6%97%8b%e8%bd%89%e6%96%bc-qr-%e5%88%86%e8%a7%a3%e7%9a%84%e6%87%89%e7%94%a8/)

[2]. [https://zh.wikipedia.org/wiki/豪斯霍尔德变换](https://zh.wikipedia.org/wiki/%E8%B1%AA%E6%96%AF%E9%9C%8D%E5%B0%94%E5%BE%B7%E5%8F%98%E6%8D%A2)

[3]. 所谓对合（involution），也称为对核函数，即逆（反）函数等于自身的函数。在线性代数中，对合是线性算子 $\pmb{T}$ 使得 $\pmb{T}^2=\pmb{I}$ 。这种算子可对角化为对角线上有 $1$ 和 $-1$ 。如果这个算子是正交的（称为**正交对合**），它是正交可对角化的。

[4]. [https://zh.wikipedia.org/wiki/QR分解](https://zh.wikipedia.org/wiki/QR%E5%88%86%E8%A7%A3)