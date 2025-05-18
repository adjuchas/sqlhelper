# 这是github开放api的测试
import requests
from typing import List, Dict, Optional

def get_github_commits(
    owner: str,
    repo: str,
    token: Optional[str] = None,
    since: Optional[str] = None,
    until: Optional[str] = None,
    per_page: int = 30,
    page: int = 1
) -> List[Dict]:
    """
    获取 GitHub 仓库的提交历史
    
    Args:
        owner: 仓库所有者用户名或组织名
        repo: 仓库名称
        token: GitHub 个人访问令牌(可选，用于私有仓库或提高速率限制)
        since: 只返回此日期之后的提交(ISO 8601格式，如2023-01-01T00:00:00Z)
        until: 只返回此日期之前的提交(ISO 8601格式)
        per_page: 每页返回的结果数量(默认30，最大100)
        page: 页码(默认1)
    
    Returns:
        包含提交信息的字典列表
        
    Raises:
        requests.exceptions.HTTPError: 如果API请求失败
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    headers = {"Accept": "application/vnd.github.v3+json"}
    
    if token:
        headers["Authorization"] = f"token {token}"
    
    params = {
        "per_page": 2,  # GitHub限制每页最多100条
        "page": 1
    }
    
    if since:
        params["since"] = since
    if until:
        params["until"] = until
    
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()  # 如果请求失败抛出异常
    
    return response.json()

# 使用示例
if __name__ == "__main__":
    try:
        # 公共仓库示例(不需要token)
        commits = get_github_commits(owner="adjuchas", repo="learnGit")
        
        # 私有仓库或需要更高速率限制时使用token
        # commits = get_github_commits(
        #     owner="your_username",
        #     repo="your_repo",
        #     token="your_personal_access_token",
        #     since="2023-01-01T00:00:00Z",
        #     per_page=100
        # )
        
        for commit in commits:
            print(f"Commit ID: {commit['sha']}")
            print(f"Author: {commit['commit']['author']['name']}")
            print(f"Date: {commit['commit']['author']['date']}")
            print(f"Message: {commit['commit']['message']}")
            print("-" * 50)
            
    except requests.exceptions.HTTPError as err:
        print(f"Error accessing GitHub API: {err}")
        if err.response.status_code == 403:
            print("可能达到速率限制，请尝试使用认证令牌(token)")
    except Exception as e:
        print(f"An error occurred: {e}")