from scripts.helpful_scripts import get_account, OPENSEA_URL
from brownie import CertificatesCollection

# sample_token_uri = "ipfs/QmQ3DPEaRohoJx8QiWDmJ9ZQAbY9on3eeg6ACWY4K6wyug?filename=johnkaller-metadata.json"
sample_token_uri = "https://gateway.pinata.cloud/ipfs/QmVJWKxptGSiEVsH4sgsUmXGrWBxTYDXWKxRVpzEpPgMAy"
JohnKWallet = "0x93D76F2889061272CdAb3Ff11FB271BA979fFAd1"

def main():
    account = get_account()
    certificate_collectible = CertificatesCollection.deploy({"from": account})
    creation_transaction = certificate_collectible.createCertificate(JohnKWallet, sample_token_uri, {"from": account})
    creation_transaction.wait(1)
    print('Please give up to 20 minutes, and hit the "refresh metadata" button')