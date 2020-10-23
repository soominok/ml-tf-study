import setuptools

# root directory 에서 pip install .
# # 하면 setup.py가 전체 파일에서 실행되는 것!
with open("README.md","r") as fh:
    long_description  = fh.read()
    setuptools.setup(
    name='com_titanic_api',
    version='1.0',
    description='Python Distribution Utilities',
    long_description=long_description,
    author='soominok',
    author_email='sumin00331@naver.com',
    url='https://www.python.org/sigs/distutils-sig/',
    packages=setuptools.find_packages(),
    python_requires='>=3.7'
)