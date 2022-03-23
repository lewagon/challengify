
# visual tests

``` bash
pytest -s tests/unit/test_tags.py
pytest -s tests/unit/test_verbs.py
pytest -s tests/unit/test_decorator.py
pytest -s tests/unit/test_language_decorators.py
pytest -s tests/unit/test_challengify.py

pytest -s tests/test_code_python.py
pytest -s tests/test_code_ruby.py
pytest -s tests/test_code_shell.py
pytest -s tests/test_code_text.py

pytest -s tests/test_code_html.py
pytest -s tests/test_code_css.py

pytest -s tests/test_code_js.py
pytest -s tests/test_code_rails.py

pytest -s tests/unit/test_challenge_versions.py
pytest -s tests/unit/test_code_replacement.py
pytest -s tests/unit/test_code_suppression_indented.py
pytest -s tests/unit/test_code_suppression_unindented.py
```
