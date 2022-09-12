class BaseOperation(object):
    def schema_name_to_resource(self, schema):
        return schema.__name__.lower()  # self.pluralize(schema.__name__.lower())
