from project.services.base_service import BaseService


class SecondaryService(BaseService):
    def __init__(self, name: str):
        super().__init__(name, 15)

    def details(self):
        robots = 'none' if len(self.robots) == 0 else ' '.join([str(r.name) for r in self.robots])

        return f"{self.name} Secondary Service:\n" + \
               f'Robots: {robots}'