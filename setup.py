import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "rp_counter",
    version = "1.0.0",
    author = "Petr Verner",
    description = "A simple package used for counting words contained within specified characters",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/Sir-Badger/word_counter",
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
    python_requires = ">=3.10"
)