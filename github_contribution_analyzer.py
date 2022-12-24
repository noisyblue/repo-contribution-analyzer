import logging
from typing import Any

from github_api import GitHubAPI
from github_contribution_analysis import GitHubContributionAnalysis, RepositoryContribution, ContributionStats, \
    ContributionStatsItem


class GitHubContributionAnalyzer:
    def __init__(self):
        self.__logger = logging.getLogger(__name__)

    def analyze(self, github_user_name: str) -> GitHubContributionAnalysis:
        all_repos = GitHubAPI.get_user_repositories(github_user_name)

        analyses = [self.__analyze_repo_contributions(repo, github_user_name) for repo in all_repos]

        owning = [analysis for analysis in analyses if analysis.isOwned]
        forks = [analysis for analysis in analyses if analysis.isForked]
        stats = self.__build_stats(owning, forks)

        return GitHubContributionAnalysis(user_name=github_user_name,
                                          owningRepos=owning,
                                          forkedRepos=forks,
                                          stats=stats)

    def __analyze_repo_contributions(self, repo: Any, github_user_name: str) -> RepositoryContribution:
        repo_name = repo['full_name']
        repo_url = repo["html_url"]
        is_forked = repo["fork"]

        self.__logger.debug(f"Checking {repo_name}...")

        contributors: list[Any] = GitHubAPI.call_api(repo["contributors_url"])
        target_user = next(filter(lambda x: x["login"] == github_user_name, contributors), None)

        return RepositoryContribution(name=repo_name,
                                      url=repo_url,
                                      isOwned=not is_forked,
                                      isForked=is_forked,
                                      contributions=target_user['contributions'] if target_user is not None else 0)

    @staticmethod
    def __build_stats(owning_repos: list[RepositoryContribution],
                      forked_repos: list[RepositoryContribution]) -> ContributionStats:
        owning_repo_count = len(owning_repos)
        forked_repo_count = len(forked_repos)

        owning_contributed_repo_count = sum(1 for repo in owning_repos if repo.contributions > 0)
        forked_contributed_repo_count = sum(1 for repo in forked_repos if repo.contributions > 0)

        return ContributionStats(
            repoCount=ContributionStatsItem(
                owning=owning_repo_count,
                forked=forked_repo_count,
                total=owning_repo_count + forked_repo_count
            ),
            contributedRepoCount=ContributionStatsItem(
                owning=owning_contributed_repo_count,
                forked=forked_contributed_repo_count,
                total=owning_contributed_repo_count + forked_contributed_repo_count
            )
        )
