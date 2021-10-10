from Sophia import aiohttpsession

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
}


async def fetch(url: str):
    async with aiohttpsession.get(url, headers=headers) as resp:
        try:
            data = await resp.json()
        except Exception:
            data = await resp.text()
    return data
