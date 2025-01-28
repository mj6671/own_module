from setuptools import setup, find_packages

setup(
    name="yt_scp",
    version="0.1.0",
    author="Mahendran",
    author_email="mahendranj927@gmail.com",
    description="youtube url scraper with hashtag",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/mj6671/yt_scp",
    packages=find_packages(),
    install_requires=[
        "selenium>=4.0.0",
        "webdriver-manager>=4.0.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Ensure this matches your LICENSE
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    # Remove any line like `license_file="LICENSE"` if present
)
