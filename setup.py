from setuptools import setup, find_packages

setup(
    name='engineering_chatbot',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=[
        'fastapi>=0.111.0',
        'uvicorn[standard]>=0.30.0',
        'jinja2>=3.1.4',
        'pydantic>=2.7.4'
    ],
    description='Minimal engineering chatbot skeleton using FastAPI',
    author='Your Name',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Framework :: FastAPI'
    ]
)
