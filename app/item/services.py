from app.item.validation import ItemCreate
from fastapi import Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.item.model import Item
from datetime import datetime, timedelta, timezone
from typing import List, Optional

async def get_all_items(db: Session):
  items = db.query(Item).all()

  return items

async def create_item(item: ItemCreate, db: Session):

  db_item = Item(name=item.name)
  db.add(db_item)
  db.commit()
  db.refresh(db_item)

  return db_item
