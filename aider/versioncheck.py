import sys

import pkg_resources
import requests

import aider


def check_version(print_cmd):
    try:
        response = requests.get("https://pypi.org/pypi/aider-chat/json")
        data = response.json()
        latest_version = data["info"]["version"]
        current_version = aider.__version__

        if pkg_resources.parse_version(latest_version) <= pkg_resources.parse_version(
            current_version
        ):
            return

        print_cmd(f"Newer version v{latest_version} is available. To upgrade, run:")
        py = sys.executable
        print_cmd(f"{py} -m pip install --upgrade aider-chat")
    except Exception as err:
        print_cmd(f"Error checking pypi for new version: {err}")


if __name__ == "__main__":
    check_version(print)
