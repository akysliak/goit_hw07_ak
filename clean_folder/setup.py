from setuptools import setup, find_namespace_packages

setup(
    name='useful',
    version='1',
    description='Code for sorting and removing files/folders',
    url='https://github.com/akysliak/goit_hw07_ak',
    author='Anastasiia Kysliak',
    author_email='',
    license='MIT',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean-folder = clean_folder.clean:main']}
)