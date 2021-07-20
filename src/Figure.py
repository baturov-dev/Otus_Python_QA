class Figure:

    @property
    def area(self):
        raise NotImplementedError

    @property
    def perimeter(self):
        raise NotImplementedError


    def add_area(self, other_figure):
        if not isinstance(other_figure, Figure):
            raise ValueError('Should be Figure!')
        else:
            return self.area + other_figure.area