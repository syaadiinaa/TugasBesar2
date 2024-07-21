import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class HTTPException(Exception):
    def __init__(self, status_code, detail):
        self.status_code = status_code
        self.detail = detail
        super().__init__(self.detail)

#penggunaan
try:
    buku = get_buku(1)
    if buku is None:
        raise HTTPException(404, "Buku tidak ditemukan")
except HTTPException as e:
    logger.error(f"Error {e.status_code}: {e.detail}")
