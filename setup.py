from setuptools import setup, find_packages


setup(
    name='ChunkUpload',
    version='0.1',
    description='A django app for uploading videos chunk by chunk and completing uploaded chunk after all chunks have been uploaded.',
    install_requires =[
        "django >= 3.0",
    ],
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    long_description=open('README.md').read(),
    url='https://github.com/mohammadGhasempour75', # should be github address
    auther= 'mohammad ghasempour',
    author_email='mamad.agha750202@gmail.com',
    classifiers=[
        #'development Status :: 4 - beta',
        #'Environment :: Web Environment',
        'programming Language :: Python :: 3',
        'license :: OSI Approved :: MIT License',
        'operating System :: OS Independent',
    ]
)