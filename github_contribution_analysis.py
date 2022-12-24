from dataclasses import dataclass


@dataclass
class RepositoryContribution:
    name: str
    url: str
    isOwned: bool
    isForked: bool
    contributions: int


@dataclass
class ContributionStatsItem:
    owning: int
    forked: int
    total: int


@dataclass
class ContributionStats:
    repoCount: ContributionStatsItem
    contributedRepoCount: ContributionStatsItem


@dataclass
class GitHubContributionAnalysis:
    user_name: str
    owningRepos: list[RepositoryContribution]
    forkedRepos: list[RepositoryContribution]
    stats: ContributionStats
