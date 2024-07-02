from setuptools import setup, find_packages

# 读取README.md作为long_description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="xmem",  # 包名
    version="1.0.0",  # 版本号
    author="Your Name",  # 作者
    author_email="your.email@example.com",  # 作者邮箱
    description="A brief description of your package",  # 简短描述
    long_description=long_description,  # 长描述，从README.md中读取
    long_description_content_type="text/markdown",  # 长描述的内容类型
    url="https://github.com/ar-mine/XMem",  # 项目主页
    packages=find_packages(),  # 自动查找项目中所有包
    classifiers=[  # 分类器，用于在PyPI上分类
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # 兼容的Python版本
    install_requires=[  # 安装依赖
        # 'numpy>=1.18.5',
        # 'pandas>=1.0.5',
        # 其他依赖
    ],
    extras_require={  # 可选依赖
        'dev': [
            # 'pytest>=6.0',
            # 'flake8>=3.8.3',
            # 其他开发依赖
        ],
    },
    entry_points={  # 定义命令行工具
        'console_scripts': [
            # 'my_tool=my_package.module1:main_func',
        ],
    },
    include_package_data=True,  # 包含包中的非代码文件
    package_data={  # 指定包含在包中的数据文件
        # 'my_package': ['data/*.dat'],
    },
)
