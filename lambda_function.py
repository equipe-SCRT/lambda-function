import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    bucket_name = 'bucket-scrt'
    s3 = boto3.resource('s3')
    objeto = s3.Object(bucket_name, event['nomeArquivo'] + '.txt')
    fileTxt = json.dumps(event['dadosArquivo'])
    
    objeto.put(Body=fileTxt)
    return {
        'statusCode': 200,
        'body': json.dumps('Arquivo gerado com sucesso')
    }
