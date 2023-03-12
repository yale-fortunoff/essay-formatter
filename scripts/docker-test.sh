
pip install --upgrade pip && \
pip install -r requirements-dev.txt && \
tox &&
echo Completed run using $(python --version)