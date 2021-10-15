## Markdown 轻量级文本编辑语言简介
- 在纯文本文字的基础上，通过添加一些简明的符号，来实现很多常用的文档字体格式。

- 与纯粹的txt文档相比，与纯文档的难度相当，但是Markdown的格式更加丰富，没有浏览器/软件转化为HTML网页的话也可以作为纯文本阅读，非常适合解释。

- 本质上，是通过浏览器转化为HTML文档呈现在网页上。


## 支持六级标题：
# 我是一级标题
## 我是二级标题
### 我是三级标题
#### 我是四级标题
##### 我是五级标题
###### 我是六级标题


## 支持字体的变化
1. **加粗字体**
1. *斜体*
4. ***加粗斜体***

以上为有序列表，Markdown会自动排序。



## 链接🔗与图片
- [BiliBili](https://www.bilibili.com/)
- <a href="https://docs.github.com/cn/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax">GitHub《基本撰写和格式语法》</a>


图片：![《两只小狗狗》](狗狗.jpeg)


- 当链接失效的时候，显示《两只小狗狗》
- 本质上，Markdown会被浏览器编辑为html文档，所以你可以随意添加HTML的元素，例如添加图像元素：

<img src="狗狗1.jpeg"
     alt="《两只小狗狗》"
     style="float: left; margin-right: 10px;" />

<!--
我是HTML注释元素，虽然我在Markdown里面，但是转换时候你看不见我
-->


## 支持有一定复杂度的公式编辑(语法类似于LaTex)

$$ e^{ix} = \cos{x} + i \sin{x} $$

欧拉公式 $e^{ix} = \cos{x} + i \sin{x}$ 包含自然数$e$和虚数$i$。

## 代码块
Python code block
```python
fruits = ['苹果', '香蕉', '梨']
print(lst)
```

JavaScript code block
```js
let fruits = ['苹果', '香蕉', '梨']
console.log(fruits.length)
```

## 注意事项
#### 转行
一行最后使用两个空格  
两行中间空一整行

使用HTML行分割符<br>
这是结尾行


## 表格
下面是一个表格：
| 列1（左对齐） | 列2（居中）   | 列3（右对齐）   |
| :---        |    :----:   |          ---: |
| Header      | Title       | Here's this   |
| Paragraph   | Text        | And more      |


## 引用
> The secret to creativity is knowing how to hide your sources. 
> -- <cite>[Albert Einstein][1]</cite>

[1]: http://www.quotedb.com/quotes/2112


## Markdown使用场景：
- GitHub的Readme.md说明文件，Issue交流栏
- 各种在脚本语言中用来讲解问题的Notebook
- [Python Jupyter Notebook/JupyterLab/Colab](https://colab.research.google.com/)
- [R Markdown Notebook](https://rmarkdown.rstudio.com/)
- 本地记录信息(例如，Visio Studio Code/Sublime等安装MarkDown预览插件)

## 总结：
- 轻量级，快速有效
- 与HTML结合效果很好：
<img src="狗狗.jpeg" alt="《两只小狗》" style="width:50px;" />
- 复杂度有限，很复杂的公式，排版等还是要用其他工具如Word，LaTeX等