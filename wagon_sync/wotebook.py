import os
import json
import copy
from wagon_sync.wotebook_cell import WotebookCell
from wagon_common.helpers.notebook import read_notebook, save_notebook


class Wotebook:
    def __init__(self, source):
        self.raw = read_notebook(source)
        self.processed = copy.deepcopy(self.raw)
        self.cells = [WotebookCell(cell) for cell in self.raw['cells']]

    def clear_outputs(self, tag=None):
        self.cells = [cell.clear_outputs(tag) for cell in self.cells]
        self.processed['cells'] = self.cells
        return self

    def remove_cells(self, tag):
        self.cells = [cell for cell in self.cells if tag not in cell.tags]
        self.processed['cells'] = self.cells
        return self

    def replace_text(self,
                     delimiter_start,
                     delimiter_end,
                     replace_code="",
                     replace_md=""):
        self.cells = [
            cell.replace_text(delimiter_start, delimiter_end, replace_code,
                              replace_md) for cell in self.cells
        ]
        self.processed['cells'] = self.cells
        return self

    def save(self, destination):
        self.processed['cells'] = [cell.serialize() for cell in self.cells]
        self.processed['metadata'].pop('celltoolbar', None)
        save_notebook(self.processed, destination)


if __name__ == "__main__":
    source = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'tests',
                          'test_notebook.ipynb')
    wtbk = Wotebook(source)
    print('A cell')
    print(wtbk.cells[-1].raw)
    print()
    print('Code Cells outputs')
    for cell in wtbk.cells:
        if cell.is_code():
            print(cell.outputs)
    print()
    print('Clear only tagged cells outputs')
    wtbk.clear_outputs(tag='clear_output')
    for cell in wtbk.cells:
        if cell.is_code():
            print(cell.outputs)
    print()
    print('Processed')
    print(wtbk.processed)
    print()
    print('Remove cells')
    print('before', len(wtbk.cells))
    wtbk.remove_cells(tag='delete')
    print('after', len(wtbk.cells))
    print(wtbk.processed)
    print()
    print('Cell content')
    for cell in wtbk.cells:
        print(cell.raw)
    print()
    print('Challengify')
    wtbk.replace_text('$CHALLENGIFY_BEGIN',
                      '$CHALLENGIFY_END',
                      replace_code="pass",
                      replace_md="> YOUR ANSWER HERE")
    wtbk.replace_text('$DELETE_BEGIN',
                      '$DELETE_END',
                      replace_code="",
                      replace_md="")
    for cell in wtbk.cells:
        print(cell.source_text)
    wtbk.save(
        os.path.join(os.path.dirname(os.path.dirname(__file__)), 'tests',
                     'test_notebook_processed.ipynb'))
