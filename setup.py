from setuptools import setup


setup(
    name='yahttp-server',
    version='1.0.0',
    description='Yet Another Http Server',
    author='Alexandre Cunha',
    author_email='alexandre.cunha@gmail.com',
    license='None',
    packages=[
        'yahttp',
    ],
    install_requires=[
        'tornado>=4.3',
    ],
    entry_points={'console_scripts': ['yahttp-server = yahttp.server:main']},
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    url='http://github.com/alercunha/yahttp-server',
)
