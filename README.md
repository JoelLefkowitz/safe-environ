# Safe Environ

Safely integrate environment variables

### Status

| Source     | Shields                                                        |
| ---------- | -------------------------------------------------------------- |
| Project    | ![license][license] ![release][release]                        |
| Publishers | [![pypi][pypi]][pypi_link]                                     |
| Downloads  | ![pypi_downloads][pypi_downloads]                              |
| Raised     | [![issues][issues]][issues_link] [![pulls][pulls]][pulls_link] |

### Installing

To install the package from pypi:

```bash
pip install safe_environ
```

Alternatively, you can clone the repo and build the package locally.

### Docs

Additional details are available in the [full documentation](https://safe-environ.readthedocs.io/en/latest/).

To generate the documentation locally:

```bash
multi-job docs
```

### Tests

Unit tests and behaviour tests are written with the pytest framework.

To run tests:

```bash
multi-job tests
```

Additionally, an html report will be saved to the local directory.

### Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests.

### Versioning

[SemVer](http://semver.org/) is used for versioning. For a list of versions available, see the tags on this repository.

Bump2version is used to version and tag changes.
For example:

```bash
bump2version patch
```

Releases are made on every major change.

### Author

- **Joel Lefkowitz** - _Initial work_ - [Joel Lefkowitz](https://github.com/JoelLefkowitz)

See also the list of contributors who participated in this project.

### License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

### Acknowledgments

None yet!

<!--- Table links --->

[license]: https://img.shields.io/github/license/joellefkowitz/safe-environ
[release]: https://img.shields.io/github/v/tag/joellefkowitz/safe-environ
[pypi_downloads]: https://img.shields.io/pypi/dw/safe-environ
[pypi]: https://img.shields.io/pypi/v/safe-environ "PyPi"
[pypi_link]: https://pypi.org/project/safe-environ
[issues]: https://img.shields.io/github/issues/joellefkowitz/safe-environ "Issues"
[issues_link]: https://github.com/JoelLefkowitz/safe-environ/issues
[pulls]: https://img.shields.io/github/issues-pr/joellefkowitz/safe-environ "Pull requests"
[pulls_link]: https://github.com/JoelLefkowitz/safe-environ/pulls
