


const RequiredKeys = [
    "type",
    "project_id",
    "private_key_id",
    "private_key",
    "client_email",
    "client_id",
    "auth_uri",
    "token_uri",
    "auth_provider_x509_cert_url", "client_x509_cert_url"
  ]


const MissingKey = (json) => {
    for (const key of RequiredKeys) {
        if (json[key] === undefined)
          return key
    } 
    return undefined
}


export default MissingKey