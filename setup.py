from setuptools import setup

setup(
    name='NlpToolkit-WordNet',
    version='1.0.17',
    packages=['WordNet', 'WordNet.Similarity'],
    url='https://github.com/StarlangSoftware/TurkishWordNet-Py',
    license='',
    author='olcaytaner',
    author_email='olcay.yildiz@ozyegin.edu.tr',
    description='Turkish WordNet KeNet',
    install_requires=['NlpToolkit-MorphologicalAnalysis']
)
