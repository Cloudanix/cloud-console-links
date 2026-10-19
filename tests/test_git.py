import pytest

from cloudconsolelink.clouds.git import LINKS, GitLinker

git = GitLinker()


@pytest.mark.parametrize(
    "provider,resource_name,params,expected",
    [
        ("github", "organization", {"owner": "acme"}, "https://github.com/acme"),
        ("github", "repository", {"owner": "acme", "repo": "api"}, "https://github.com/acme/api"),
        ("github", "branch", {"owner": "acme", "repo": "api", "branch": "main"},
         "https://github.com/acme/api/tree/main"),
        ("github", "user", {"login": "octocat"}, "https://github.com/octocat"),
        ("github", "team", {"owner": "acme", "team": "platform"}, "https://github.com/orgs/acme/teams/platform"),
        ("gitlab", "group", {"group_path": "acme/infra"}, "https://gitlab.com/acme/infra"),
        ("gitlab", "project", {"project_path": "acme/infra/api"}, "https://gitlab.com/acme/infra/api"),
        ("gitlab", "branch", {"project_path": "acme/api", "branch": "main"},
         "https://gitlab.com/acme/api/-/tree/main"),
        ("gitlab", "member", {"username": "jdoe"}, "https://gitlab.com/jdoe"),
        ("bitbucket", "workspace", {"workspace": "acme"}, "https://bitbucket.org/acme"),
        ("bitbucket", "project", {"workspace": "acme", "project_key": "PRJ"},
         "https://bitbucket.org/acme/workspace/projects/PRJ"),
        ("bitbucket", "repository", {"workspace": "acme", "repo": "api"}, "https://bitbucket.org/acme/api"),
        ("bitbucket", "branch", {"workspace": "acme", "repo": "api", "branch": "main"},
         "https://bitbucket.org/acme/api/src/main"),
        ("bitbucket", "member", {"workspace": "acme"},
         "https://bitbucket.org/acme/workspace/settings/user-directory"),
        ("azuredevops", "organization", {"organization": "acme"}, "https://dev.azure.com/acme"),
        ("azuredevops", "project", {"organization": "acme", "project": "web"}, "https://dev.azure.com/acme/web"),
        ("azuredevops", "repository", {"organization": "acme", "project": "web", "repo": "api"},
         "https://dev.azure.com/acme/web/_git/api"),
        ("azuredevops", "branch", {"organization": "acme", "project": "web", "repo": "api", "branch": "main"},
         "https://dev.azure.com/acme/web/_git/api?version=GBmain"),
        ("azuredevops", "user", {"organization": "acme"}, "https://dev.azure.com/acme/_settings/users"),
    ],
)
def test_links(provider, resource_name, params, expected):
    assert git.get_console_link(provider, resource_name, **params) == expected


def test_every_template_is_tested():
    tested = {
        ("github", r) for r in ("organization", "repository", "branch", "user", "team")
    } | {
        ("gitlab", r) for r in ("group", "project", "branch", "member")
    } | {
        ("bitbucket", r) for r in ("workspace", "project", "repository", "branch", "member")
    } | {
        ("azuredevops", r) for r in ("organization", "project", "repository", "branch", "user")
    }
    assert {(p, r) for p, links in LINKS.items() for r in links} == tested


def test_base_url_override_github_enterprise():
    link = git.get_console_link("github", "repository", base_url="https://ghe.acme.io/", owner="acme", repo="api")
    assert link == "https://ghe.acme.io/acme/api"


def test_base_url_override_self_managed_gitlab():
    link = git.get_console_link("gitlab", "project", base_url="https://git.acme.io", project_path="acme/api")
    assert link == "https://git.acme.io/acme/api"


def test_branch_with_slash_stays_a_path():
    link = git.get_console_link("github", "branch", owner="acme", repo="api", branch="feature/x y")
    assert link == "https://github.com/acme/api/tree/feature/x%20y"


def test_azuredevops_branch_is_fully_encoded_in_query():
    link = git.get_console_link("azuredevops", "branch", organization="acme", project="web", repo="api",
                                branch="feature/x")
    assert link == "https://dev.azure.com/acme/web/_git/api?version=GBfeature%2Fx"


def test_space_in_name_is_encoded():
    link = git.get_console_link("azuredevops", "project", organization="acme", project="My Project")
    assert link == "https://dev.azure.com/acme/My%20Project"


def test_slash_in_non_path_param_is_encoded():
    link = git.get_console_link("github", "repository", owner="acme", repo="a/b")
    assert link == "https://github.com/acme/a%2Fb"


def test_unknown_provider():
    with pytest.raises(ValueError, match="Unknown git provider"):
        git.get_console_link("svn", "repository", repo="api")


def test_unknown_resource_name():
    with pytest.raises(ValueError, match="Unknown github resource_name"):
        git.get_console_link("github", "pull_request", owner="acme")


def test_missing_param():
    with pytest.raises(ValueError, match="'repo'"):
        git.get_console_link("github", "repository", owner="acme")


def test_empty_param():
    with pytest.raises(ValueError, match="'owner'"):
        git.get_console_link("github", "organization", owner="")
