from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='classifai',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'openai',
    ],
    entry_points={
        'console_scripts': [
            'classifai=classifai:main',
        ],
    },
    author='Thomas Thomas',
    author_email='irthomasthomas@Gmail.com',
    description='A command-line tool for AI-powered classification tasks using LLMs',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/irthomasthomas/classifai',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
