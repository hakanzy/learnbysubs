from setuptools import setup, find_packages
import os

setup(
    name='learnbysubs',
    version='0.1',
    author='Hakan OZAY',
    author_email='hakanzy@gmail.com',
    url='https://github.com/hakanzy/learnbysubs',
    description='Generate combined subtitle file with two different languages',
    long_description=os.path.join(os.path.dirname(__file__), 'README.md'),
    packages=find_packages(exclude=[]),
    entry_points={'console_scripts':
                  ['learnbysubs = learnbysubs:main']},
    install_requires=[
        'pysrt==1.0.0',
        'cchardet==0.3.5'
    ],
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
