# Git discovery in temporary test directories

A directory without its own `.git` directory can still be inside a Git working
tree. Git searches its parents when discovering a repository. A temporary fixture
created beneath a checkout may therefore inherit that checkout, even when a test
expects a non-repository directory.

## Observed failure

During a Windows test run, temporary fixtures were placed beneath the surrounding
workspace. Tests expecting Git commands to reject a non-repository directory
instead found the workspace repository. Related file-discovery tests also returned
unexpected results. The location of the temporary fixtures was the relevant
constraint.

## Establish an explicit boundary

Use a temporary root outside any repository, or set `GIT_CEILING_DIRECTORIES` to
the absolute temporary root in the environment of the test process. Put fixtures
in child directories of that root. Keep the setting process-scoped so it does not
change normal Git behavior in later shells.

Git documents that the ceiling does not exclude the current working directory and
does not override an explicit `GIT_DIR`. Therefore, a fixture with its own `.git`
directory should remain a repository; a child fixture without one should not
inherit a repository above the ceiling.

Before running tests, verify both cases:

- In a non-repository child fixture, `git rev-parse --is-inside-work-tree` must
  exit nonzero.
- In the actual checkout, the same command must still succeed and print `true`.

## Record the result

An experiment note should include the fixture root, the process-scoped environment
setting, the two discovery checks, and the tests rerun. In the observed case, the
affected test packages passed after establishing the boundary, without changing
or skipping their assertions. Keep this separate from any source-code fix.

Reference: [Git environment variables: GIT_CEILING_DIRECTORIES](https://git-scm.com/docs/git).
