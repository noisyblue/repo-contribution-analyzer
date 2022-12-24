import logging
import time
from typing import Any, TypeVar

import requests

T = TypeVar('T', bound="GitHubAPI")


class GitHubAPI:
    __is_initialized = False
    __github_token = None
    __logger = logging.getLogger(__name__)

    @staticmethod
    def initialize(github_token=None):
        GitHubAPI.__github_token = github_token
        GitHubAPI.__is_initialized = True

    @staticmethod
    def get_user_repositories(user_name: str) -> list[Any]:
        url = f"https://api.github.com/users/{user_name}/repos"
        return GitHubAPI.call_api(url)

    @staticmethod
    def call_api(url: str, should_retry_on_rate_limit=True) -> T:
        GitHubAPI.__raise_if_not_initialized()

        GitHubAPI.__logger.debug(f"Calling {url} ...")

        headers = {}
        if GitHubAPI.__github_token:
            headers["Authorization"] = f"Bearer {GitHubAPI.__github_token}"

        res = requests.get(url, headers=headers)

        if res.status_code == 403 and should_retry_on_rate_limit:
            if int(res.headers["x-ratelimit-remaining"]) == 0:
                seconds_to_reset = int(res.headers["X-ratelimit-reset"]) - int(time.time()) + 1

                GitHubAPI.__logger.warning(f"Rate limit exceeded. Retrying after {seconds_to_reset} seconds of sleep...")
                time.sleep(seconds_to_reset)

                res = requests.get(url)

        res.raise_for_status()

        return res.json()

    @staticmethod
    def __raise_if_not_initialized() -> None:
        if not GitHubAPI.__is_initialized:
            raise RuntimeError("GitHubAPI is not initialized!")
