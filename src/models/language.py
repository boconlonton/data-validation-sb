class Language:
    def __init__(self, code, vietnamese, english, **kwargs):
        self.code = code
        self.vn = vietnamese
        self.eng = english

    @property
    def eng(self):
        return self._eng

    @eng.setter
    def eng(self, value):
        self._eng = value
        self._key = value

    @property
    def key(self):
        return self._key

    def __repr__(self):
        return f'Language(key={self.key},eng={self.eng},vn={self.vn})'
