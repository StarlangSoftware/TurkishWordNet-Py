from setuptools import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='NlpToolkit-WordNet',
    version='1.0.18',
    packages=['WordNet', 'WordNet.Similarity'],
    url='https://github.com/StarlangSoftware/TurkishWordNet-Py',
    license='',
    author='olcaytaner',
    author_email='olcay.yildiz@ozyegin.edu.tr',
    description='Turkish WordNet KeNet',
    install_requires=['NlpToolkit-MorphologicalAnalysis'],
    long_description=long_description,
    long_description_content_type='text/markdown'
)
