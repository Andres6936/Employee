import base64
import uuid

from supabase import Client

from Services.Models.Document import Document


def UploadAllDocuments(supabase: Client, documents: list[Document]):
    error = False
    message = ''
    for document in documents:
        responseUpload = (
            supabase.storage.from_('DocumentsQuote')
            .upload('{0}.{1}'.format(str(uuid.uuid4()), document.MIME),
                    base64.b64decode(document.Base64)))
        if responseUpload.status_code == 200:
            responseInsert = supabase.table('DocumentsQuotes').insert({
                'Process': documents.Process,
                'Type': document.Type,
                'URL': str(responseUpload.request.url),
            }).execute()
            if len(responseInsert.data) != 1:
                error = True
                message = 'Document not register in database'
        else:
            error = True
            message = 'Document cannot upload to storage'
    return {
        'Error': error,
        'Message': message
    }
