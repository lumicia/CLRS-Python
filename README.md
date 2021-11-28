# 算法导论学习笔记

使用 Python 实现算法导论一书中的算法和习题代码，并尝试用类型注解（type hint）标注函数和方法的参数与返回类型。变量仅标注一部分，类型非常直观或简单，以及难以写出的不做标注。测试代码不做标注。

Python 最新版本为 Python3.10，值得注意的类型注解特性：
-  无需导入 `typing` 模块将废弃的类型。例如标注一个参数 `a` 为数值的列表，Python3.8 及之前需要先导入 `List`，写成 `a: List[int]`。Python3.9 之后可以直接写 `a: list[int]`。
-  无需导入 `Union` 或 `Option`。Python3.10 之后 `Union[str, int]` 可以用 `str | int` 代替，`Option[str]` 可以用 `str | None` 代替。

笔记在个人博客：https://lumicia.github.io/tags/clrs。

## Chap2

- insertion sort
- merge sort