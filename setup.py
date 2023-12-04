from setuptools import setup, find_packages


packages = find_packages()

package_data = {
    'tours': [
        'templates/tours/*.html',
        'templates/tours/tags/*.html',
        'static/*/*',
    ],
}

install_requires = [
    'Django',
]

setup(
    name='django-tours',
    version='0.0.4',
    author='Wilmer Martinez',
    author_email='info@wilmermartinez.dev',
    description='Django app to display tours with shepherdjs',
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/wilmerm/django-tours',
    license='MIT',
    packages=packages,
    package_data=package_data,
    install_requires=install_requires,
    keywords=[
        'django',
        'tours',
        'django-tours',
        'shepherdjs',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)