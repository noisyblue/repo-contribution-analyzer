#!/usr/bin/env python3
import logging
import os
import sys

from github_api import GitHubAPI
from github_contribution_analysis_serializer import GitHubContributionAnalysisSerializerFactory, \
    AnalysisSerializationFormat
from github_contribution_analyzer import GitHubContributionAnalyzer

if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} github-user-name")
    sys.exit(1)


def main():
    github_user_name = sys.argv[1]

    GitHubAPI.initialize(os.environ.get("GITHUB_TOKEN"))

    logging.basicConfig(
        format='%(asctime)s:%(levelname)s: %(message)s',
        level=logging.DEBUG
    )

    analyzer = GitHubContributionAnalyzer()
    result = analyzer.analyze(github_user_name)

    serializer = GitHubContributionAnalysisSerializerFactory.get_serializer(AnalysisSerializationFormat.TEXT)
    print(serializer.serialize(result))


if __name__ == '__main__':
    sys.exit(main())
