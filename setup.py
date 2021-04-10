from setuptools import setup

setup(
    name='oopygame',
    version='0.2.3',    
    description='An object oriented API based on pygame',
    url='https://github.com/Py-GNU-Unix/oopygame',
    author='Py-GNU-Unix',
    author_email='py.gnu.unix.moderator@gmail.com',
    license='GPL-3.0',
    packages=['oopygame'],
    install_requires=['pygame>=2.0',
                      'CairoSVG',
                      ],

    classifiers=[
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],

    include_package_data=True
)
