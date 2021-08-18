# 算法导论学习笔记

个人使用 Python 实现算法导论一书中的算法和习题代码，部分代码参考了其他人的实现。

为了方便学习类型注解同时向前兼容，使用了 Python 3.9，这样可以避免导入 `typing` 模块将废弃的类型。例如标注一个参数 `a` 为数值的列表，之前需要先导入 `List`，写成 `a: List[int]`。Python 3.9 之后可以直接写 `a: list[int]`。

实现过程中记录的笔记在个人博客：https://lumicia.github.io/categories/algorithm/。
