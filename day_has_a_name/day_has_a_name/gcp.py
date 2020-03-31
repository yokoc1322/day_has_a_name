from google.cloud import secretmanager


def get_secret(project_id, secret_id, version_name):
    client = secretmanager.SecretManagerServiceClient()
    name = client.secret_version_path(project_id, secret_id, version_name)
    response = client.access_secret_version(name)
    payload = response.payload.data.decode('UTF-8')
    return payload
