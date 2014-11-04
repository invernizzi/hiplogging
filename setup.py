from setuptools import setup


setup(
    description="HipChat support for the Python logging module",
    name='hiplogging',
    url='https://github.com/invernizzi/hiplogging',
    version='0.1',
    packages=['hiplogging'],
    author='Luca Invernizzi',
    author_email='invernizzi.l@gmail.com',
    license='MIT',
    long_description=open('README.md').read(),
    keywords=['hipchat', 'log', 'logging'],
    download_url = 'https://github.com/invernizzi/hiplogging/tarball/0.1',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
)
