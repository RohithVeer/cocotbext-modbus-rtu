from setuptools import setup, find_packages

setup(
    name='cocotbext-modbus',
    version='0.1.0',
    description='Reusable VIP for Modbus RTU Protocol using Cocotb',
    author='Rohith Mudigonda',
    author_email='your.email@example.com',
    packages=find_packages(include=['cocotbext', 'cocotbext.modbus']),
    install_requires=['cocotb>=1.7'],
    include_package_data=True,
    zip_safe=False,
)

