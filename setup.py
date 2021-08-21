from setuptools import setup

setup(
    name="james",
    version='0.1',
    install_requires=[
        'Click',
        'jesse'
    ],
    entry_points='''
        [console_scripts]
        james=james.__init__:cli
    ''',
)
