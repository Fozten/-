import uvicorn
from fastapi import FastAPI, Request
from aiogram import Bot, Dispatcher
from aiogram.types import Update
import config
from bot import dp, bot

app = FastAPI()


@app.on_event("startup")
async def on_startup():
    # Устанавливаем webhook при запуске
    await bot.set_webhook(config.WEBHOOK_URL)


@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    update = Update(**data)
    await dp.feed_update(bot, update)
    return {"ok": True}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=False
    )
