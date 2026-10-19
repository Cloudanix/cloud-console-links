import logging
import string
import urllib.parse
from typing import Dict
from typing import Optional

logger = logging.getLogger(__name__)

DEFAULT_BASE_URLS: Dict[str, str] = {
    "github": "https://github.com",
    "gitlab": "https://gitlab.com",
    "bitbucket": "https://bitbucket.org",
    "azuredevops": "https://dev.azure.com",
}

# A "{name_q}" field is a query-string value: the "name" param, fully encoded (slashes too).
LINKS: Dict[str, Dict[str, str]] = {
    "github": {
        "organization": "{base}/{owner}",
        "repository": "{base}/{owner}/{repo}",
        "branch": "{base}/{owner}/{repo}/tree/{branch}",
        "user": "{base}/{login}",
        "team": "{base}/orgs/{owner}/teams/{team}",
    },
    "gitlab": {
        "group": "{base}/{group_path}",
        "project": "{base}/{project_path}",
        "branch": "{base}/{project_path}/-/tree/{branch}",
        "member": "{base}/{username}",
    },
    "bitbucket": {
        "workspace": "{base}/{workspace}",
        "project": "{base}/{workspace}/workspace/projects/{project_key}",
        "repository": "{base}/{workspace}/{repo}",
        "branch": "{base}/{workspace}/{repo}/src/{branch}",
        "member": "{base}/{workspace}/workspace/settings/user-directory",
    },
    "azuredevops": {
        "organization": "{base}/{organization}",
        "project": "{base}/{organization}/{project}",
        "repository": "{base}/{organization}/{project}/_git/{repo}",
        "branch": "{base}/{organization}/{project}/_git/{repo}?version=GB{branch_q}",
        "user": "{base}/{organization}/_settings/users",
    },
}

# Params whose value is itself a path (GitLab "group/subgroup", branch "feature/x"); "/" stays literal.
PATH_PARAMS = {"group_path", "project_path", "branch"}

QUERY_SUFFIX = "_q"


def _encode(field: str, value: str) -> str:
    if field.endswith(QUERY_SUFFIX):
        return urllib.parse.quote(value, safe="")
    return urllib.parse.quote(value, safe="/" if field in PATH_PARAMS else "")


class GitLinker:
    def get_console_link(
        self,
        provider: str,
        resource_name: str,
        base_url: Optional[str] = None,
        **params: str,
    ) -> str:
        """Build the web URL of a git-provider entity (GitHub, GitLab, Bitbucket, Azure DevOps).

        Args:
            provider: "github", "gitlab", "bitbucket" or "azuredevops".
            resource_name: entity type within the provider, e.g. "repository", "branch" (see LINKS).
            base_url: host override for GitHub Enterprise, self-managed GitLab, etc.
                Defaults to the provider's public host; a trailing "/" is dropped.
            **params: identifiers the template needs, e.g. owner="acme", repo="api", branch="main".

        Returns:
            str: the URL, with each param URL-encoded.

        Raises:
            ValueError: unknown provider or resource_name, or a required param is missing/empty.

        Example:
            >>> GitLinker().get_console_link("github", "branch", owner="acme", repo="api", branch="main")
            'https://github.com/acme/api/tree/main'
        """
        if provider not in LINKS:
            raise ValueError(f"Unknown git provider {provider!r}")
        template = LINKS[provider].get(resource_name)
        if template is None:
            raise ValueError(f"Unknown {provider} resource_name {resource_name!r}")

        values = {"base": (base_url or DEFAULT_BASE_URLS[provider]).rstrip("/")}
        for _, field, _, _ in string.Formatter().parse(template):
            if not field or field == "base":
                continue
            name = (
                field[: -len(QUERY_SUFFIX)] if field.endswith(QUERY_SUFFIX) else field
            )
            if not params.get(name):
                raise ValueError(f"{provider} {resource_name} link requires {name!r}")
            values[field] = _encode(field, str(params[name]))

        logger.debug(f"Building {provider} {resource_name} link")
        return template.format(**values)


__all__ = ["DEFAULT_BASE_URLS", "GitLinker", "LINKS"]
