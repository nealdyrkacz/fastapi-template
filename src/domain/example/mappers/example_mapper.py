from persistence.example.models.example_model import Example as ExampleORM
from domain.example.models.example import Example
from api.schemas.example.example import ExampleResponse

class ExampleMapper:
    @staticmethod
    def to_domain(db_model: ExampleORM) -> Example:
        return Example(
            id=db_model.id,
            name=db_model.name,
        )
    
    @staticmethod
    def to_response(domain_model: Example) -> ExampleResponse:
        # Business logic: what to expose in API
        return ExampleResponse(
            id=domain_model.id,
            name=domain_model.name
        )

