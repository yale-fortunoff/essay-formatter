import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

requirements = open("./requirements.txt").read().splitlines()

setuptools.setup(
    name="essay-formatter", 
    version="0.0.1",
    author="Jake Kara",
    author_email="jake@jakekara.com ",
    description="Markdown to JSON formatter for essays",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yale-fortunoff/essay-formatter",
    project_urls={
        "Bug Tracker": "https://github.com/yale-fortunoff/essay-formatter/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    entry_points = {
        'console_scripts': ['essay-formatter=essay_formatter.__main__:main'],
    },
    install_requires=requirements

)