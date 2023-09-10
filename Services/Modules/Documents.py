import base64
import uuid

from supabase import Client

from Services.Models.Document import Document
from Services.States.QuoteStates import QuoteStates


def UpdateQuoteToPendingReview(supabase: Client, process: str):
    responseUpdate = (
        supabase.table('Quotes')
        .update({
            'State': QuoteStates.PENDING_REVIEW.name
        })
        .eq('Process', process)
        .execute())
    if len(responseUpdate.data) == 1:
        return {
            'isBase64Encoded': False,
            'statusCode': 200,
            'body': 'Successful'
        }
    else:
        return {
            'isBase64Encoded': False,
            'statusCode': 403,
            'body': 'Cannot update the state of Quote'
        }


def UploadAllDocuments(supabase: Client, documents: list[Document], process: str):
    error = False
    message = ''
    for document in documents:
        responseUpload = (
            supabase.storage.from_('Documents')
            .upload('{0}.{1}'.format(str(uuid.uuid4()), document.MIME),
                    base64.b64decode(document.Base64)))
        if responseUpload.status_code == 200:
            responseInsert = supabase.table('Documents').insert({
                'Process': process,
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
