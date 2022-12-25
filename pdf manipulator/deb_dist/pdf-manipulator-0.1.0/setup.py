from setuptools import setup


with open("README.md", 'r',encoding="utf-8") as readme_file:
    long_description =readme_file.read()

setup(
    name="PDF_Manipulator",
    version = "0.1.0",
    description= "make pdf_manipulator a DEB package",
    long_description=long_description,
    long_description_content_type = 'text/markdown',
    author="2Math0",
    author_email="thomas.meshail@gmail.com",
    license="MIT",
    packages=["py"],
    package_dir={"py": "py/"},
    install_requires=[
        'PySimpleGUI',
        'fitz',
    ],
    data_files= [('share/applications', ['pdf_manipulator.desktop'])],
    python_requires = '>=3.6',
    

)