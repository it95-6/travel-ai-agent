from backend.app.db.init_db import init_db
from backend.app.db.repositories.restaurant_repository import RestaurantRepository
from backend.app.db.session import SessionLocal

SAMPLE_RESTAURANTS = [
    {
        "name": "浅草グリル",
        "area": "浅草",
        "category": "洋食",
        "budget": "2000-3000円",
        "description": "観光の合間に立ち寄りやすい、定番メニュー中心のレストランです。",
    },
    {
        "name": "築地海鮮食堂",
        "area": "築地",
        "category": "海鮮",
        "budget": "3000-4000円",
        "description": "新鮮な魚介を気軽に楽しめる、旅行者向けの人気店です。",
    },
    {
        "name": "表参道ベジキッチン",
        "area": "表参道",
        "category": "カフェ",
        "budget": "1500-2500円",
        "description": "雰囲気が良く、ランチでも休憩でも使いやすいカフェです。",
    },
]


def seed_restaurants() -> int:
    init_db()

    with SessionLocal() as db:
        repository = RestaurantRepository(db)
        if repository.count_restaurants() > 0:
            return 0

        repository.create_restaurants(SAMPLE_RESTAURANTS)
        return len(SAMPLE_RESTAURANTS)


if __name__ == "__main__":
    inserted_count = seed_restaurants()
    print(f"Inserted {inserted_count} restaurant records.")
