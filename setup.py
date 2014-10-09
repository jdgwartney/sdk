from setuptools import setup

setup(
    name='boundary.plugins',
    version = '1.0',
    description='This is your awesome module',
    author='You',
    author_email='davidg@boundary.com',
    package_dir = {'': 'src/main/python'},
    packages = ['your', 'you.module'],
    test_suite = 'boundary.plugins.tests',
    use_2to3 = True,
    convert_2to3_doctests = ['src/main/python/README.txt'],
    use_2to3_fixers = ['your.fixers'],
    use_2to3_exclude_fixers = ['lib2to3.fixes.fix_import'],
)
