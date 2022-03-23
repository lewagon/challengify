default: pylint pytest

# $DELETE_BEGIN
pylint:
	find . -iname "*.py" -not -path "./tests/test_*" | xargs -n1 -I {}  pylint --output-format=colorized {}; true
# $DELETE_END

# $CHALLENGIFY_BEGIN
pytest:
	PYTHONDONTWRITEBYTECODE=1 pytest -v --color=yes
# $CHALLENGIFY_END
