from enum import Enum


class TransactionTypes(Enum):
    Payment = 'Payment',
    TrustSet = 'TrustSet'
    SignerListSet = 'SignerListSet'
    SetRegularKey = 'SetRegularKey',
    PaymentChannelFund = 'PaymentChannelFund'
    PaymentChannelCreate = 'PaymentChannelCreate'
    PaymentChannelClaim = 'PaymentChannelClaim',
    OfferCreate = 'OfferCreate'
    OfferCancel = 'OfferCancel'
    EscrowFinish = 'EscrowFinish',
    EscrowCreate = 'EscrowCreate'
    EscrowCancel = 'EscrowCancel'
    DepositPreauth = 'DepositPreauth',
    CheckCreate = 'CheckCreate'
    CheckCash = 'CheckCash'
    CheckCancel = 'CheckCancel'
    AccountSet = 'AccountSet'
