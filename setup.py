import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyKoalaUtils", # Replace with your own username
    version="0.0.1",
    author="Jerome Parent",
    author_email="jerome.parent@lyncetec.com",
    description="Utility to open LynceeTec Koala bin files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jejmule/pyKoalaUtils",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
)