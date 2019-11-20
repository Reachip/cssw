import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Cohen Spread Sheet Wrapper",
    version="0.1",
    author="Rached Mejri",
    author_email="r.mejri74100@gmail.com",
    description="A wrapper to use the spread sheet of Dr. Jean-Michel Cohen concerning nutrition nutriments quantity per food family.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=["xlrd", "xlutils", "requests"],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
