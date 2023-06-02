import logging
from datetime import datetime
from sqlalchemy.orm import relationship
import setting.logging as log
from database.database import Base, session
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Float

log.configure_logging()
logger = logging.getLogger(__name__)


class ProductSuperRelationship(Base):
    __tablename__ = "productsuprel"
    id = Column(Integer, primary_key=True, autoincrement=True)
    price = Column(Float, index=True)
    currency = Column(String(255))
    date = Column(Date, default=datetime.utcnow)

    product_id = Column(Integer, ForeignKey("products.id"))
    products = relationship("Products", back_populates="productsuprel")

    super_id = Column(Integer, ForeignKey("supermarket.id"))
    supers = relationship("Supermarket", back_populates="productsuprel")

    def __str__(self):
        return f"id= {self.id}"

    def __repr__(self):
        return f"<{str(self)}>"

    @classmethod
    def save_new_relation(cls, price_num: float, currency: str, super_id: int, product):
        """
        Guarda una nueva relación entre un supermercado y un producto con el precio especificado.

        :param price_num: El precio del producto.
        :param currency: La moneda en la que se expresa el precio.
        :param super_id: El ID del supermercado.
        :param product: El objeto del producto.
        :return: None
        """

        relation = ProductSuperRelationship(
            price=price_num,
            currency=currency,
            product_id=product.id,
            super_id=super_id,
        )

        session.add(relation)
        session.commit()
