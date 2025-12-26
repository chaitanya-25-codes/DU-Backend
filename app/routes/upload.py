from fastapi import APIRouter,UploadFile,File,Form
from fastapi.responses import JSONResponse
from app.services.rag import run_rag
import os
import uuid
from app.utils.pdf_utils import extract_text_from_pdf
import shutil
router=APIRouter()
UPLOAD_DIR="uploads"
os.makedirs(UPLOAD_DIR,exist_ok=True)

@router.post("/submit")
async def submit_file(
    file:UploadFile=File(...),
    description:str=Form(...)
):
    file_path=os.path.join(UPLOAD_DIR,file.filename)
    with open(file_path,"wb") as f:
        shutil.copyfileobj(file.file,f)
    # read the file content as a string
    if(file.filename.endswith(".pdf")):
        text=extract_text_from_pdf(file_path)
    else:
         with open(file_path,"r",encoding="utf-8",errors="ignore") as content_file:
             text=content_file.read()
    response_from_llm=run_rag(
        description=description,
        text=text,
        doc_id = uuid.uuid4().hex
    )
    return JSONResponse({
        "filename": file.filename,
        "doc_id": uuid.uuid4().hex,
        "description": description,
        "llm_response": response_from_llm,
        "message": "File uploaded successfully"
    })