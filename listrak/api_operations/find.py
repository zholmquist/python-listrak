from listrak.api_operations.base_operation import BaseOperation


class Find(BaseOperation):
    def find(self, **params):

        resource = self.schema_name_to_resource(self.schema)
        if not "id" in params:
            return None

        response = self.client.get(f"{resource}/{params['id']}", **params).json()

        if "data" in response:
            response = response.get("data")
        else:
            return None

        return self.schema(**response)
