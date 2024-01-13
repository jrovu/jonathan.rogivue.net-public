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
# - [ ] One-click button (MacOS dock icon, runs the script)
# - [ ] Initial-setup automation (Terraform setup AWS S3, CloudFront, Certs, Route 53, etc)

# Requirements
import subprocess
# Documentation: https://docs.python.org/3/library/subprocess.html


# INPUT
# - remote_repository = (GitHub URL)
# - domain_name



# Intro
print("----------")
print("▶ Site Publisher")
print("----------")

# Publish to remote repository
# -----------------------------
# git push origin master (?)

print("----------")
print("▶ Committing changes to Repository (git)")
print("----------")
subprocess.run(["git", "add", "."])
commit_message = "Content changes - Deployment automation"
subprocess.run(["git", "commit", "-m", commit_message]) 


# Build site using MkDocs
print("----------")
print("▶ Running MkDocs build...")
print("----------")
subprocess.run(["mkdocs", "build"])

# Check Links
print("----------")
print("▶ Checking local files for broken links...")
print("----------")
subprocess.run(["linkchecker", "site/index.html"])

# Upload/Sync to File server (AWS S3)
# Documentation: https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/sync.html
print("----------")
print("▶ Upload-syncing local files to remote file server (AWS S3)")
print("----------")
subprocess.run(["aws", "s3", "sync", "site/", "s3://jonathan.rogivue.net-public"])