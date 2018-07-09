# AliceOS Docs
The documentation for AliceOS

## Requirements
You will need Python 2 and `documentation-builder` from Canonical to run the scripts necessary.

[Get documentation-builder &rsaquo;](https://snapcraft.io/documentation-builder)

## Building
If you intend to just build the `docs` folder, run the following command:
```
./serve.py build-only
```

If you plan to test locally, run the following command:
```
./serve.py build-local-test
```
The website will be available for local viewing at `localhost:8000`.

## Pushing to the repository
Ensure that the `docs` folder remains when pushing; GitHub watches this folder to use that as the site.