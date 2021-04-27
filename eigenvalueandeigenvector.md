# 理解特征值和特征向量

*打开本页，如果不能显示公式，请刷新浏览器。*

## 以反射变换为例$^{[1]}$

$\mathbb{V}$ 和 $\mathbb{W}$ 是两个向量空间，有线性变换 $\pmb{T}:\mathbb{V}\to\mathbb{W}$ ，将输入向量 $\pmb{x}\in\mathbb{V}$ 映射到输出向量 $\pmb{T}(\pmb{x})\in\mathbb{W}$ 。

对于任意 $\pmb{x,y}\in\mathbb{V}$ 和标量 $c$ ，线性变换 $\pmb{T}$ 满足下列性质：

$\begin{split}\pmb{T}(\pmb{x}+\pmb{y})&=\pmb{T}(\pmb{x})+\pmb{T}(\pmb{y})\\\pmb{T}(c\pmb{x})&=c\pmb{T}(\pmb{x})\end{split} \tag{1}$

若 $\mathbb{V}=\mathbb{W}$ 也称 $\pmb{T}$ 为线性算子（算符）。

假设几何向量空间 $\mathbb{R}^2$ ，任一线性算子 $\pmb{T}:\mathbb{R}^2\to\mathbb{R}^2$ 都可以用 $2\times 2$ 实数矩阵 $\pmb{A}$ 表示：

$\pmb{T}(\pmb{x})=\pmb{Ax}\tag{2}$

其中 $\pmb{x}\in\mathbb{R}^2$ 。称 $\pmb{A}$ 是线性算子 $\pmb{T}$ 的变换矩阵或表示矩阵。

下面研究在二维几何空间的镜像反射变换（reflection）。对于向量 $\pmb{x}=\begin{bmatrix}x_1\\x_2\end{bmatrix}$ ，以x轴为镜面的反射变换：

$\pmb{T}\left(\begin{bmatrix}x_1\\x_2\end{bmatrix}\right)=\begin{bmatrix}x_1\\-x_2\end{bmatrix}=x_1\begin{bmatrix}1\\0\end{bmatrix}+x_2\begin{bmatrix}0\\-1\end{bmatrix}=\begin{bmatrix}1&0\\0&-1\end{bmatrix}\begin{bmatrix}x_1\\x_2\end{bmatrix}$

令 $\pmb{D}=\begin{bmatrix}1&0\\0&-1\end{bmatrix}$

称 $\pmb{D}$ 为标准反射矩阵。

更一般情况，求过原点的直线 $L=\{t\pmb{v}_1|t\in\mathbb{R}\}$ 的反射矩阵，即以此直线为镜面。

令 $\pmb{v}_2$ 表示直线 $L$ 的法向量，即 $\pmb{v}_2\bot\pmb{v}_1$ ，如下图所示：

![](https://gitee.com/qiwsir/images/raw/master/2021-4-27/1619485058963-v1.png)

则：

$\begin{split}\pmb{T}(\pmb{v}_1)&=\pmb{v}_1=1\cdot\pmb{v}_1\\\pmb{T}(\pmb{v}_2)&=-\pmb{v}_2=（-1)\cdot\pmb{v}_2\end{split}\tag{3}$

上面两个式子的形式相同，都是：

$\pmb{T}(\pmb{v})=\lambda\pmb{v}\tag{4}$

则称 $\lambda$ 为线性算子 $\pmb{T}$ 的特征值（eigenvalue），对应的非零向量 $\pmb{v}$ 为特征向量（eigenvector）。这两个量完全代表了线性算子 $\pmb{T}$ 的固有特征。

以（3）式为例，①特征向量 $\pmb{v}_1,\pmb{v}_2$ 经反射算子 $\pmb{T}$ 得到的像 $\pmb{T}(\pmb{v}_i)$ 属于子空间 $span\{\pmb{v}_1,\pmb{v}_2\}$ ，特征向量 $\lambda_1,\lambda_2$ 决定了 $\pmb{T}(\pmb{v}_i)$ 的伸缩倍数，正负号决定指向是否与原来相同；②除了特征空间 $span\{\pmb{v}_1,\pmb{v}_2\}$ ，其他不属于此子空间的非零向量皆不满足（4）式。

以上是以镜像发射变换为例。此外，线性算子 $\pmb{T}$ 还可以有其他意义。所以，没有一个确定的答案。

在（2）式中，表示矩阵 $\pmb{A}$ 用后面的方法得到，但是，（3）式中的镜像直线是一般的直线，不是x轴，无法用求表示矩阵 $\pmb{D}$ 方式计算出相应的表示矩阵。

下面探讨构建变换矩阵的方法。

将线性无关的特征向量组成 $\mathbb{R}^2$ 的一个基底 $\pmb{\beta}=\{\pmb{v}_1,\pmb{v}_2\}$ ，任一向量 $\pmb{x}\in\mathbb{R}^2$ 可唯一表示成：

$\pmb{x}=c_1\pmb{v}_1+c_2\pmb{v}_2$

其中 $c_1,c_2$ 可以合并写成向量 $\pmb{x}$ 参考基底 $\pmb{\beta}$ 的向量，记作：$[\pmb{x}]_{\pmb{\beta}}=\begin{bmatrix}c_1\\c_2\end{bmatrix}$

根据（3）式，可得：

$\pmb{T}(\pmb{x})=\pmb{T}(c_1\pmb{v}_1+c_2\pmb{v}_2)=c_1\pmb{T}(\pmb{v}_1)+c_2\pmb{T}(\pmb{v}_2)=c_1\pmb{v}_1-c_2\pmb{v}_2\tag{5}$

根据（5）式，可以写出 $\pmb{T}(\pmb{x})$ 参考基底 $\pmb{\beta}$ 的坐标向量：

$[\pmb{T}(\pmb{x})]_{\pmb{\beta}}=\begin{bmatrix}c_1\\-c_2\end{bmatrix}=\begin{bmatrix}1&0\\0&-1\end{bmatrix}\begin{bmatrix}c_1\\c_2\end{bmatrix}=\pmb{D}[\pmb{x}]_{\pmb{\beta}}\tag{6}$

由此可知：若参考特征向量构成的基底，所有镜像反射矩阵必可转换成标准反射矩阵 $\pmb{D}$ 。

又因为：

$\pmb{x}=c_1\pmb{v}_1+c_2\pmb{v}_2=\begin{bmatrix}\pmb{v}_1&\pmb{v}_2\end{bmatrix}\begin{bmatrix}c_1\\c_2\end{bmatrix}=\pmb{S}[\pmb{x}]_{\pmb{\beta}}\tag{7}$

若假设 $\pmb{v}_1=\begin{bmatrix}2\\1\end{bmatrix}\pmb{v}_2=\begin{bmatrix}-1\\2\end{bmatrix}$ ，则 $\pmb{S}=\begin{bmatrix}\pmb{v}_1&\pmb{v}_2\end{bmatrix}=\begin{bmatrix}2&-1\\1&2\end{bmatrix}$ 称为坐标变换矩阵。

因为 $[\pmb{x}]_{\pmb{\beta}}=\pmb{S}^{-1}\pmb{x}$ （由（7）式得），且 $[\pmb{T}(\pmb{x})]_{\pmb{\beta}}=\pmb{S}^{-1}\pmb{T}(\pmb{x})$ ，代入（6）式：

$\pmb{S}^{-1}\pmb{T}(\pmb{x})=\pmb{D}\pmb{S}^{-1}\pmb{x}$

两边同时左乘 $\pmb{S}$ ，得：

$\pmb{T}(\pmb{x})=\pmb{SD}\pmb{S}^{-1}\pmb{x}=\pmb{Ax}\tag{8}$

将上述过程，可以用如下示意图表示：

![](https://gitee.com/qiwsir/images/raw/master/2021-4-27/1619488496426-v2.png)

所以，$\pmb{T}$ 的变换矩阵为：

$\pmb{A}=\pmb{SD}\pmb{S}^{-1}=\begin{bmatrix}2&-1\\1&2\end{bmatrix}\begin{bmatrix}1&0\\0&-1\end{bmatrix}\frac{1}{5}\begin{bmatrix}2&1\\-1&2\end{bmatrix}=\frac{1}{5}\begin{bmatrix}3&4\\4&-3\end{bmatrix}$



## 参考文献

[1]. [线代启示录：答Rich——关于特征值与特征向量的物理意义]