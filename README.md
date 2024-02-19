# *[build-latex-document-action](https://github.com/kostrykin/build-latex-document-action)*

Builds and publishes the PDF of a LaTeX document.

The PDF is published as the attachment of a release, which has the same name as the branch (or the tag) which triggered the workflow. If that release already exists, it will be updated. Documents built from `future/**` branches or tags are only *drafted* for release.

When triggered from pull requests, the built PDF is provided as an artifact and posted into the pull request which triggered the worklow.

For examples see:
- <https://github.com/BMCV/mobi-fs3-python-assignments/blob/current/.github/workflows/build_assignments.yml>
- <https://github.com/BMCV/mobi-fs5-python-assignments/blob/current/.github/workflows/build_assignments.yml>
- <https://github.com/BMCV/mobi-fs3-python-lecture/blob/current/.github/workflows/build_slides.yml>
