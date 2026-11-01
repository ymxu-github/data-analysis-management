# Python 数据分析学习与实战

本项目通过 Jupyter Notebook 演示 Python 数据分析的基础操作，并以电影数据为例，练习使用 Pandas 整理数据、使用 Matplotlib 绘制图表。

## 项目结构

```text
.
├── data/
│   ├── movies.csv                 # TOP 300 电影数据
│   ├── sales.csv                  # 销售示例数据
│   └── sales_output.csv           # 销售数据处理示例输出
├── demo/
│   ├── 01-jupyter-base.ipynb      # Jupyter 基础
│   ├── 02-pandas-base.ipynb       # Pandas 基础
│   ├── 03-pandas-dataframe.ipynb  # DataFrame
│   ├── 04-pandas-read-to.ipynb    # 数据读写
│   ├── 05-pandas-query.ipynb      # 查询
│   ├── 06-pandas-select.ipynb     # 数据选择
│   ├── 07-pandas-filter.ipynb     # 数据筛选
│   ├── 08-pandas-cleaning.ipynb   # 数据清洗
│   ├── 09-pandas-sort.ipynb       # 数据排序
│   ├── 10-pandas-group.ipynb      # 分组统计
│   ├── 11-matplotlib-base.ipynb   # Matplotlib 基础
│   ├── 12-matplotlib-detail.ipynb # 图表样式
│   ├── 13-matplotlib-subplots.ipynb # 多子图绘制
│   └── 14-top-300-moves.ipynb     # TOP 300 电影数据分析案例
└── top-300-moves.py               # 电影分析案例的 Python 脚本
```

建议按 `demo` 中的编号顺序学习。最后一个 Notebook 和 Python 脚本都围绕 `data/movies.csv` 展示电影数据分析。

## 环境准备

需要 Python 3.10 或更高版本。安装运行脚本所需的依赖：

```bash
python -m pip install pandas matplotlib
```

如需运行 Notebook，再安装并启动 Jupyter：

```bash
python -m pip install notebook
python -m notebook
```

启动后，在浏览器中打开 `demo` 目录下的 Notebook。

## 运行电影分析脚本

在项目根目录执行：

```bash
python top-300-moves.py
```

脚本会读取 `data/movies.csv`，并显示一个包含四张图的分析面板：

- 每年上映电影数量变化
- 不同语言的电影数量
- 不同类型的电影数量（多类型电影会分别计数）
- 电影评分分布（占比低于 2% 的评分合并为“其他”）

年份缺失时，脚本会尝试从“上映时间”字段提取年份。脚本根据自身所在目录定位 CSV，因此可从其他工作目录运行。

## 数据说明

`movies.csv` 包含电影名称、年份、上映时间、类型、语言和评分等字段。分析脚本只读取其中所需字段。`sales.csv` 用于 Notebook 中的读写和数据处理示例。

Matplotlib 图表设置了 `SimHei` 中文字体。若运行环境没有该字体，中文标签可能显示为方框或乱码；可安装 SimHei，或将 `top-300-moves.py` 中的字体设置改成系统已安装的中文字体。