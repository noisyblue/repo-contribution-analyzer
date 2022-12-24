Repository Contribution Analyzer
================================

This is a script that analyzes a GitHub user's repository contributions and outputs the analysis result.
This script was made because the author was tired of tracking S/W engineer applicants' forked repository contributions during the engineer recruitment process.
<br/><br/>
Right now there are only a few features, but over time more features will be added if the author continue to suffer from repetitive manual work. 😉

## Features
- Owned/Forked Repositories summary
  - Name
  - URL
  - Contributions
- Statistics
  - Repository count
  - Contributed repository count

## Setup
```shell
pip install -r requirements.txt
```

## Execution
> ℹ️ You can execute the script without GitHub Personal Access Token.    
However, it is recommended to use your personal access token unless you can endure the GitHub rate limit error and its wait duration.  

```shell
GITHUB_TOKEN=<GITHUB_PERSONAL_ACCESS_TOKEN> python main.py github-user-name
```

## Console output
```shell
$ python main.py noisyblue
=== Analysis of noisyblue's GitHub repositories ===
Owning repositories:
noisyblue/kaggle-playground - https://github.com/noisyblue/kaggle-playground - 7 contributions
noisyblue/repo-contribution-analyzer - https://github.com/noisyblue/repo-contribution-analyzer - 1 contributions

Forked repositories:
noisyblue/iOSKenBurns - https://github.com/noisyblue/iOSKenBurns - 2 contributions
noisyblue/mybatis-mapper - https://github.com/noisyblue/mybatis-mapper - 2 contributions

📈 Statistics:
Repository count
- Total: 4
- Owning: 2
- Forked: 2

Contributed repository count
- Total: 4
- Owning: 2
- Forked: 2 
```
