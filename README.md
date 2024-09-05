# *[build-latex-document-action](https://github.com/kostrykin/build-latex-document-action)*

Builds and publishes the PDF of a LaTeX document to a target branch.

The PDF is published to a target branch of the repository, which has the same name as the branch (or the tag) which triggered the workflow. If that PDF already exists on the target branch, it will be updated. The target branch can be published with GitHub Pages: https://kostrykin.github.io/build-latex-document-action

When triggered from pull requests, the built PDF is provided as an artifact and posted into the pull request which triggered the worklow.

For examples see:
- <https://github.com/BMCV/mobi-fs3-python-assignments/blob/current/.github/workflows/build_assignments.yml>
- <https://github.com/BMCV/mobi-fs5-python-assignments/blob/current/.github/workflows/build_assignments.yml>
- <https://github.com/BMCV/mobi-fs3-python-lecture/blob/current/.github/workflows/build_slides.yml>

---

**Example:** Create a target branch as an orphan branch:
```bash
git checkout --orphan pdf
git reset --hard
git commit --allow-empty -m "Create target branch"
git push origin pdf
```
