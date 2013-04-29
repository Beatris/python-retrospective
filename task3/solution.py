class Person:

    def __init__(self, name, birth_year, gender,
    mother=None, father=None):
        self.name = name
        self.birth_year = birth_year
        self.gender = gender
        self.mother = mother
        self.father = father
        self._children = set()

        for parent in [self.mother, self.father]:
            if parent is not None:
                self.add_parent(parent)

    def add_parent(self, parent):
        parent.add_child(self)

    def add_child(self, child):
        if (child.birth_year - self.birth_year) >= 18 \
        and child not in self._children:
            self._children.add(child)
            if self.gender == "F":
                child.mother = self
            elif self.gender == "M":
                child.father = self

    def children(self, gender=None):
        return [filter(lambda child:
        child.gender == gender or gender is None, self._children)]

    def get_brothers(self):
        brothers = []
        if self.mother is not None:
            for son in self.mother.children(gender='M'):
                if son not in brothers:
                    brothers += self.mother.children(gender="M")
        if self.father is not None:
            for son in self.father.children(gender='M'):
                if son not in brothers:
                    brothers += self.father.children(gender="M")
        if self in brothers:
            brothers.remove(self)
        return brothers

    def get_sisters(self):
        sisters = []
        if self.mother is not None:
            for daughter in self.mother.children(gender='F'):
                if daughter not in sisters:
                    sisters += self.mother.children(gender="F")
        if self.father is not None:
            for daughter in self.father.children(gender='F'):
                if daughter not in sisters:
                    sisters += self.father.children(gender="F")
        if self in sisters:
            sisters.remove(self)
        return sisters

    def is_direct_successor(self, person):
        return self in person.children() or person in self.children()