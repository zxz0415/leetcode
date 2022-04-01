import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nonebot-plugin-leetcode",
    version="0.1",
    author="zxz0415",
    author_email="948125001@qq.com",
    description="one plugin used in nonebot , can send leetcode question to your qq friends and groups every day",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pythonml/douyin_image",
    packages=setuptools.find_packages(),
    install_requires=[
        'nonebot-plugin-apscheduler>=0.1.2',
        'nonebot2>=2.0.0a16',
        'nonebot-adapter-cqhttp>=2.0.0a16',
        'requests>=2.26.0'
    ],
    entry_points={
        'console_scripts': [
        ],
    },
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
)
