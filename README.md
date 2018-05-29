# pypi_package_example
python 打包分发研究

# Example Package

This is a simple example package. You can use
[Github-flavored Markdown](http://guides.github.com/features/mastering-markdown/)
to write your content.

version = 0.0.1

## 特性

* 基本Pypi打包发布流程总结


## 流程

* 按本项目结构创建项目

编辑 setup.py文件

指定项目名称 版本 系统依赖等元数据

- 进入打包流程



```Python
# 安装打包发布工具
pip install -U setuptools wheel twine
# 打包
python setup.py bdist bdist_wheel
# 上传打包 需要输入仓库的账号密码,注意测试仓库与正式仓库是独立的
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
# 安装包
pip install --index-url https://test.pypi.org/simple/ pypi_package_example_wjw19854==0.0.1 -U
```

### Note

- 本流程样例是上长传到测试仓库 并从测试仓库安装.如果要上传到正式共有仓库 ,去掉url参数即可.
- 要上传成功必须在对应仓库注册账号

## TODO

- 研究其他打包替代方案如 [poetry](https://github.com/sdispater/poetry) 或者 [hatch](https://github.com/ofek/hatch)
