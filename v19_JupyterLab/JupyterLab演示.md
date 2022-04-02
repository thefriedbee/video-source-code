# JupyterLab演示提纲

## 从Jupyter Notebook到JupyterLab的变化
1.	JupyterLab是在Jupyter Notebook(约2010开始)的基础上新一代的网页IDE(约2017开始)，目的是在不久的将来取代Notebook
2.	所有内容集中到一张网页上（原来是每个tab一个notebook，导航页面单独的tab）
3.	支持更多第三方组件与拓展工具，整体UI风格接近于visual studio code

## 安装与登陆
看GitHub项目链接，提供三种安装方式：
```
Conda: conda install -c conda-forge jupyterlab
Mamba: mamba install -c conda-forge jupyterlab
PIP: pip install jupyterlab
```

登陆：
与Jupyter notebook相似，在Terminal中输入（之前输入jupyter notebook）
```
> jupyter-lab
```

## JupyterLab的UI设计
### 一．地址导航/文件操作边栏
1.	Launcher新建文件（蓝底白色“+”）（notebook/ipython命令行/系统命令行/Markdown/Py/txt文本/帮助）
2.	新建文件夹/上传文件
3.	文件拖拽，重命名等十分方便

### 二．运行状态边栏
	查看所有正在运行的文件，可以控制关闭环境

### 三．MarkDown索引展示
	Notebook支持三大索引方式，对于很长的文件寻找位置非常方便。并且可以选择调整代码块缩略图，markdown具体文本，显示标题编号。

### 四．功能拓展
	JupyterLab有很多拓展功能可以进一步根据自己的需要安装，其中包括Jupyter项目组提供的拓展跟第三方的拓展。这些拓展类似于visual studio code中的第三方拓展，在稍后将操作实例中介绍。

### 五．属性检查器Property Inspector/Debugger等
	1. 右上角开启，检查cell对应的定义cell属性的元数据
	2. 开启Debugger调试器，可以通过增加断点等方式帮助调试

### 六．菜单栏
与其他软件的菜单栏大同小异，以下三点需要注意：
	1. Cell操作基本都在Edit中
	2. View改变工具视角
	3. Kernel核心选项控制当前Notebook的进程
	4. Tab：选择那个tab（用处不大，用鼠标点击要操作的tab即可）

### 七．底部状态栏
	右下角：Mode: 提示你在编辑代码文本，还是操纵cell
	左下角：简洁模式（只显示当前tab）；正在运行文件的状态；当前notebook运行的python核心

## 操作实例演示
1.	窗口排布
2.	一个文件多个视窗View
3.	使用contextual Help本地查看文档
4.	下载matplotlib图片
5.	更换UI主题（dark mode）
6.	将一个notebook中的cell转移到另一个notebook中
7.	任务：安装ipywidgets（官方插件）
8.	任务：安装变量检查器插件（类似于Spyder）（第三方插件）


部分参考资料，有用的博客文章
1.	https://jupyter.org/
2.	https://github.com/jupyterlab/jupyterlab
3.	https://jupyterlab.readthedocs.io/en/stable/
4.	https://towardsdatascience.com/getting-the-most-out-of-jupyter-lab-9b3198f88f2d
5.	https://medium.com/analytics-vidhya/why-switch-to-jupyterlab-from-jupyter-notebook-c6d98362945b#:~:text=JupyterLab%20runs%20in%20a%20single,you%20what%20you%20prefer%20more.
6.	https://www.analyticsvidhya.com/blog/2020/06/10-powerful-reasons-jupyterlab-data-science/
7.	https://towardsdatascience.com/optimizing-jupyter-notebook-tips-tricks-and-nbextensions-26d75d502663
8.	https://medium.com/@mjspeck/presenting-code-using-jupyter-notebook-slides-a8a3c3b59d67
9.	https://docs.bokeh.org/en/latest/
10.	https://docs.bokeh.org/en/latest/docs/gallery.html#gallery

