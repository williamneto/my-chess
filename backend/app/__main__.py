import uvicorn

from app.core.config import settings

if __name__ == '__main__':
    if settings.ENV.lower() == "development":
        uvicorn.run("app.main:app",
                    host=settings.HOST,
                    port=settings.PORT,
                    reload=True,
                    proxy_headers=True, # THIS LINE
                    forwarded_allow_ips='*', 
                    log_level="debug",
                    reload_excludes="*.session")

