# To Build
- Bump up version at `setup.py`
- Install dependencies by `pip install -r dev-requirement.txt`
- Build the package `python -m build`
- Test API call by installing at different project  `pip install YOUR_PACKAGE_NAME.whl`
- Upload to pypi.org by `twine upload dist/*`