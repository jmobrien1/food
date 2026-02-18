from fastapi import HTTPException


class PlanGenerationError(HTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=500, detail=f"Plan generation failed: {detail}")


class IngredientNotFoundError(HTTPException):
    def __init__(self, name: str):
        super().__init__(status_code=404, detail=f"Ingredient not found: {name}")


class LLMServiceError(HTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=502, detail=f"LLM service error: {detail}")


class InvalidAuditRequestError(HTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=422, detail=detail)
