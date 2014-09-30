from setuptools import setup

setup(
    name='boundary.plugin',
    version = '1.0',
    description='This is your awesome module',
    author='You',
    author_email='davidg@boundary.com',
    package_dir = {'': 'src'},
    packages = ['your', 'you.module'],
    test_suite = 'your.module.tests',
    use_2to3 = True,
    convert_2to3_doctests = ['src/your/module/README.txt'],
    use_2to3_fixers = ['your.fixers'],
    use_2to3_exclude_fixers = ['lib2to3.fixes.fix_import'],
)
