from collections.abc import Sequence

from sqlalchemy import func, or_, select
from sqlalchemy.orm import Session

from backend.app.db.models.restaurant import Restaurant


class RestaurantRepository:
    def __init__(self, db: Session):
        self.db = db

    def count_restaurants(self) -> int:
        statement = select(func.count()).select_from(Restaurant)
        return int(self.db.execute(statement).scalar_one())

    def list_restaurants(self, limit: int = 20) -> list[Restaurant]:
        statement = select(Restaurant).order_by(Restaurant.id).limit(limit)
        return list(self.db.scalars(statement).all())

    def search_restaurants(
        self,
        *,
        area: str | None = None,
        category: str | None = None,
        budget: str | Sequence[str] | None = None,
        keyword: str | None = None,
        limit: int = 10,
    ) -> list[Restaurant]:
        statement = select(Restaurant)

        if area:
            statement = statement.where(Restaurant.area.ilike(f"%{area}%"))
        if category:
            statement = statement.where(Restaurant.category.ilike(f"%{category}%"))
        if budget:
            if isinstance(budget, str):
                statement = statement.where(Restaurant.budget.ilike(f"%{budget}%"))
            else:
                statement = statement.where(Restaurant.budget.in_(list(budget)))
        if keyword:
            pattern = f"%{keyword}%"
            statement = statement.where(
                or_(
                    Restaurant.name.ilike(pattern),
                    Restaurant.description.ilike(pattern),
                )
            )

        statement = statement.order_by(Restaurant.id).limit(limit)
        return list(self.db.scalars(statement).all())

    def create_restaurants(self, restaurants: Sequence[dict[str, str]]) -> list[Restaurant]:
        items = [Restaurant(**restaurant) for restaurant in restaurants]
        self.db.add_all(items)
        self.db.commit()

        for item in items:
            self.db.refresh(item)

        return items
