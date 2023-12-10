class DemoService:
    @staticmethod
    def stub_data(service_version: str):
        return {
            "messageId": 1,
            "example": {
                "message": str.format(
                    "Hello World deployed version is: v{}.", service_version
                )
            },
        }

    def return_stub_data(self, service_version: str):
        return self.stub_data(service_version)
