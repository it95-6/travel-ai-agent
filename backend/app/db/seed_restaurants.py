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
    {
        "name": "渋谷和み食堂",
        "area": "渋谷",
        "category": "和食",
        "budget": "1000-2000円",
        "description": "渋谷駅近くで手頃に和食ランチを楽しめる食堂です。",
    },
    {
        "name": "新宿炭火焼肉亭",
        "area": "新宿",
        "category": "焼肉",
        "budget": "2000-3000円",
        "description": "コスパの良い焼肉セットが人気の新宿の定番店です。",
    },
    {
        "name": "銀座鮨みやび",
        "area": "銀座",
        "category": "寿司",
        "budget": "8000-12000円",
        "description": "特別な日に使いたい、落ち着いた雰囲気の寿司店です。",
    },
    {
        "name": "浅草和ごはん庵",
        "area": "浅草",
        "category": "和食",
        "budget": "1000-2000円",
        "description": "観光客にも人気の、煮魚や天ぷらが楽しめる和食店です。",
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
