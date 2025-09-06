#!/usr/bin/env python3
"""
Setup script for ML Dashboard
"""

from setuptools import setup, find_packages
import os

# Read the README file
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Read requirements
def read_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        return [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="ml-dashboard",
    version="1.0.0",
    author="Aaron",
    author_email="aaron@example.com",
    description="A comprehensive web-based dashboard for visualizing machine learning model performance and predictions",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/machine-learning-dashboard",
    project_urls={
        "Bug Reports": "https://github.com/your-username/machine-learning-dashboard/issues",
        "Source": "https://github.com/your-username/machine-learning-dashboard",
        "Documentation": "https://github.com/your-username/machine-learning-dashboard#readme",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Framework :: Flask",
        "Environment :: Web Environment",
    ],
    python_requires=">=3.8",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "flake8>=5.0.0",
            "black>=22.0.0",
            "isort>=5.0.0",
            "mypy>=1.0.0",
        ],
        "test": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "pytest-mock>=3.0.0",
            "requests>=2.28.0",
        ],
        "docs": [
            "sphinx>=5.0.0",
            "sphinx-rtd-theme>=1.0.0",
            "myst-parser>=0.18.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "ml-dashboard=app:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["templates/*.html", "static/css/*.css", "static/js/*.js", "static/images/*"],
    },
    keywords=[
        "machine-learning",
        "dashboard",
        "visualization",
        "tensorflow",
        "flask",
        "d3.js",
        "bootstrap",
        "data-science",
        "ml",
        "ai",
        "monitoring",
        "analytics",
    ],
    zip_safe=False,
    platforms=["any"],
    license="MIT",
)
