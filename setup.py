from setuptools import setup
setup(
    name = 'chinmay-cli',
    version = '0.1.0',
    packages = ['cli'],
    entry_points = {
        'console_scripts' : [
            'chinmaycli = cli.__main__:main'
        ]
    }
)