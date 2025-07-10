from setuptools import setup, find_packages

setup(
    name='cocotbext-modbus',
    version='0.1.0',
    description='Reusable Verification IP for MODBUS RTU Protocol using Cocotb',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Rohith Mudigonda',
    author_email='rohith.mudigonda@example.com',
    url='https://github.com/yourusername/cocotbext-modbus',
    packages=find_packages(include=['cocotbext', 'cocotbext.modbus']),
    install_requires=[
        'cocotb>=1.7',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Electronic Design Automation (EDA)',
    ],
    python_requires='>=3.7',
    include_package_data=True,
    zip_safe=False,
)

