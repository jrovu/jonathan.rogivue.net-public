#!/usr/bin/env python3
# Publish MkDocs Site to AWS
# Updated: 2024-01-13 / JRO
# --------------------------
# Description:
# - Converts Markdown-formatted text & images into a static HTML website
# - Saves changes to remote repository (GitHub)
# - Publishes the website online, to Amazon AWS platform
#
# How to use it
# ./publish_site.py
#
# Development Backlog
# --------------------
# - [ ] Github users tokens
#       Info: https://github.com/settings/tokens
# - [ ] Tool accepts arguments (currently hard-coded)
#       - Site directory
# - [ ] Clears network cache (AWS Cloudfront)
# - [ ] One-click button (MacOS dock icon, runs the script)
# - [ ] Initial-setup automation (Terraform setup AWS S3, CloudFront, Certs, Route 53, etc)

# Required modules
# ------------------
import subprocess
# Subprocess Documentation: https://docs.python.org/3/library/subprocess.html


# INPUT ARGUMENTS
local_files = "/Users/jro/JRO-Sync/_Websites/Jonathan.Rogivue.net/"
s3_bucket_url = "s3://jonathan.rogivue.net-public/"
# remote_repository_url = 

mkdocs_config = local_files + "mkdocs.yml"
local_built_site = local_files + "site/"
local_repository_path = local_files
# - remote_repository = "https://github.com/jrovu/jonathan.rogivue.net-public.git"
# - domain_name



# Intro
print("\n▶ Site Publisher")
print("----------")

# Publish to remote repository
# -----------------------------
# git push origin master (?)


print("\n▶ Committing changes to Repository (git)")
print("----------")
subprocess.run(["git", "add", local_files], cwd=local_repository_path)
commit_message = "Content changes - Deployment automation"
subprocess.run(["git", "commit", "-m", commit_message], cwd=local_repository_path) 
subprocess.run(["git", "push", "origin", "master"])

# Build site using MkDocs

print("\n▶ Running MkDocs build...")
print("----------")
subprocess.run(["mkdocs", "build", "--config-file", mkdocs_config])


# Check Links

print("\n▶ Checking local files for broken links...")
print("----------")
subprocess.run(["linkchecker", local_built_site])

# Upload/Sync to File server (AWS S3)
# Documentation: https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/sync.html

print("\n▶ Upload-syncing local files to remote file server (AWS S3)")
print("----------")
subprocess.run(["aws", "s3", "sync", local_built_site, s3_bucket_url])