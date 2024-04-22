# Ansible-Role: acr-ansible-hostname

AIT-CyberRange: Downloads folders from gitlab asyncronously (fire and forget).

**IMPORTANT:** Files and folders must be pushed before executing this role.

> This role currently only works with gitlab. Support for github will follow.


## Requirements

- Debian or Ubuntu 
- Gitlab

## Role Variables

```yaml
# Path to the data to be uploaded relative to the repo's root
agd_relative_src_path: '/path/to/data/relative/to/project'
# Path to the repo base on local machine
agd_absolute_project_path: '/basepath/to/project/'
# GitLab private access token if repo is private
agd_git_token: ''
# Destination folder on remote machine
agd_data_dest: '/tmp/'
# Owner of files on remote machine
agd_owner: 'root'
# Group of files on remote machine
agd_group: 'root'
# Mode of files on remote machine
agd_mode: 755
# Time for process to finish
agd_timeout: 7200
```

## Example Playbook

```yaml
- hosts: servers
  tasks:
    - name: Loop through shares
      tags: [skip_ansible_lint]
      ansible.builtin.include_role:
        name: async_git_download
      vars:
        agd_absolute_project_path: "{{ local_ansible_dir }}"
        agd_relative_src_path: /data/files/smb_shares/{{ samba_share.name }}
        agd_git_token: "{{ gitlab_pat }}"
        agd_data_dest: /srv/shares/{{ samba_share.name }}
        agd_owner: root
        agd_group: "{{ samba_share.group }}"
        agd_mode: 774
      loop: "{{ samba_shares }}"
      loop_control:
        loop_var: samba_share
```

## License

GPL-3.0

## Author

- Lenhard Reuter