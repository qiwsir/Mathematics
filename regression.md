## 回归分析

在统计学中，经常要研究变量之间的关系。变量之间存在两种关系：

- 确定性，即变量之间可用函数关系来表达。比如：力（F）、质量（m）、加速度（a），这三个变量之间的关系可以用 F=ma 表示，就是熟知的牛顿第二定律。也可以说，经典物理基本思想，就是寻找宇宙世界的确定性的关系——上帝不掷骰子。
- 非确定性，即变量之间如果存在关系，通过统计学找到它们之间的相关关系，而非因果关系。比如有经济学家研究发现“女生夏天所穿裙子越短，经济越好”，在这个“研究成果”中，“裙子的长度”与“经济状况”之间，就不是因果关系，而是相关关系。统计结果展示的都是相关关系，相关关系是否能揭示因果性？还需要进一步研究。

回归分析是研究相关关系的一种数学工具，能够帮助我们从一个变量取得的值去估计另一个变量所取的值。

## 高尔顿的研究

最早对回归问题进行研究的是英国遗传学家高尔顿爵士（[Sir Francis Galton](https://en.wikipedia.org/wiki/Francis_Galton)）。1886年，他研究亲子身高的时候发现，父母与子女的身高虽然有相关性，但子女的身高具有“回归平均值”（regression toward the mean）的现象——简称“回归均值”。

<center><img src="https://gitee.com/qiwsir/images/raw/master/2021-2-19/1613698856343-Francis_Galton.jpg" style="zoom:50%;" /></center>

<center>Sir Francis Galton (1822–1911)</center>

我们比较熟悉的“巨人”篮球明星姚明，据有关资料称姚明身高2米26，他的夫人叶莉身高1米90$^{[1]}$，不少人就此盼望他们的女儿会更高。根据高尔顿的研究，虽然高父母的子女身高一般也高，但往往比父母要矮。

高尔顿提出的“回归均值”，不仅是一个统计学概念，还表明从分布的边缘往中心移动是一个无可避免、持续不断的动态过程，从而致使正态分布成为与此过程一致的结果$^{[2]}$。英国统计学家皮尔逊（Karl Pearson）曾这样称赞高尔顿的工作：

> 高尔顿对我们的科学观念发动一场革命，修正了我们的科学哲学，甚至校订了人生$^{[3]}$。

下面的表格，是高尔顿研究亲子身高所用的数据（单位：英寸）$^{[4]}$：


![](https://gitee.com/qiwsir/images/raw/master/2021-2-19/1613703942299-length.png)



- 最左边一列，表示“父母平均身高分组”。左起第二列（Total）表示对应分组中有多少对父母，例如“父母平均身高分组”中的 $71.5$ ，对应“Total”列中的 $11$ ，意味着在该分组中有 $11$ 对父母。用图像表示这两组数据的关系（注：以下数据中，$73$ 表示大于 $72.5$ 的组，$63$ 表示小于 $64.5$ 的组）。

  ```python
  import pandas as pd
  import seaborn as sns
  
  df = pd.DataFrame({'parent_group':[73, 72.5, 71.5, 70.5, 69.5, 68.5, 67.5, 66.5, 65.5, 64.5, 63], 
                     "Total":[5, 6, 11, 22, 41, 49, 33, 20, 12, 5, 1]})
  sns.barplot(x="parent_group", y="Total", data=df)
  ```

  输出图像

  ![](https://gitee.com/qiwsir/images/raw/master/2021-2-19/1613705258435-parent_length.png)

  从图像结果可知，所研究的父母身高是呈正态分布。

- 用类似的方法，还可以研究“成年子女身高分组”中每组人数（上述数据表中底起第二行“Total”）的分布特点。

  ```python
  child_df = ({'group':[61, 62.2, 63.2, 64.2, 65.2, 66.2, 67.2, 68.2, 69.2, 70.2, 71.2, 72.2, 73.2, 74],
              'Total':[5, 7, 32, 59, 48, 117, 138, 120, 167, 99, 64, 41, 17, 14]})
  sns.barplot(x='group', y='Total', data=child_df)
  ```

  输出图像

  ![](https://gitee.com/qiwsir/images/raw/master/2021-2-19/1613711181103-child_length.png)

  亦为正态分布。

- 再从数据表中数据分布特点，从左下角到右上角，呈对角分布，说明父母与子女的身高具有正相关性，

- 但是，如果比较数据表中最右一列“子女身高中位数”和最左列“父母平均身高分组”，会发现，在父母平均身高组 $68.5$ 及其以上的行中，子女的身高中位数小于父母平均身高；在此组以下的行中，子女的身高中位数大于父母的平均身高。这就呈现了“回归均值”的现象。

为什么会出现“回归均值”现象？高尔顿做了解释，他认为“孩子的遗传一部分得自父母，一部分得自祖先。一般而言，族谱向上追溯愈久远，祖先人数愈多，也更加多样化，最后就跟采自任何种族，人数一样多的任意样本，没有什么差别”$^{[5]}$ 。从现代的角度来看，高尔顿的解释并不正确，因为子女从父母那里得到遗传基因，祖先的遗传是通过父母遗传给子女的。那么，身高“回归均值”的现象应该如何解释？我想这已经超出了本文所探讨的范围，最具说服力的解释应该由专门的遗传学研究者做出。

如果从统计学角度，可以这样解释$^{[5]}$——也仅仅是从数量关系上进行解释，而非因果性解释。

设数据样本 $\{x_i, y_i\}$ ，$x_i$ 表示父母的身高，$y_i$ 表示子女的升高，根据线性回归，可得：

$\frac{\hat{y}-\overline{y}}{\sigma_y}=\rho\frac{x-\overline{x}}{\sigma_x}$

其中 $\rho$ 为 $x_i$ 和 $y_i$ 的相关系数。通常 $-1\lt\rho\lt1$ ，所以子女的身高相对平均值的差不会超过父母身高相对均值的差。但，这个结论的前提是已经承认了“回归均值”现象，依据 $y=\alpha+\beta x$ 线性回归的假设而得到结论，并非因果性上的完全解释。



## 参考文献

[1]. [https://baike.baidu.com/item/姚沁蕾/531809](https://baike.baidu.com/item/姚沁蕾/531809)

[2]. [https://ccjou.wordpress.com/2014/06/10/回歸均值/](https://ccjou.wordpress.com/2014/06/10/%e5%9b%9e%e6%ad%b8%e5%9d%87%e5%80%bc/)

[3]. Peter L Bernstein, *Against the Gods:The Remarkable Story of Risk*, 1996. 原文是 “Galton had created a revolution in our scientific ideas  [that] has modified our philosophy of science and even of life itself.”

[4]. Francis Galton, Regression towards mediocrity in hereditary stature, *Journal of the Anthropological Institute*, 15, pp 246-263 ,1886.

[5]. [Regression toward the mean](http://en.wikipedia.org/wiki/Regression_toward_the_mean) 原文是 “A child inherits partly from his parents, partly from his  ancestors. Speaking generally, the further his genealogy goes back, the  more numerous and varied will his ancestry become, until they cease to  differ from any equally numerous sample taken at haphazard from the race at large.” 



