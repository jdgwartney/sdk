from distutils.core import setup

setup(
    name='meter-plugin-sdk',
    version='0.1.0',
    url="http://github.io/boundary/meter-plugin-sdk-python",
    author='David Gwartney',
    author_email='david_gwartney@bmc.com',
    packages=['meter_plugin_sdk', ],
    scripts=[
        'bin/hell',
    ],
    package_data={'meter_plugin_sdk': ['templates/*']},
    license='LICENSE.txt',
    description='TrueSight Pulse Meter Plugin SDK for Python',
    long_description=open('README.txt').read(),
    install_requires=[
        "tinyrpc",
    ],
)
