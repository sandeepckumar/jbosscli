from setuptools import setup, find_packages

with open("README.md", 'r', encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()

setup(
    name="jbosscli",
    version="0.0.1",
    author="Sandeep C Kumar",
    author_email="sandeepkchenna@gmail.com",
    license="MIT License",
    description="Jboss EAP 7 CLI Tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='',
    py_modules=["jbosscli", "app"],
    packages=find_packages(),
    install_requires=[requirements],
    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    entry_points = """
    [console_scripts]
    jbosscli=jbosscli:main
    """
)
