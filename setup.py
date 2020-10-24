from setuptools import setup

setup(
    name='NlpToolkit-WordNet',
    version='1.0.16',
    packages=['WordNet', 'WordNet.Similarity'],
    url='https://github.com/olcaytaner/TurkishWordNet-Py',
    license='',
    author='olcay',
    author_email='olcaytaner@isikun.edu.tr',
    description='Turkish WordNet KeNet',
    install_requires=['NlpToolkit-MorphologicalAnalysis']
)
