from app.db import get_db
from app.item.services import get_all_items, create_item
from app.item.validation import ItemCreate
from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from sqlalchemy.orm import sessionmaker, Session
import boto3
import os
from dotenv import load_dotenv

load_dotenv()  

router = APIRouter()

S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")

s3_client = boto3.client('s3')

# Health check endpoint
@router.get("/api/items/health")
async def health_check():
    return {"status": "ok"}

# Fetch items from PostgreSQL (RDS)
@router.get("/api/items")
async def get_all(db: Session = Depends(get_db)):
    try:
        items = await get_all_items(db)
        
        return items
    
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch items")

# Create an item in PostgreSQL (RDS)
@router.post("/api/items")
async def create(item: ItemCreate, db: Session = Depends(get_db)):
    try:
        created_item = await create_item(item, db)
        
        return created_item
    
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Failed to create item")

# Upload file to S3
@router.post("/api/items/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        file_content = await file.read()
        s3_client.put_object(Bucket=S3_BUCKET_NAME, Key=file.filename, Body=file_content)

        return {"message": "File uploaded successfully", "filename": file.filename}
    
    except Exception as e:
        print(f"Error uploading file: {e}")
        raise HTTPException(status_code=500, detail="Failed to upload file")
