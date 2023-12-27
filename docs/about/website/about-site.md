---
title: "About this site"
tags: [draft, scratch-notes, goals, to-do]
published: 2023-12-27
updated: 2023-12-27
---

# About this site / Vision

## Vision / Progress

- ✔  This is a"Lo-fi" website - Mostly text files in a folder, along with images, and other media
- Philosophy: 
  - https://squidfunk.github.io/mkdocs-material/philosophy/
- 🔲 All pages print nicely - viewable & exportable as HTML, PDF, Ebook
- 🔲 Content & Publishing System designed to last 20+ years
  - Minimal dependency on external services
  - open-source tools, content, format
- ✔ Easy to author (Typora + Markdown)
- ✔ Can edit site using Laptop (MacBook) 
- 🔲 Can edit site using Phone (iPhone)
- ✔ Can publish site from Laptop
- 🔲 Can publish site from Phone
  - WorkingCopy?
- 🔲 All content is versioned, and mistakes can be easily rolled-back (Git, GitHub)
- 🔲 All content is regularly backed up
  - Locally (MacOS TimeMachine)
  - External storage (2 TB, USB-C drive)
  - Network Storage (Synology NAS)
  - Remote Storage (AWS S3, AWS Glacier)
- Media files (images, music, video, etc) are grouped with content.
- Automatically Format Markdown
- Durable for 10+ years
- Automatically checks for broken links before publishing
  - [LinkChecker](https://pypi.org/project/LinkChecker/)



## Tech Stack

- Content format: Markdown-formatted text and media files, in folders
  - Text format: [Markdown](https://en.wikipedia.org/wiki/Markdown)
- Hosting: 
  - Domain name: NameCheap
  - File Storage: Amazon AWS S3
  - Content caching & delivery: Amazon AWS CloudFront
- Content management system: 
  - Text editor: [Typora](https://typora.io/) - Markdown text editor for MacOS
  - Website generator: MkDocs Material
  - Repository: GitHub?
- Web Publishing: 
  - Graphical File upload tool: 
    - Cyberduck
  - Terminal file upload tool:
    - Rsync?
    - To Research: AWS CLI sync
  - Clear cache
- PDF publishing
  - Print-ready HTML stylesheet
  - Pandoc



## Processes

### Create Content
- On MacBook, Open Typora.app
- Drag ~/Websites/(Sitename) folder into Typora
- Pull down latest changes from Content Repository
- Check out TO-WRITE list
- Prioritize the list, and start writing!



### Publish the site

- Terminal Commands
  
- Convert Markdown to HTML
- Clear cache



## Initial Setup

### Install MkDocs

https://squidfunk.github.io/mkdocs-material/getting-started/

```
pip install mkdocs-material
```



### Build initial site

https://squidfunk.github.io/mkdocs-material/creating-your-site/

```zsh
mkdocs new .
```



### Content Versioning & Repository

Enable content versioning (git),  remote content repository (GitHub).

- Initialize content versioning in top level directory
  - `git init`
- Commit changes & publish to remote repository



### Content



## Setup Navigation



## Setup Theme

- Change colors
  - Extra CSS: https://squidfunk.github.io/mkdocs-material/customization/#additional-css

- Change fonts

- Add logo
  - https://squidfunk.github.io/mkdocs-material/setup/changing-the-logo-and-icons/


## Setup Blog

https://squidfunk.github.io/mkdocs-material/setup/setting-up-a-blog/



## Setup Plugins

- Tabs
- Tags - https://squidfunk.github.io/mkdocs-material/setup/setting-up-tags/







## Hosting setup (AWS)

### Setup AWS S3 bucket

- Create bucket
- Set permissions for bucket

### Setup AWS CloudFront

- Create certificates for HTTPS
- Setup caching



## Writing & Publishing Flow

- Open Finder, browse to Websites folder
- Drag a Website folder into the Typora app.
- Turn on MkDocs server, in order to preview site content
- Add / edit content.
- Automatically Format Markdown
- Commit to local & remote content repository.
- Run MkDocs to build the HTML site
- Link checker (checks for 404 errors)
- Copy / rsync / aws sync the site to the AWS S3 bucket
- Invalidate the cache, so content updates are available



## Resources

- MkDocs Tutorial - https://www.youtube.com/watch?v=Q-YA_dA8C20

## Appendix

- Publishing automation - https://squidfunk.github.io/mkdocs-material/publishing-your-site/

### Backups

- Use a remote content repository to always copy content to the cloud
- On your local computer, use an automated backup program (like Apple TimeMachine) to back up your home folder to an external hard drive.