from fastapi import (
    APIRouter,
    HTTPException,
)

from src.ai_service.ai_services import (
    AIService,
)
from src.services.rule_classifier import (
    RuleClassifier,
)


router = APIRouter()


from src.services.keyword_classifier import (
    KeywordClassifier,
)
classifier = KeywordClassifier()


ai_service = AIService(
    classifier
)


@router.get("/")
def root():

    return {
        "message": "AI Service is running",
        "version": "1.0.0",
    }


@router.post("/classify")
def classify(
    text: str,
):

    try:

        return ai_service.classify(
            text
        )

    except ValueError as exc:

        raise HTTPException(
            status_code=400,
            detail=str(exc),
        )