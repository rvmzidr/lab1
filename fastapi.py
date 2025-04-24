from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Liste pour stocker les items
items = []

# Modèle Pydantic pour l'Item
class Item(BaseModel):
    text: str = None
    is_done: bool = False

# Méthode pour créer un item
@app.post("/items")
def create_item(item: Item) -> Item:
    items.append(item)
    return item

# Méthode pour récupérer un item par son ID
@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int) -> Item:
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found")