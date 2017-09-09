# learningNotes

***
17-8-27

不要使用font标签<br/>
使用相对的字体尺寸而不是使用固体尺寸（通过浏览器不能调整固定尺寸的大小，易用性不好，不方便残障人士)<br/>
使用“alt”属性为图片添加相应的文字
***
17-8-29

html(Hyper Text Markup Language)--超文本标记语言(不是编程语言)。<br/>
html标签通常是成对出现的，比如`<b>`和`</b>`，标签对中第一个标签是开始标签，第二个标签是结束标签，也被称为开放标签和闭合标签。

## 一、HTML基础教程

### 1.HTML元素

html元素指的是从开始标签到结束标签的所有代码<br/>
**空元素** ---
没有内容的HTML元素，空元素在开始标签中关闭，如`<br />`

### 2.HTML属性

html属性 ---
为HTML元素提供附加信息，属性总是以名称/值对的形式出现，如：`name="value"`,属性总是在HTML元素的开始标签中规定的。

### 3.HTML标题

标题标签只用于创建标题，不要仅仅为了产生大号文本或粗体而使用标题(这种情况用CSS或其他标签来替代)。因为标题被搜索引擎用来为网页的结构和内容编制索引，且为用户快速浏览网页来呈现文档结构。

### 4.HTML段落

`<p></p>`<br/>
`<br />`<br/>
`<hr />`在HTML页面中创建水平线，用于分割内容。

显示页面时，浏览器会移除源代码中多余的空格和空行，html代码中所有连续的空格或空行都会被算作一个空格

### 5.HTML样式

style属性用于改变HTML元素的样式

**不赞成使用的标签和属性**

标签:`<center> <font> <basefont> <s> <strike> <u>`<br/>
属性:`align bgcolor color`

对于以上的标签和属性，使用样式代替

**背景颜色**

`bgcolor`只能用于`body`元素上，已被淘汰，`background-color`属性可以为各种元素定义背景颜色

**字体、颜色、尺寸**

`font-family color font-size`属性分别定义元素中文本的字体系列、颜色和尺寸:<br/>
`<p style="font-family:arial;color:red;font-size:20px;">A paragraph.</p>`

被淘汰的`<font>`标签:<br/>
`<p><font size="5" face="arial" color="red">A paragraph.</font></p>`

**文本对齐**

`text-align`属性规定元素中文本的水平对齐方式:<br/>
`<h1 style="text-align:center">This is a heading</h1>`

被淘汰的align属性:<br/>
`<h1 align="center">This is heading 1</h1`

### 6.HTML格式化

- **文本格式化**<br/>
<b>this text is bold(粗体文本)</b> `<b>this text is bold</b>`<br/>
<strong>this text is strong(加重语气)</strong> `<strong>this text is strong</strong>`<br/>
<big>this text is big(大号字)</big> `<big>this text is big</big>`<br/>
<em>this text is emphasized(着重文字)</em> `<em>this text is emphasized</em>`<br/>
<i>this text is italic(斜体字)</i> `<i>this text is italic</i>`<br/>
<small>this text is small(小号字)</small> `<small>this text is small</small>`<br/>
this text contains<sub>subscript(下标字)</sub> `this text contains<sub>subscript</sub>`<br/>
this text contains<sup>superscript(上标字)</sup> `this text contains<sup>superscript</sup>`

- **预格式文本**<br/>
  <pre>这是 预格式文本
  它保留了 空格 和
  换行。
  pre标签很适合显示计算机代码 </pre>
  `<pre>这是 预格式文本
  它保留了 空格 和
  换行。
  pre标签很适合显示计算机代码 </pre>`

- **“计算机输出”标签**<br/>
用于显示计算机/编程代码

  <code>Computer code(计算机代码)</code> `<code>Computer code</code>` `<code>`不保留多余的空格和折行<br/>
  <kbd>Keyboard input(键盘码)</kbd> `<kbd>Keyboard input</kbd>`<br />
  <tt>Teletype text(打字机代码)</tt> `<tt>Teletype text</tt>`<br />
  <samp>Sample text(计算机代码样本)</samp> `<samp>Sample text</samp>`<br />
  <var>Computer variable(变量)</var> `<var>Computer variable</var>`

- **缩写和首字母缩写**<br/>
<abbr title="etcetera">etc.</abbr> `<abbr title="etcetera">etc.</abbr>`定义缩写<br/>
<acronym title="World Wide Web">WWW</acronym> `<acronym title="World Wide Web">WWW</acronym>`定义首字母缩写

  在某些浏览器中，当您把鼠标移至缩略词语上时，title 可用于展示表达的完整版本。对缩写进行标记能够为浏览器、翻译系统以及搜索引擎提供有用的信息

- **文字方向**<br/>
<bdo dir="rtl">Here is some Hebrew text</bdo>`<bdo dir="rtl">Here is some Hebrew text</bdo>`<br/>
如果您的浏览器支持 bi-directional override (bdo)

- **块引用**<br/>
  这是长的引用：(`<blockquote></blockquote>`)
  <blockquote>五十年来，WWF 一直致力于保护自然界的未来。 世界领先的环保组织，WWF 工作于 100 个国家，并得到美国一百二十万会员及全球近五百万会员的支持。</blockquote>

  浏览器通常会对`<blockquote>`进行缩进处理

  这是短的引用：
  <q>这是短的引用。</q>(`<q></q>`)<br/>
  浏览器通常会为`<q>`元素包围引号

  使用`<blockquote>`元素的话，浏览器会插入换行和外边距，而`<q>`元素不会有任何特殊的呈现

  `<cite>`定义著作的标题<br/>
  <cite>The Scream</cite> `<cite>The Scream</cite> `(浏览器通常以斜体显示`<cite>`元素)

  `<dfn>`定义项目或缩写的定义<br/>
  The <dfn title="World Health Organization">WHO</dfn> was founded in 1948.`The <dfn title="World Health Organization">WHO</dfn> was founded in 1948.`

- **删除字效果和插入字效果**<br/>
  一打有 <del>二十</del><ins>十二</ins>件 `一打有<del>二十</del><ins>十二</ins>件`

  大多数浏览器会改写为删除文本和下划线文本<br/>
  一些老式浏览器会把删除文本和下划线文本显示为普通文本

### 7.HTML CSS
当浏览器读到一个样式表，它就会按照这个样式表来对文档进行格式化

- **外部样式表**<br/>
使用外部样式表，可以通过更改一个文件来改变整个站点的外观，可以将样式应用到多个界面。<br/>
`<head><link rel="stylesheet" type="text/css" href="mystyle.css"></head>`

- **内部样式表**<br/>
在head部分通过`<style>`标签定义内部样式表(当单个文件需要特别样式时)<br/>
`<head><style type="text/css">body {background-color: red} p {margin-left: 20px}</style></head>`

- **内联样式**<br/>
当特殊的样式需要应用到个别元素时<br/>
`<p style="color: red; margin-left: 20px">This is a paragraph</p>`

### 8.HTML 链接
超链接可以是文字或是图像，可以点击这些内容来跳转到新的文档或者当前文档中的某个部分。我们使用`<a>`标签来在HTML中创建链接。

**`<a>`标签的使用方式:**
- 通过使用href属性 --- 创建指向另一个文档的链接
- 通过使用name属性 --- 创建文档内的书签

**链接语法：**`<a href="url">link text</a>`<br />
href属性规定链接的目标<br />
“链接文本”不必一定是文本，图片或其他HTML元素都可以成为链接。

- **HTML链接 --- target属性**<br/>
使用target属性，可定义被链接的文档在什么地方显示<br />
`<a href="http://www.w3school.com.cn/" target="_blank">Visit W3School!</a>` --- 链接在新窗口打开

- **HTML链接 --- name属性**<br/>
  name属性规定锚(anchor)的名称；<br />
  可以使用name属性创建HTML页面中的书签；<br />
  书签不会以任何特殊方式显示，它对读者是不可见的；<br/>
  当使用命名锚(named anchors)时，可以创建直接跳到该命名锚(如页面中某个小节)的链接，这样读者就不用来回滚动页面来寻找有用信息了

  *命名锚的语法：*`<a name="label">锚（显示在页面上的文本）</a>`(可以使用id属性来替代name属性，命名锚)

  如：<br/>
  先在HTML文档中对锚进行命名（创建一个书签）：<br/>
  <a name="tips">基本的注意事项 --- 有用的提示</a>`<a name="tips">有用的提示</a>`;<br/>
  再在同一个文档中创建指向该锚的链接：<br/>
  <a href="#tips">有用的提示</a>`<a href="#tips">有用的提示</a>"`

  <i>PS:要始终将正斜杠添加到子文件夹。如果这样书写链接：href="http://www.w3school.com.cn/html" ，就会向服务器产生两次HTTP请求。因为服务器会添加正斜杠到这个地址，然后创建一个新请求 --- </i>href="http://www.w3school.com.cn/html/"

### 9.HTML图像
图像标签`<img>`是空标签 --- 它只包含属性，没有闭合标签<br/>

源属性（src）--- src指source，源属性的值是图像的URL地址(URL指存储图像的位置)<br/>
替换文本属性（alt） --- alt属性为图像定义一串预备的可替换的文本，在浏览器无法载入图像时，替换文本会告诉读者他们所失去的信息

`<img src="url" alt="describe picture" />`

向HTML页面添加**背景图片**：`<html><body background="....jpg"></body></html>`<br/>

在文字中**排列图像**：`<img src="..." alin="bottom"`、`<img src="..." alin="middle"`、`<img src="..." alin="top"`(默认对齐方式为bottom)

在带有图像的段落中，若将图像的align属性设置为“left”，图像将**浮动**到文本的左侧，若将图像的align属性设置为“right”，图像将浮动到文本的右侧

**创建图像映射**:创建带有可供点击区域的图像地图，其中的每个区域都是一个超级链接`usemap`(`<map>`定义图像地图,`<area>`定义图像地图中的可点击区域)

**把图像转换为图像映射**`<img src="....jpg" ismap />`


***
### 10.HTML表格
每个表格由`table`标签开始<br />
每个表格行由`tr`标签开始<br />
每个表格数据由`td`标签开始

一列：
<table border="1">
<tr>
  <td>100</td>
</tr>
</table>

```
<table border="1">
<tr>
  <td>100></td>
</tr>
</table>
```


一行三列：
<table border="1">
<tr>
  <td>100</td>
  <td>200</td>
  <td>300</td>
</tr>
</table>

```
<table border="1">
<tr>
  <td>100</td>
  <td>200</td>
  <td>300</td>
</tr>
</table>
```



两行三列：
<table border="1">
<tr>
  <td>100</td>
  <td>200</td>
  <td>300</td>
</tr>
<tr>
  <td>400</td>
  <td>500</td>
  <td>600</td>
</tr>
</table>

```
<table border="1">
<tr>
  <td>100</td>
  <td>200</td>
  <td>300</td>
</tr>
<tr>
  <td>400</td>
  <td>500</td>
  <td>600</td>
</tr>
</table>
```
表格由`table`标签定义，每个表格均有若干行（由`tr`标签定义），每行被分割为若干单元格（由`td`标签定义）字母td指表格数据(table data)，即数据单元格的内容，数据单元格可以包含文本、图片、列表、段落、表单、水平线、表格等。


`th`标签定义表头，大多数浏览器会把表头定义为粗体居中的文本
<table border="1">
<tr>
  <th>Heading</th>
  <th>Another Heading</th>
</tr>
<tr>
  <td>row 1 cell 1</td>
  <td>row 1 cell 2</td>
</tr>
<tr>
  <td>row 2 cell 1</td>
  <td>row 2 cell 2</td>
</tr>
</table>

```
<table border="1">
<tr>
  <th>Heading</th>
  <th>Another Heading</th>
</tr>
<tr>
  <td>row 1 cell 1</td>
  <td>row 1 cell 2</td>
</tr>
<tr>
  <td>row 2 cell 1</td>
  <td>row 2 cell 2</td>
</tr>
</table>
```

**表格中的空单元格**<br/>
一些浏览器可能无法显示出空单元格的边框<br/>
解决办法：在空单元格中t添加一个空格占位符
```
<table border="1">
<tr>
  <td>100</td>
  <td>200</td>
</tr>
<tr>
  <td>&nbsp;</td>
  <td>400</td>
</tr>
</table>
```
no-breaking空格：`&nbsp;`

表格标题：
<table border="1">
<caption>我的标题</caption>
<tr>
  <td>100</td>
  <td>200</td>
</tr>
<tr>
  <td>300</td>
  <td>400</td>
</tr>
</table>

```
<table border="1">
<caption>我的标题</caption>
<tr>
  <td>100</td>
  <td>200</td>
</tr>
<tr>
  <td>300</td>
  <td>400</td>
</tr>
</table>
```

**跨行或跨列的表格单元格**
<table border="1">
<tr>
  <td>1</td>
  <td>2</td>
  <td>3</td>
</tr>
<tr>
  <td rowspan="2">47</td>
  <td colspan="2">56</td>
</tr>
<tr>
  <td>8</td>
  <td>9</td>
</tr>
<table>

```
<table border="1">
<tr>
  <td>1</td>
  <td>2</td>
  <td>3</td>
</tr>
<tr>
  <td rowspan="2">47</td>
  <td colspan="2">56</td>
</tr>
<tr>
  <td>8</td>
  <td>9</td>
</tr>
<table>
```

`rowspan="2"`横跨两行<br/>
`colspan="2"`横跨两列

**单元格边距**
<table border="1" cellpadding="10">
<tr>
  <td>1</td>
  <td>2</td>
</tr>
<tr>
  <td>3</td>
  <td>4</td>
</tr>
<table>

`cellpadding`创建单元格内容与边框之间的空白

**单元格间距**

`cellspacing`增加单元格之间的距离

**向表格添加背景颜色或背景图像**

背景颜色：
```
<table border="1" bgcolor="red">
<tr>
  <td>1</td>
  <td>2</td>
</tr>
<tr>
  <td>3</td>
  <td>4</td>
</tr>
<table>
```

背景图像：
```
<table border="1" background="....jpg">
<tr>
  <td>1</td>
  <td>2</td>
</tr>
<tr>
  <td>3</td>
  <td>4</td>
</tr>
<table>
```

**在表格单元中排列内容**
```
<table border="1">
<tr>
  <td align="left">1</td>
  <td align="right">2</td>
</tr>
<tr>
  <td align="left">3</td>
  <td align="right">4</td>
</tr>
<table>
```

**使用frame属性控制围绕表格的边框**

`frame="box"`:
<table frame="box">
  <tr>
    <th>Month</th>
    <th>Savings</th>
  </tr>
  <tr>
    <td>January</td>
    <td>$100</td>
  </tr>
</table>

`frame="above"`:
<table frame="above">
  <tr>
    <th>Month</th>
    <th>Savings</th>
  </tr>
  <tr>
    <td>January</td>
    <td>$100</td>
  </tr>
</table>

`frame="below"`
<table frame="below">
  <tr>
    <th>Month</th>
    <th>Savings</th>
  </tr>
  <tr>
    <td>January</td>
    <td>$100</td>
  </tr>
</table>

`frame="hsides"`上下
<table frame="hsides">
  <tr>
    <th>Month</th>
    <th>Savings</th>
  </tr>
  <tr>
    <td>January</td>
    <td>$100</td>
  </tr>
</table>

`frame="vsides"`左右
<table frame="vsides">
  <tr>
    <th>Month</th>
    <th>Savings</th>
  </tr>
  <tr>
    <td>January</td>
    <td>$100</td>
  </tr>
</table>

### 11.HTML列表
**无序列表**
<ul type="disc">
  <li>咖啡</li>
  <li>茶</li>
  <li>牛奶</li>
</ul>

```
<ul type="disc">
  <li>咖啡</li>
  <li>茶</li>
  <li>牛奶</li>
</ul>
```
type的值有disc，circle，square

**有序列表**
<ol start="50">
  <li>咖啡</li>
  <li>茶</li>
  <li>牛奶</li>
</ol>

```
<ol start="50">
  <li>咖啡</li>
  <li>茶</li>
  <li>牛奶</li>
</ol>
```
type的值有A(字母列表),a(小写字母列表),I(罗马字母列表),i(小写罗马字母列表)

**定义列表**
<dl>
   <dt>计算机</dt>
   <dd>用来计算的仪器 ... ...</dd>
   <dt>显示器</dt>
   <dd>以视觉方式显示信息的装置 ... ...</dd>
</dl>

```
<dl>
   <dt>计算机</dt>
   <dd>用来计算的仪器 ... ...</dd>
   <dt>显示器</dt>
   <dd>以视觉方式显示信息的装置 ... ...</dd>
</dl>
```
自定义列表不仅仅是一列项目，而是项目及其注释的组合<br/>
自定义列表以`<dl>`标签开始，每个自定义列表项以`<dt>`开始，每个自定义列表项的定义以`<dd>`开始

### 12.HTML块

- **块级元素**(block level element)<br/>
  块级元素在浏览器显示时，通常会以新行来开始和结束
- **内联元素**(inline element)<br/>
  前后不换行
- **`div`元素**(块级元素，是可用于组合其他HTML元素的容器)<br/>
  和CSS一起使用，可用于对大的内容块设置样式属性；<br/>
  可用于文档布局
- **`span`元素**(内联元素，可用作文本的容器)<br/>
  当与CSS一起使用时，可用于为部分文本设置样式属性
