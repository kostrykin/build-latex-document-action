# *[build-latex-document-action](https://github.com/kostrykin/build-latex-document-action)*

Builds and publishes the PDF of a LaTeX document to a target branch.

The PDF is published to a target branch of the repository, which has the same name as the branch (or the tag) that triggered the workflow. If that PDF already exists on the target branch, it will be updated. The target branch can be published with GitHub Pages: https://kostrykin.github.io/build-latex-document-action

When triggered from pull requests, the built PDF is provided as an artifact and posted into the pull request that triggered the worklow.

## Installation

### Create the `build.yml` workflow

This workflow builds the PDF on `push` and `pull_request` triggers. For `pull_request` triggers, it runs within the context of the base branch and repository (the branch that is being merged, potentially a fork). The built PDF is uploaded as an artifact by the action. For `push` triggers, the PDF is published to the target branch, that is `pdf` by default. Example:

```yml
name: Build document

on:
  push:
    paths:
      - 'sources/**'
      - '.github/workflows/build.yml'
  pull_request:
    branches:
      - 'current'
      - 'future/**'

jobs:
  build:
    runs-on: ubuntu-latest
    if: ${{
        github.event_name == 'pull_request' ||
        github.ref_name == 'current' ||
        startsWith(github.ref_name, 'future/')
      }}
    permissions:
      contents: write
    steps:

      - name: Initialize
        uses: actions/checkout@v4

      - uses: kostrykin/build-latex-document-action@v2.2.0
        with:
          working_directory: sources
          document_filename: document.pdf
          sources: |
            part1.tex
            part2.tex
```

### Create the `post-comment.yml` workflow

This workflow is triggered when a `build.yml` workflow is finished. It is only required for `pull_request` triggers, since it is responsible for posting the comment into the pull request that triggered the `build.yml` workflow. To be able to do this across forks, this workflow needs to run within the context of the target branch of the pull request. Example:

```yml
name: Post pull request comment

on:
  workflow_run:
    workflows: [Build document]
    types: [completed]

jobs:
  post_pr_comment:
    runs-on: ubuntu-latest
    permissions:
      pull-requests: write
    if: ${{ github.event.workflow_run.conclusion == 'success' }}
    steps:

      - uses: kostrykin/post-gh-comment-from-artifact@v1.0.0
```

### Create a target branch as an orphan branch

```bash
git checkout --orphan pdf
git reset --hard
git commit --allow-empty -m "Create target branch"
git push origin pdf
```

## Examples

For examples see:
- <https://github.com/BMCV/mobi-fs3-python-assignments/blob/current/.github/workflows/build_assignments.yml>
- <https://github.com/BMCV/mobi-fs5-python-assignments/blob/current/.github/workflows/build_assignments.yml>
- <https://github.com/BMCV/mobi-fs3-python-lecture/blob/current/.github/workflows/build_slides.yml>
