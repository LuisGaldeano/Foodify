from database.database import Base
from sqlalchemy import Column, Integer, String, BigInteger
from sqlalchemy.orm import Session
import openfoodfacts as offs


class Products(Base):
    __tablename__ = 'products'
    ean = Column(BigInteger, primary_key=True, index=True)
    name = Column(String(255), index=True)
    brand = Column(String(255))
    shop = Column(String(255))
    image = Column(String(10000))
    nutriscore = Column(String)

    def __str__(self):
        return f"id= {self.id} - name= {self.name}"

    def __repr__(self):
        return f"<{str(self)}>"

    @classmethod
    def offs_save_product(cls, db: Session, product_data: dict):
        product = Products(
            ean=product_data['code'],
            name=product_data['product_name'],
            brand=product_data['brands'],
            image=product_data['image_url'],
            nutriscore=product_data['nutriscore_grade']
        )

        db.add(product)
        db.commit()
        db.close()

    @classmethod
    def get_product_and_save(cls, db: Session, barcode: str):
        product_data = offs.products.get_product(barcode)['product']
        if product_data:
            cls.offs_save_product(db, product_data)
            return True
        return False

    @classmethod
    def check_ean_exists(cls, db: Session, ean: str) -> bool:
        return db.query(Products).filter_by(ean=ean).first() is not None

    @classmethod
    def get_product_by_name(cls, db: Session, name: str):
        product = db.query(Products).filter(Products.name == name).first()
        return product

    @classmethod
    def get_product_by_barcode(cls, db: Session, ean: int):
        product = db.query(Products).filter(Products.ean == ean).first()
        return product

    # @classmethod
    # def put_in_nevera(cls, db: Session, ean: int):
    #     product = db.query(Products).filter(Products.ean == ean).first()
    #     new_product = Nevera()
    #     new_product.ean_id = product.ean


