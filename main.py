from fastapi import FastAPI
app=FastAPI(title="this neww app")

@app.get('/')
async def wellcome():
    return {"data":"this is firast data"}