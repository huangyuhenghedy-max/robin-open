# PyPI Trusted Publisher Setup

The repository contains a publish workflow at `.github/workflows/publish.yml`. It uses PyPI Trusted Publishing, so no PyPI token belongs in the repository or local project files.

## One-time PyPI setup

From the project owner's PyPI account:

1. Open `https://pypi.org/manage/account/publishing/`.
2. Add a pending publisher with:
   - Owner: `huangyuhenghedy-max`
   - Repository: `robin-open`
   - Workflow: `publish.yml`
   - Environment: `pypi`
3. Create a GitHub environment named `pypi` under repository Settings → Environments.
4. Publish a new GitHub Release. The workflow builds the wheel and source archive, runs `twine check`, and publishes through OIDC.

Until this one-time setup is complete, GitHub package verification can pass but PyPI publication will remain intentionally blocked.
