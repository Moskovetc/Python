class Pars:
    pars = {}

    def __init__(self, pars_names):
        self._pars_names = self._add(pars_names)

    @staticmethod
    def _remove_eol(item):
        try:
            if '\n' in item:
                item = item[0:-1]
        except:
            pass
        return item

    def _add(self, parameters_list):
        items = []
        for item in parameters_list:
            item = self._remove_eol(item)
            items.append(item)
        return items

    def add_items(self, items):
        pars_items = self._add(items)
        self.pars = dict(zip(self._pars_names, pars_items))


