from setuptools import setup

setup(
    name="tiktoken",
    package_data={"tiktoken": ["py.typed"]},
    packages=["tiktoken", "tiktoken_ext"],
    zip_safe=False,
)
