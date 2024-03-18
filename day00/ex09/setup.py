from setuptools import setup, find_packages


setup(
    name='ft_package',
    version='0.0.1',
    packages=find_packages(),
    author='Lucas Sokol',
    author_email='sokol.lucas@gmail.com',
    description='A small useless package from lusokol',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/lusokol/python/tree/main/day00/ex09',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Linux',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.10',
)
