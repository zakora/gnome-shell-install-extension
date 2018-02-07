from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
    name='gnome-shell-install-extension',
    version='1.0.0',
    description="Install Gnome Shell extension from zip files.",
    long_description=long_description,
    url='https://github.com/zakora/gnome-shell-install-extension',
    author='zakora',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: X11 Applications :: Gnome',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Desktop Environment :: Gnome',
    ],
    python_requires='~=3.5',
    py_modules=['main'],
    entry_points={
        'console_scripts': ['gnome-shell-install-extension=main:main']
    },
)
