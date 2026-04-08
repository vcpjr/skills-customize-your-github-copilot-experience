from typing import List, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float
    available: bool = True


app = FastAPI(title="FastAPI REST API")

items: List[Item] = [
    Item(id=1, name="Caneta", description="Caneta azul", price=2.5, available=True),
    Item(id=2, name="Caderno", description="Caderno de 100 folhas", price=15.0, available=True),
]


@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API REST com FastAPI"}


@app.get("/items/", response_model=List[Item])
def read_items():
    return items


@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item não encontrado")


@app.post("/items/", response_model=Item, status_code=201)
def create_item(item: Item):
    if any(existing.id == item.id for existing in items):
        raise HTTPException(status_code=400, detail="ID do item já existe")
    items.append(item)
    return item


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item):
    for index, existing in enumerate(items):
        if existing.id == item_id:
            items[index] = item
            return item
    raise HTTPException(status_code=404, detail="Item não encontrado")


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for index, existing in enumerate(items):
        if existing.id == item_id:
            items.pop(index)
            return {"message": "Item removido com sucesso"}
    raise HTTPException(status_code=404, detail="Item não encontrado")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
