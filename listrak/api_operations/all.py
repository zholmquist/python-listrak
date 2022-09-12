from listrak.api_operations.base_operation import BaseOperation


class All(BaseOperation):
    def all(self, **params):
        resource = self.schema_name_to_resource(self.schema)
        response = self.client.get(f"{resource}").json()

        if "data" in response:
            response = response.get("data")
        else:
            print(response)

        resources = []
        for resource_data in response:
            resources.append(self.schema(**resource_data))

        return resources
