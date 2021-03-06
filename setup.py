# pylint: disable = C0111
from setuptools import find_packages, setup

with open("README.md", "r") as f:
    DESCRIPTION = f.read()

setup(name="cord19q",
      version="2.2.0",
      author="NeuML",
      description="CORD-19 Analysis",
      long_description=DESCRIPTION,
      long_description_content_type="text/markdown",
      url="https://github.com/neuml/cord19q",
      project_urls={
          "Documentation": "https://github.com/neuml/cord19q",
          "Issue Tracker": "https://github.com/neuml/cord19q/issues",
          "Source Code": "https://github.com/neuml/cord19q",
      },
      license="Apache 2.0: http://www.apache.org/licenses/LICENSE-2.0",
      packages=find_packages(where="src/python/"),
      package_dir={"": "src/python/"},
      keywords="search embedding machine-learning nlp covid-19 medical scientific papers",
      python_requires=">=3.6",
      entry_points={
          "console_scripts": [
              "cord19q = cord19q.shell:main",
          ],
      },
      install_requires=[
          "faiss-gpu>=1.6.3",
          "fasttext>=0.9.2",
          "html2text>=2020.1.16",
          "mdv>=1.7.4",
          "networkx>=2.4",
          "nltk>=3.5",
          "numpy>=1.18.4",
          "pymagnitude @ git+https://github.com/neuml/magnitude",
          "PyYAML>=5.3",
          "regex>=2020.5.14",
          "scikit-learn>=0.22.2.post1",
          "scipy>=1.4.1",
          "torch>=1.4.0",
          "tqdm>=4.46.0",
          "transformers>=2.11.0"
      ],
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Operating System :: OS Independent",
          "Programming Language :: Python :: 3",
          "Topic :: Software Development",
          "Topic :: Text Processing :: Indexing",
          "Topic :: Utilities"
      ])
