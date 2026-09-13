# 26.6.13-codex1

Personal sandbox repository for hands-on experiments with coding-agent workflows.

Created on 2026-06-13. Contents change as experiments come and go — nothing here is a released project.

## Verify the sandbox contract

Run the standard-library test suite to check that the README still points to the
experiment template and that the template keeps every section needed for a
reproducible note:

```bash
python -m unittest discover -s tests -v
```

## Reproducible experiment notes

For each experiment, record the goal, constraints, reproduction steps, expected and observed results, focused verification, and cleanup work. Start with the [experiment note template](docs/experiment-template.md) so results remain useful after the sandbox state changes.
