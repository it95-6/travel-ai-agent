from backend.app.db.repositories.restaurant_repository import RestaurantRepository
from backend.app.schemas.chat import ChatRequest, ChatResponse, RestaurantCandidate

AREA_CANDIDATES = ("渋谷", "新宿", "銀座", "浅草", "築地", "表参道")
CATEGORY_CANDIDATES = ("和食", "洋食", "海鮮", "カフェ", "焼肉", "寿司")
BUDGET_CANDIDATES = {
    "安め": ["1000-2000円", "1500-2500円", "2000-3000円"],
    "高め": ["3000-4000円", "8000-12000円"],
}


def _extract_from_candidates(message: str, candidates: tuple[str, ...]) -> str | None:
    for candidate in candidates:
        if candidate in message:
            return candidate
    return None


def _extract_area(message: str) -> str | None:
    return _extract_from_candidates(message, AREA_CANDIDATES)


def _extract_category(message: str) -> str | None:
    return _extract_from_candidates(message, CATEGORY_CANDIDATES)


def _extract_budget(message: str) -> tuple[str | None, list[str] | None]:
    for label, allowed_budgets in BUDGET_CANDIDATES.items():
        if label in message:
            return label, allowed_budgets
    return None, None


def _build_reply(
    *,
    area: str | None,
    category: str | None,
    budget: str | None,
    candidate_count: int,
    used_default_search: bool,
) -> str:
    conditions = [value for value in (area, category, budget) if value]

    if candidate_count == 0:
        if conditions:
            condition_text = "、".join(conditions)
            return f"{condition_text} の条件で探しましたが、該当するレストランは見つかりませんでした。"
        return "条件に合うレストランは見つかりませんでした。別のエリアや予算でも試せます。"

    if used_default_search:
        return "条件指定が見つからなかったため、登録済みレストランの上位候補を最大3件返します。"

    condition_text = "、".join(conditions)
    return f"{condition_text} の条件に合うレストラン候補を最大3件返します。"


def build_chat_response(
    request: ChatRequest,
    repository: RestaurantRepository,
) -> ChatResponse:
    message = request.message
    area = _extract_area(message)
    category = _extract_category(message)
    budget, budget_values = _extract_budget(message)

    used_default_search = not any((area, category, budget))
    if used_default_search:
        restaurants = repository.list_restaurants(limit=3)
    else:
        restaurants = repository.search_restaurants(
            area=area,
            category=category,
            budget=budget_values,
            limit=3,
        )

    candidates = [
        RestaurantCandidate(
            name=restaurant.name,
            area=restaurant.area,
            category=restaurant.category,
            budget=restaurant.budget,
            description=restaurant.description,
        )
        for restaurant in restaurants
    ]

    reply = _build_reply(
        area=area,
        category=category,
        budget=budget,
        candidate_count=len(candidates),
        used_default_search=used_default_search,
    )
    return ChatResponse(reply=reply, candidates=candidates)
