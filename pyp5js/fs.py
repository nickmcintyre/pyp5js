from pathlib import Path
from cprint import cprint


class SketchFiles():
    TARGET_NAME = 'target'
    STATIC_NAME = 'static'

    def __init__(self, sketch_dir, sketch_name, check_sketch_dir=True):
        self._sketch_dir = sketch_dir or ''
        self.sketch_name = sketch_name
        self.check_sketch_dir = check_sketch_dir
        self.from_lib = LibFiles()

    def can_create_sketch(self):
        return not self.sketch_dir.exists()

    def check_sketch_exists(self):
        return self.sketch_py.exists()

    @property
    def sketch_dir(self):
        sketch_dir = Path(self._sketch_dir)

        if not self._sketch_dir:
            return sketch_dir.joinpath(f'{self.sketch_name}')

        if self.check_sketch_dir and not sketch_dir.exists():
            cprint.err(f"The directory {sketch_dir} does not exists.", interrupt=True)

        return sketch_dir

    @property
    def static_dir(self):
        return self.sketch_dir.joinpath(self.STATIC_NAME)

    @property
    def index_html(self):
        return self.sketch_dir.joinpath('index.html')

    @property
    def p5js(self):
        return self.static_dir.joinpath('p5.js')

    @property
    def p5_dom_js(self):
        return self.static_dir.joinpath('p5.dom.js')

    @property
    def target_sketch(self):
        return self.sketch_dir.joinpath("target_sketch.py")

    @property
    def sketch_py(self):
        py_file = self.sketch_dir.joinpath(f'{self.sketch_name}.py')

        if self.check_sketch_dir and not py_file.exists():
            cwd_py_file = Path.cwd().joinpath(f"{self.sketch_name}.py")
            if not cwd_py_file.exists():
                cprint.warn(f"Couldn't find the sketch.")
                cprint.err(f"Neither the file {py_file} or {cwd_py_file} exist.", interrupt=True)

            py_file = cwd_py_file
            self._sketch_dir = py_file.parent

        return py_file

    @property
    def target_dir(self):
        return self.sketch_dir.joinpath(self.TARGET_NAME)


class LibFiles():

    def __init__(self):
        self.install = Path(__file__).parent

    @property
    def templates_dir(self):
        return self.install.joinpath('templates')

    @property
    def assets_dir(self):
        return self.install.joinpath('assets')

    @property
    def static_dir(self):
        return self.install.joinpath('static')

    @property
    def pytop5js(self):
        return self.install.joinpath('pyp5js.py')

    @property
    def base_sketch(self):
        return self.templates_dir.joinpath('base_sketch.py.template')

    @property
    def pytop5js_template(self):
        return self.templates_dir.joinpath('pyp5js.py.template')

    @property
    def target_sketch_template(self):
        return self.templates_dir.joinpath('target_sketch.py.template')

    @property
    def index_html(self):
        return self.templates_dir.joinpath('index.html')

    @property
    def p5js(self):
        return self.static_dir.joinpath('p5', 'p5.min.js')

    @property
    def p5_dom_js(self):
        return self.static_dir.joinpath('p5', 'addons', 'p5.dom.min.js')

    @property
    def p5_yml(self):
        return self.assets_dir.joinpath('p5_reference.yml')
