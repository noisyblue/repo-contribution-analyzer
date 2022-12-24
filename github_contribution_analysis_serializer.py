from abc import abstractmethod
from enum import Enum
from typing import TypeVar

from github_contribution_analysis import GitHubContributionAnalysis

T = TypeVar('T')


class AnalysisSerializationFormat(Enum):
    TEXT = 1,
    JSON = 2


class GitHubContributionAnalysisSerializer:
    @abstractmethod
    def serialize(self, analysis: GitHubContributionAnalysis) -> T:
        raise NotImplementedError()


class GitHubContributionAnalysisSerializerFactory:
    @staticmethod
    def get_serializer(serialization_format: AnalysisSerializationFormat) -> GitHubContributionAnalysisSerializer:
        if serialization_format == AnalysisSerializationFormat.TEXT:
            return GitHubContributionAnalysisTextSerializer()
        elif serialization_format == AnalysisSerializationFormat.JSON:
            raise NotImplementedError()
        else:
            raise Exception(f"Unknown format: {serialization_format}")


class GitHubContributionAnalysisTextSerializer(GitHubContributionAnalysisSerializer):
    def serialize(self, analysis: GitHubContributionAnalysis) -> str:
        owning_repos_summary = "\n".join(
            [f"{repo.name} - {repo.url} - {repo.contributions} contributions" for repo in analysis.owningRepos])
        forked_repos_summary = "\n".join(
            [f"{repo.name} - {repo.url} - {repo.contributions} contributions" for repo in analysis.forkedRepos])

        result = f"""\n=== Analysis of {analysis.user_name}'s GitHub repositories ===
Owning repositories:
{owning_repos_summary}

Forked repositories:
{forked_repos_summary}

📈 Statistics:
Repository count
- Total: {analysis.stats.repoCount.total}
- Owning: {analysis.stats.repoCount.owning}
- Forked: {analysis.stats.repoCount.forked}

Contributed repository count
- Total: {analysis.stats.contributedRepoCount.total}
- Owning: {analysis.stats.contributedRepoCount.owning}
- Forked: {analysis.stats.contributedRepoCount.forked}
"""

        return result
