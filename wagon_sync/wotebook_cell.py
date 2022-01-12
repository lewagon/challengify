import re


class WotebookCell(dict):
    def __init__(self, cell):
        self.raw = cell
        for key in cell:
            setattr(self, key, cell[key])
        self._get_tags()
        self.source_text = "".join(self.source)

    def __repr__(self):
        return f'<WotebookCell {self.cell_type}>'

    def is_code(self):
        return self.cell_type == 'code'

    def clear_outputs(self, tag=None):
        if self.is_code() and (tag is None or tag in self.tags):
            self.outputs = []
        return self

    def replace_text(self, delimiter_start, delimiter_end, replace_code,
                     replace_md):
        delimiter_start = re.escape(delimiter_start)
        delimiter_end = re.escape(delimiter_end)
        if self.is_code():
            pattern = f"# {delimiter_start}(.|\n)*?(?<!# {delimiter_end})# {delimiter_end}"
            self.source_text = re.sub(pattern, replace_code, self.source_text)
        else:
            pattern = f"{delimiter_start}(.|\n)*?(?<!{delimiter_end}){delimiter_end}"
            self.source_text = re.sub(pattern, replace_md, self.source_text)
        self.text2source()
        return self

    def serialize(self):
        return {key: getattr(self, key) for key in self.raw.keys()}

    def _get_tags(self):
        if self.raw.get('metadata', False):
            self.tags = self.raw['metadata'].get('tags', [])
        else:
            self.tags = []

    def text2source(self):
        self.source = self.source_text.splitlines(keepends=True)
