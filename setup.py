# python setup.py bdist_wheel 打包成wheel文件

from setuptools import setup

VERSION = '1.0.0'
setup(
    name="TEST",
    packages=['static'],
    version=VERSION,
    description="package test",
    install_requires=[],
    author=['zyf'],
    author_email=['1256809441@qq.com'],
    url='',
    # project_urls={
    #         'Documentation': 'https://packaging.python.org/tutorials/distributing-packages/',
    #         'Funding': 'https://donate.pypi.org',
    #         'Source': 'https://github.com/pypa/sampleproject/',
    #         'Tracker': 'https://github.com/pypa/sampleproject/issues',
    # },
    # download_url='https://github.com/invernizzi/scapy-http/tarball/' + VERSION,
    # keywords=['http', 'scapy', 'newtork', 'dissect', 'packets'],
    keywords=['test'],
    python_requires='>=3'
)