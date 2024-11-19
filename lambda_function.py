import json
import boto3
import base64

def lambda_handler(event, context):
    bucket_name = 'bucket-scrt-2'
    s3 = boto3.resource('s3')

    try:
        objeto = s3.Object(bucket_name, event['nomeArquivo'])
    except Exception as e:
        response = {
            'statusCode': 500,
            'body': 'Falha ao conectar ao S3 (nome do arquivo)',
            'message': str(e),
            'bodyErr': event['dadosArquivo']
        }
        return json.dumps(response)

    try:
        file_bytes = base64.b64decode(event['dadosArquivo'])
        fileTxt = bytearray(file_bytes)
    except Exception as e:
        response = {
            'statusCode': 500,
            'body': 'Falha ao processar os dados do arquivo',
            'message': str(e),
            'bodyErr': event['dadosArquivo']
        }
        return json.dumps(response)

    try:
        objeto.put(Body=fileTxt)
        response = {
            'statusCode': 200,
            'body': 'Arquivo gerado com sucesso'
        }
    except Exception as e:
        response = {
            'statusCode': 500,
            'body': 'Erro ao inserir arquivo',
            'message': str(e),
            'bodyErr': event['dadosArquivo']
        }
        return json.dumps(response)

    return json.dumps(response)
