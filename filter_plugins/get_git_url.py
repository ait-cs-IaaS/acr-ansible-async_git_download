import subprocess
import os


class FilterModule(object):
    def filters(self):
        return {"git_download_url": self.git_download_url}

    def git_download_url(
        self, relative_local_path, absolute_project_path, git_token=""
    ):

        # Change directory to the project path
        os.chdir(absolute_project_path)

        # Run git command to get URL
        git_url = subprocess.run(
            ["git", "remote", "get-url", "origin"], capture_output=True, text=True
        ).stdout.strip()

        # Get relative path
        relative_path = subprocess.run(
            ["git", "rev-parse", "--show-prefix"], capture_output=True, text=True
        ).stdout.strip()

        # Get current branch
        current_branch = subprocess.run(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"], capture_output=True, text=True
        ).stdout.strip()

        git_url = git_url.split("@")[-1].split(".git")[0].replace(":", "/")

        # Get repository name
        repo_name = git_url.split("/")[-1]

        # Restore working directory
        os.chdir(os.getcwd())

        rel_path = f"{relative_path}{relative_local_path}"

        # Construct URL
        stripped_git_url = f"https://{git_url}/-/archive/{current_branch}/{repo_name}-{current_branch}.tar.gz?path=/{rel_path}"

        # Append git token if provided
        if git_token:
            stripped_git_url += f"\&private_token={git_token}"

        nested_length = len(rel_path.split("/"))
        return {"url": stripped_git_url, "length": nested_length}
