from pydantic import BaseModel


class Resource(BaseModel):

    changed_attributes = set()

    def __setattr__(self, name, value):
        if name != "changed_attributes":
            self.changed_attributes.add(name)

        super().__setattr__(name, value)
