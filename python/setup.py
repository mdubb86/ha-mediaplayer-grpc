import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="ha-mediaplayer-grpc",
    version="0.1.6",
    packages=["mediaplayer"],
    url="https://github.com/mdubb86/ha-mediaplayer-grpc",
    description="Generated GRPC client/server code for implementing a Home Assistant Media Player integration",
    long_description=README,
    long_description_content_type="text/markdown",
)