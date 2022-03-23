
# visual tests

``` bash
pytest -s tests/unit/base
pytest -s tests/unit/base/test_code_replacement.py
pytest -s tests/unit/base/test_code_suppression_indented.py
pytest -s tests/unit/base/test_code_suppression_unindented.py

pytest -s tests/unit/run
pytest -s tests/unit/run/test_tags.py
pytest -s tests/unit/run/test_verbs.py
pytest -s tests/unit/run/test_decorator.py
pytest -s tests/unit/run/test_language_decorators.py
pytest -s tests/unit/run/test_challengify.py

pytest -s tests/unit/iterate
pytest -s tests/unit/iterate/test_challenge_version_iterator.py

pytest -s tests/functional
pytest -s tests/functional/test_code_python.py
pytest -s tests/functional/test_code_ruby.py
pytest -s tests/functional/test_code_shell.py
pytest -s tests/functional/test_code_text.py
pytest -s tests/functional/test_code_html.py
pytest -s tests/functional/test_code_css.py
pytest -s tests/functional/test_code_js.py
pytest -s tests/functional/test_code_rails.py
```
