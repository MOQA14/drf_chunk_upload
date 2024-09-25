from setuptools import setup, find_packages


setup(
    name='ChunkUpload',
    version='0.3',
    description='A django app for uploading videos chunk by chunk and completing uploaded chunk after all chunks have been uploaded.',
    install_requires =[
        "django >= 3.0",
    ],
    test_require=[
        'pytest',
    ],
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/MOQA14',
    auther= 'mohammad ghasempour',
    author_email='mamad.agha750202@gmail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ]
)