from backend.app.schemas.chat import ChatRequest, ChatResponse, RecommendationItem


def build_chat_response(request: ChatRequest) -> ChatResponse:
    message = request.message.lower()
    recommendations = []

    if any(keyword in message for keyword in ("travel", "trip", "sightseeing", "旅行", "観光")):
        recommendations.append(
            RecommendationItem(
                category="travel",
                title="浅草",
                reason="街歩きと観光をまとめて楽しみやすい定番エリアだからです。",
            )
        )

    if any(keyword in message for keyword in ("restaurant", "food", "eat", "レストラン", "食事", "グルメ")):
        recommendations.append(
            RecommendationItem(
                category="restaurant",
                title="築地周辺",
                reason="飲食店の候補が多く、旅行文脈とも相性が良いからです。",
            )
        )

    if not recommendations:
        recommendations = [
            RecommendationItem(
                category="travel",
                title="鎌倉",
                reason="日帰りでも動きやすく、初回の提案先として扱いやすいためです。",
            ),
            RecommendationItem(
                category="restaurant",
                title="表参道カフェエリア",
                reason="ジャンルの幅があり、好みの追加条件を聞きやすいためです。",
            ),
        ]

    return ChatResponse(
        reply=(
            "最小実装のチャット応答です。"
            "今後は SQLite や外部API連携に置き換えやすいよう、"
            "ルーター・スキーマ・サービスを分けています。"
        ),
        recommendations=recommendations,
    )
