LibreTime uses the [black](https://github.com/psf/black) coding style for Python
and you must ensure that your code follows it. If not, the CI will fail and your
Pull Request will not be merged. Similarly, the Python import statements are
sorted with [isort](https://github.com/pycqa/isort). There is configuration
provided for [pre-commit](https://pre-commit.com/), which will ensure that code
matches the expected style and conventions when you commit changes. It is set up
by running:

```bash
sudo apt install pre-commit
pre-commit install
```

You can also run it anytime using:

```bash
pre-commit run --all-files
```