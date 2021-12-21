from setuptools import find_packages, setup

setup(
    name='custom_cli',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
    entry_points={
        'flask.commands': [
            'command_plugin=command_plugin:cli'
        ],
        'console_scripts': [
            'custom_script=custom_script:cli'
        ],
    },
)
