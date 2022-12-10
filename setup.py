from setuptools import setup, find_packages


'''
### 参考

> python--如何将自己的包上传到PyPi并可通过pip安装：https://blog.csdn.net/yifengchaoran/article/details/113447773


### 步骤
要将自己的python项目上传到PyPi，需要按照以下步骤操作：

+ 首先，你需要确保你的项目已经打包成了一个可以安装的python包。这通常需要在项目根目录下创建一个名为"setup.py"的文件，并在该文件中指定项目的依赖关系、安装选项等信息。

+ 其次，你需要在PyPi上注册一个账号，并登录。

+ 接下来，打开命令行界面，进入到你的项目根目录。

+ 输入"pip install twine"来安装twine工具。

+ 更新工具包： pip install --upgrade twine setuptools wheel

+ 使用"python setup.py sdist"命令来生成项目的源代码包。

+ 使用"python setup.py bdist_wheel"命令来生成项目的长描述。

+ 输入"twine upload dist/*"来上传项目的源代码包。

+ 在上传过程中，你需要输入你在PyPi上注册的用户名和密码。

一旦上传完成，你的项目就已经成功发布到了PyPi上。你可以在PyPi的网站上搜索你的项目名称，找到你的项目，并查看它的安装和使用说明。

### My environment

+ Without Proxy like v2ray
+ conda activate pypi-3.10

### Package URL

+ https://pypi.org/project/m2w/2.2.7/

'''

with open("./m2w/README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='m2w',
    version='2.2.7',
    description='Automatically upload and update local markdown to WordPress via Python',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    author='Bensz',
    author_email='hwb2012@qq.com',
    url="https://github.com/huangwb8/m2w", 
    packages=find_packages(),
     classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
)
