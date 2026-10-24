import os
from ._base import _BaseService
from ..response import UnibaseResponse
from ..exceptions import NetworkError

class StorageService(_BaseService):
    def upload(self, file_path: str) -> UnibaseResponse:
        """Upload a file from the local filesystem to Unibase storage."""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
            
        filename = os.path.basename(file_path)
        endpoint = f"{self._client.url}/api/storage/upload"
        
        try:
            with open(file_path, "rb") as f:
                files = {"file": (filename, f)}
                headers = {"ub-api-key": self._client.api_key}
                
                # We do not use self._request here because we need to send multipart/form-data
                # and requests will set the proper content-type header automatically if we don't set it.
                # However, our session has Content-Type: application/json.
                # We must omit it for this specific request.
                
                req_headers = dict(self._client._session.headers)
                req_headers.pop("Content-Type", None)
                req_headers.update(headers)
                
                res = self._client._session.post(
                    endpoint,
                    files=files,
                    headers=req_headers
                )
                try:
                    data = res.json()
                except ValueError:
                    data = {"success": False, "message": res.text, "data": None}
                
                return UnibaseResponse.from_dict(data, status_code=res.status_code)
        except Exception as e:
            raise NetworkError(f"Failed to upload file: {str(e)}")
