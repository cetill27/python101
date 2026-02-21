# I can’t find my PR — Beginner Help

If you are new and cannot find the Pull Request (PR), this is usually because the branch is only local and has not been pushed to GitHub yet.

## What happened in this workspace

- Your roadmap file was committed locally to git history.
- A PR title/body was prepared by the automation tool.
- **But there is no GitHub remote configured in this repo yet**, so there is no live PR URL to open.

## How to publish your work and create a real PR

### 1) Create an empty GitHub repository
- Go to GitHub → New repository.
- Name it something like `python101`.
- Do not initialize with README (optional, but keeps things simple).

### 2) Connect this local repo to GitHub
Run:

```bash
git remote add origin https://github.com/<your-username>/<your-repo>.git
```

### 3) Push your branch
Current branch here is `work`. Push it:

```bash
git push -u origin work
```

### 4) Open the PR in GitHub
- GitHub will usually show a “Compare & pull request” banner.
- Click it and submit.

Or use this URL pattern directly:

```text
https://github.com/<your-username>/<your-repo>/compare/main...work
```

(If your default branch is `master` instead of `main`, replace accordingly.)

## Optional: create PR from CLI (if `gh` is installed)

```bash
gh pr create --base main --head work --title "Add 30-day Python AI/ML roadmap" --body-file PR_BODY.md
```

## Verify your roadmap file exists locally

```bash
git log --oneline -n 5
git show --name-only --oneline HEAD
```

You should see commit:

- `Add 30-day Python AI/ML roadmap with daily tasks, exercises, and book list`

And file:

- `PYTHON_AI_ML_30_DAY_ROADMAP.md`

## If you want, I can also generate:
- a ready-to-paste PR body template,
- a cleaner branch naming strategy,
- and step-by-step GitHub screenshots checklist.
