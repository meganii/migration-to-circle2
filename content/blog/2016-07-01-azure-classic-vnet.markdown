---
title: "azure classic vnet"
date: 2016-07-01T21:57:59+09:00
comments: true
category: ['']
tags: ['']
published: false
slug: azure-classic-vnet
img:
---

<!--more-->
{{% googleadsense %}}


## Azure ポータルで仮想ネットワーク(クラシック)を作成するとどうなるか？

`group asm-rg classic-vnet`とprefixにリソースグループ名 仮想ネットワーク名となる。

仮想ネットワーク(クラシック)と

```
PS C:\Users\meganii> Set-AzureVNetGatewayKey -VNetName asm-vnet -LocalNetworkSiteName arm-vnet -SharedKey secretKey

Error          :
HttpStatusCode : OK
Id             : 4aa20471-b093-41e6-987a-9a6f00c5575c
Status         : Successful
RequestId      : ff07be86feacabf198bfac5af8584fa0
StatusCode     : OK
```

## PowerShell

add-azureaccount

Set-AzureVNetGatewayKey -VNetName asm-vnet -LocalNetworkSiteName arm-vnet-local -SharedKey grec42191


## 用語確認

- FQDN (Fully Qualified Domain Name)
> FQDNとはDNS(Domain Name System)などのホスト名、ドメイン名などすべてを省略せずに指定した記法形式


## VPN接続確認

```
Get-AzureRmVirtualNetworkGatewayConnection -Name localtovon -ResourceGroupName testrg -Debug
```
[Azure Resource Manager と PowerShell を使用してサイト間 VPN 接続で仮想ネットワークを作成する | Microsoft Azure](https://azure.microsoft.com/ja-jp/documentation/articles/vpn-gateway-create-site-to-site-rm-powershell/#4vpn-ip)


```
PS C:\Users\meganii> Get-AzureRmVirtualNetworkGatewayConnection -ResourceGroupName Default-Networking -Debug
DEBUG: 1:45:32 AM - GetAzureVirtualNetworkGatewayConnectionCommand begin processing with ParameterSet
'__AllParameterSets'.

Confirm
Continue with this operation?
[Y] Yes  [A] Yes to All  [H] Halt Command  [S] Suspend  [?] Help (default is "Y"): A
DEBUG: 1:45:36 AM - using account id 'yt_meganii@yahoo.co.jp'...
DEBUG: [Common.Authentication]: Authenticating using Account: 'yt_meganii@yahoo.co.jp', environment: 'AzureCloud',
tenant: 'c6e14170-2cd7-451a-9955-72ac3eabbd1b'
DEBUG: Microsoft.IdentityModel.Clients.ActiveDirectory Information: 2 :
DEBUG: 7/3/2016 1:45:40 AM:  - TokenCache: Deserialized 3 items to token cache.
DEBUG: Microsoft.IdentityModel.Clients.ActiveDirectory Information: 2 :
DEBUG: 7/3/2016 1:45:40 AM: 474da6d7-6836-48bd-88ce-5debe9d62daa - AcquireTokenHandlerBase: === Token Acquisition
started:
 Authority: https://login.microsoftonline.com/c6e14170-2cd7-451a-9955-72ac3eabbd1b/
 Resource: https://management.core.windows.net/
 ClientId: 1950a258-227b-4e31-a9cf-717495945fc2
 CacheType: Microsoft.IdentityModel.Clients.ActiveDirectory.TokenCache (3 items)
 Authentication Target: User

DEBUG: Microsoft.IdentityModel.Clients.ActiveDirectory Verbose: 1 :
DEBUG: 7/3/2016 1:45:40 AM: 474da6d7-6836-48bd-88ce-5debe9d62daa - TokenCache: Looking up cache for a token...
DEBUG: Microsoft.IdentityModel.Clients.ActiveDirectory Information: 2 :
DEBUG: 7/3/2016 1:45:40 AM: 474da6d7-6836-48bd-88ce-5debe9d62daa - TokenCache: An item matching the requested resource
was found in the cache
DEBUG: Microsoft.IdentityModel.Clients.ActiveDirectory Verbose: 1 :
DEBUG: 7/3/2016 1:45:40 AM: 474da6d7-6836-48bd-88ce-5debe9d62daa - TokenCache: 59.7295647383333 minutes left until
token in cache expires
DEBUG: Microsoft.IdentityModel.Clients.ActiveDirectory Information: 2 :
DEBUG: 7/3/2016 1:45:40 AM: 474da6d7-6836-48bd-88ce-5debe9d62daa - TokenCache: A matching item (access token or refresh
 token or both) was found in the cache
DEBUG: Microsoft.IdentityModel.Clients.ActiveDirectory Information: 2 :
DEBUG: 7/3/2016 1:45:40 AM: 474da6d7-6836-48bd-88ce-5debe9d62daa - AcquireTokenHandlerBase: === Token Acquisition
finished successfully. An access token was retuned:
 Access Token Hash: U6rJPpVK8sjTrgmy8rhx2mLGRET5in70Wwj/8UsS324=
 Refresh Token Hash: yt0iFqKEHar7Aoraumrp0UAawuW/IvBdI9HM07n3kPA=
 Expiration Time: 7/3/2016 2:45:23 AM +00:00
 User Hash: 8QIR9RcspE6WAOxBYSrldv4y1ixVkVLcKLDiaCfXEKM=

DEBUG: Microsoft.IdentityModel.Clients.ActiveDirectory Information: 2 :
DEBUG: 7/3/2016 1:45:40 AM:  - TokenCache: Serializing token cache with 3 items.
DEBUG: Microsoft.IdentityModel.Clients.ActiveDirectory Information: 2 :
DEBUG: 7/3/2016 1:45:40 AM: 90f669ec-2ec2-44af-b7c2-e045e5dd406c - AcquireTokenHandlerBase: === Token Acquisition
started:
 Authority: https://login.microsoftonline.com/c6e14170-2cd7-451a-9955-72ac3eabbd1b/
 Resource: https://management.core.windows.net/
 ClientId: 1950a258-227b-4e31-a9cf-717495945fc2
 CacheType: Microsoft.IdentityModel.Clients.ActiveDirectory.TokenCache (3 items)
 Authentication Target: User

DEBUG: Microsoft.IdentityModel.Clients.ActiveDirectory Verbose: 1 :
DEBUG: 7/3/2016 1:45:40 AM: 90f669ec-2ec2-44af-b7c2-e045e5dd406c - TokenCache: Looking up cache for a token...
DEBUG: Microsoft.IdentityModel.Clients.ActiveDirectory Information: 2 :
DEBUG: 7/3/2016 1:45:40 AM: 90f669ec-2ec2-44af-b7c2-e045e5dd406c - TokenCache: An item matching the requested resource
was found in the cache
DEBUG: Microsoft.IdentityModel.Clients.ActiveDirectory Verbose: 1 :
DEBUG: 7/3/2016 1:45:40 AM: 90f669ec-2ec2-44af-b7c2-e045e5dd406c - TokenCache: 59.7282631066667 minutes left until
token in cache expires
DEBUG: Microsoft.IdentityModel.Clients.ActiveDirectory Information: 2 :
DEBUG: 7/3/2016 1:45:40 AM: 90f669ec-2ec2-44af-b7c2-e045e5dd406c - TokenCache: A matching item (access token or refresh
 token or both) was found in the cache
DEBUG: Microsoft.IdentityModel.Clients.ActiveDirectory Information: 2 :
DEBUG: 7/3/2016 1:45:40 AM: 90f669ec-2ec2-44af-b7c2-e045e5dd406c - AcquireTokenHandlerBase: === Token Acquisition
finished successfully. An access token was retuned:
 Access Token Hash: U6rJPpVK8sjTrgmy8rhx2mLGRET5in70Wwj/8UsS324=
 Refresh Token Hash: yt0iFqKEHar7Aoraumrp0UAawuW/IvBdI9HM07n3kPA=
 Expiration Time: 7/3/2016 2:45:23 AM +00:00
 User Hash: 8QIR9RcspE6WAOxBYSrldv4y1ixVkVLcKLDiaCfXEKM=

DEBUG: ============================ HTTP REQUEST ============================

HTTP Method:
GET

Absolute Uri:
https://management.azure.com/subscriptions/f7996802-3da7-4a3a-bf02-80fee24df3fb/resourceGroups/Default-Networking/provi
ders/Microsoft.Network/connections?api-version=2016-03-30

Headers:
x-ms-client-request-id        : da243457-543a-4461-8a71-aa7f9787fb6f
accept-language               : en-US

Body:


DEBUG: ============================ HTTP RESPONSE ============================

Status Code:
OK

Headers:
Pragma                        : no-cache
x-ms-ratelimit-remaining-subscription-reads: 14998
x-ms-request-id               : 856220de-6363-4255-9616-f5a330c10ddc
x-ms-correlation-request-id   : 856220de-6363-4255-9616-f5a330c10ddc
x-ms-routing-request-id       : JAPANEAST:20160703T014540Z:856220de-6363-4255-9616-f5a330c10ddc
Strict-Transport-Security     : max-age=31536000; includeSubDomains
Cache-Control                 : no-cache
Date                          : Sun, 03 Jul 2016 01:45:39 GMT

Body:
{
  "value": []
}

DEBUG: 1:45:40 AM - GetAzureVirtualNetworkGatewayConnectionCommand end processing.
DEBUG: 1:45:40 AM - GetAzureVirtualNetworkGatewayConnectionCommand end processing.
PS C:\Users\meganii>
```

Get-AzureRmVirtualNetworkGatewayConnection -ResourceGroupName arm-rg -Debug


```
PS C:\Users\meganii> Get-AzureRmVirtualNetworkGatewayConnection -ResourceGroupName arm-rg -Debug
DEBUG: 2:03:45 AM - GetAzureVirtualNetworkGatewayConnectionCommand begin processing with ParameterSet
'__AllParameterSets'.

Confirm
Continue with this operation?
[Y] Yes  [A] Yes to All  [H] Halt Command  [S] Suspend  [?] Help (default is "Y"): A
DEBUG: 2:03:47 AM - using account id 'yt_meganii@yahoo.co.jp'...
DEBUG: [Common.Authentication]: Authenticating using Account: 'yt_meganii@yahoo.co.jp', environment: 'AzureCloud',
tenant: 'c6e14170-2cd7-451a-9955-72ac3eabbd1b'
DEBUG: Microsoft.IdentityModel.Clients.ActiveDirectory Information: 2 :
DEBUG: 7/3/2016 2:03:47 AM:  - TokenCache: Deserialized 3 items to token cache.
DEBUG: Microsoft.IdentityModel.Clients.ActiveDirectory Information: 2 :
DEBUG: 7/3/2016 2:03:47 AM: b845429d-0ace-4a2a-aeaf-5353cc884e86 - AcquireTokenHandlerBase: === Token Acquisition
started:
 Authority: https://login.microsoftonline.com/c6e14170-2cd7-451a-9955-72ac3eabbd1b/
 Resource: https://management.core.windows.net/
 ClientId: 1950a258-227b-4e31-a9cf-717495945fc2
 CacheType: Microsoft.IdentityModel.Clients.ActiveDirectory.TokenCache (3 items)
 Authentication Target: User

DEBUG: Microsoft.IdentityModel.Clients.ActiveDirectory Verbose: 1 :
DEBUG: 7/3/2016 2:03:47 AM: b845429d-0ace-4a2a-aeaf-5353cc884e86 - TokenCache: Looking up cache for a token...
DEBUG: Microsoft.IdentityModel.Clients.ActiveDirectory Information: 2 :
DEBUG: 7/3/2016 2:03:47 AM: b845429d-0ace-4a2a-aeaf-5353cc884e86 - TokenCache: An item matching the requested resource
was found in the cache
DEBUG: Microsoft.IdentityModel.Clients.ActiveDirectory Verbose: 1 :
DEBUG: 7/3/2016 2:03:47 AM: b845429d-0ace-4a2a-aeaf-5353cc884e86 - TokenCache: 41.605021315 minutes left until token in
 cache expires
DEBUG: Microsoft.IdentityModel.Clients.ActiveDirectory Information: 2 :
DEBUG: 7/3/2016 2:03:47 AM: b845429d-0ace-4a2a-aeaf-5353cc884e86 - TokenCache: A matching item (access token or refresh
 token or both) was found in the cache
DEBUG: Microsoft.IdentityModel.Clients.ActiveDirectory Information: 2 :
DEBUG: 7/3/2016 2:03:47 AM: b845429d-0ace-4a2a-aeaf-5353cc884e86 - AcquireTokenHandlerBase: === Token Acquisition
finished successfully. An access token was retuned:
 Access Token Hash: U6rJPpVK8sjTrgmy8rhx2mLGRET5in70Wwj/8UsS324=
 Refresh Token Hash: yt0iFqKEHar7Aoraumrp0UAawuW/IvBdI9HM07n3kPA=
 Expiration Time: 7/3/2016 2:45:23 AM +00:00
 User Hash: 8QIR9RcspE6WAOxBYSrldv4y1ixVkVLcKLDiaCfXEKM=

DEBUG: Microsoft.IdentityModel.Clients.ActiveDirectory Information: 2 :
DEBUG: 7/3/2016 2:03:47 AM:  - TokenCache: Serializing token cache with 3 items.
DEBUG: Microsoft.IdentityModel.Clients.ActiveDirectory Information: 2 :
DEBUG: 7/3/2016 2:03:47 AM: 720d3138-e912-4310-9003-28d885386d1c - AcquireTokenHandlerBase: === Token Acquisition
started:
 Authority: https://login.microsoftonline.com/c6e14170-2cd7-451a-9955-72ac3eabbd1b/
 Resource: https://management.core.windows.net/
 ClientId: 1950a258-227b-4e31-a9cf-717495945fc2
 CacheType: Microsoft.IdentityModel.Clients.ActiveDirectory.TokenCache (3 items)
 Authentication Target: User

DEBUG: Microsoft.IdentityModel.Clients.ActiveDirectory Verbose: 1 :
DEBUG: 7/3/2016 2:03:47 AM: 720d3138-e912-4310-9003-28d885386d1c - TokenCache: Looking up cache for a token...
DEBUG: Microsoft.IdentityModel.Clients.ActiveDirectory Information: 2 :
DEBUG: 7/3/2016 2:03:47 AM: 720d3138-e912-4310-9003-28d885386d1c - TokenCache: An item matching the requested resource
was found in the cache
DEBUG: Microsoft.IdentityModel.Clients.ActiveDirectory Verbose: 1 :
DEBUG: 7/3/2016 2:03:47 AM: 720d3138-e912-4310-9003-28d885386d1c - TokenCache: 41.605021315 minutes left until token in
 cache expires
DEBUG: Microsoft.IdentityModel.Clients.ActiveDirectory Information: 2 :
DEBUG: 7/3/2016 2:03:47 AM: 720d3138-e912-4310-9003-28d885386d1c - TokenCache: A matching item (access token or refresh
 token or both) was found in the cache
DEBUG: Microsoft.IdentityModel.Clients.ActiveDirectory Information: 2 :
DEBUG: 7/3/2016 2:03:47 AM: 720d3138-e912-4310-9003-28d885386d1c - AcquireTokenHandlerBase: === Token Acquisition
finished successfully. An access token was retuned:
 Access Token Hash: U6rJPpVK8sjTrgmy8rhx2mLGRET5in70Wwj/8UsS324=
 Refresh Token Hash: yt0iFqKEHar7Aoraumrp0UAawuW/IvBdI9HM07n3kPA=
 Expiration Time: 7/3/2016 2:45:23 AM +00:00
 User Hash: 8QIR9RcspE6WAOxBYSrldv4y1ixVkVLcKLDiaCfXEKM=

DEBUG: ============================ HTTP REQUEST ============================

HTTP Method:
GET

Absolute Uri:
https://management.azure.com/subscriptions/f7996802-3da7-4a3a-bf02-80fee24df3fb/resourceGroups/arm-rg/providers/Microso
ft.Network/connections?api-version=2016-03-30

Headers:
x-ms-client-request-id        : fc39efd0-ebee-480c-8e15-2ea2fbc11d38
accept-language               : en-US

Body:


DEBUG: ============================ HTTP RESPONSE ============================

Status Code:
OK

Headers:
Pragma                        : no-cache
x-ms-request-id               : daa4f165-c95d-4ba5-ab48-1b1a26922292
Strict-Transport-Security     : max-age=31536000; includeSubDomains
Cache-Control                 : no-cache
Server                        : Microsoft-HTTPAPI/2.0,Microsoft-HTTPAPI/2.0
x-ms-ratelimit-remaining-subscription-reads: 14999
x-ms-correlation-request-id   : 78fd8b17-f405-4821-8651-42052d37baa2
x-ms-routing-request-id       : JAPANEAST:20160703T020347Z:78fd8b17-f405-4821-8651-42052d37baa2
Date                          : Sun, 03 Jul 2016 02:03:47 GMT

Body:
{
  "value": [
    {
      "name": "asm-vnet-local",
      "id":
"/subscriptions/f7996802-3da7-4a3a-bf02-80fee24df3fb/resourceGroups/arm-rg/providers/Microsoft.Network/connections/asm-
vnet-local",
      "etag": "W/\"eeb34c1a-1c47-4019-b57d-0671c2194f7a\"",
      "type": "Microsoft.Network/connections",
      "location": "japaneast",
      "properties": {
        "provisioningState": "Succeeded",
        "resourceGuid": "d1a92429-1a95-4ede-84b1-34cf000ee9d8",
        "virtualNetworkGateway1": {
          "id":
"/subscriptions/f7996802-3da7-4a3a-bf02-80fee24df3fb/resourceGroups/arm-rg/providers/Microsoft.Network/virtualNetworkGa
teways/vpn-gateway"
        },
        "localNetworkGateway2": {
          "id":
"/subscriptions/f7996802-3da7-4a3a-bf02-80fee24df3fb/resourceGroups/arm-rg/providers/Microsoft.Network/localNetworkGate
ways/asm-vnet-gateway"
        },
        "connectionType": "IPsec",
        "routingWeight": 0,
        "enableBgp": false,
        "ingressBytesTransferred": 0,
        "egressBytesTransferred": 0
      }
    }
  ]
}



AuthorizationKey           :
VirtualNetworkGateway1     : Microsoft.Azure.Commands.Network.Models.PSVirtualNetworkGateway
VirtualNetworkGateway2     :
LocalNetworkGateway2       : Microsoft.Azure.Commands.Network.Models.PSLocalNetworkGateway
Peer                       :
ConnectionType             : IPsec
RoutingWeight              : 0
SharedKey                  :
EnableBgp                  : False
ConnectionStatus           :
EgressBytesTransferred     : 0
IngressBytesTransferred    : 0
ProvisioningState          : Succeeded
VirtualNetworkGateway1Text : "/subscriptions/f7996802-3da7-4a3a-bf02-80fee24df3fb/resourceGroups/arm-rg/providers/Micro
                             soft.Network/virtualNetworkGateways/vpn-gateway"
VirtualNetworkGateway2Text :
LocalNetworkGateway2Text   : "/subscriptions/f7996802-3da7-4a3a-bf02-80fee24df3fb/resourceGroups/arm-rg/providers/Micro
                             soft.Network/localNetworkGateways/asm-vnet-gateway"
PeerText                   :
ResourceGroupName          : arm-rg
Location                   : japaneast
ResourceGuid               : d1a92429-1a95-4ede-84b1-34cf000ee9d8
Tag                        : {}
TagsTable                  :
Name                       : asm-vnet-local
Etag                       : W/"eeb34c1a-1c47-4019-b57d-0671c2194f7a"
Id                         : /subscriptions/f7996802-3da7-4a3a-bf02-80fee24df3fb/resourceGroups/arm-rg/providers/Micros
                             oft.Network/connections/asm-vnet-local

DEBUG: 2:03:48 AM - GetAzureVirtualNetworkGatewayConnectionCommand end processing.
DEBUG: 2:03:48 AM - GetAzureVirtualNetworkGatewayConnectionCommand end processing.
```


```
PS C:\Users\meganii> Get-AzureRmVirtualNetworkGatewayConnection -Name asm-vnet-local -ResourceGroupName arm-rg -Debug
DEBUG: 2:09:55 AM - GetAzureVirtualNetworkGatewayConnectionCommand begin processing with ParameterSet
'__AllParameterSets'.

Confirm
Continue with this operation?
[Y] Yes  [A] Yes to All  [H] Halt Command  [S] Suspend  [?] Help (default is "Y"): A
DEBUG: 2:09:58 AM - using account id 'yt_meganii@yahoo.co.jp'...
DEBUG: [Common.Authentication]: Authenticating using Account: 'yt_meganii@yahoo.co.jp', environment: 'AzureCloud',
tenant: 'c6e14170-2cd7-451a-9955-72ac3eabbd1b'
DEBUG: Microsoft.IdentityModel.Clients.ActiveDirectory Information: 2 :
DEBUG: 7/3/2016 2:09:58 AM:  - TokenCache: Deserialized 3 items to token cache.
DEBUG: Microsoft.IdentityModel.Clients.ActiveDirectory Information: 2 :
DEBUG: 7/3/2016 2:09:58 AM: 0eb916e4-7954-49f4-af1d-88bbd74a45da - AcquireTokenHandlerBase: === Token Acquisition
started:
 Authority: https://login.microsoftonline.com/c6e14170-2cd7-451a-9955-72ac3eabbd1b/
 Resource: https://management.core.windows.net/
 ClientId: 1950a258-227b-4e31-a9cf-717495945fc2
 CacheType: Microsoft.IdentityModel.Clients.ActiveDirectory.TokenCache (3 items)
 Authentication Target: User

DEBUG: Microsoft.IdentityModel.Clients.ActiveDirectory Verbose: 1 :
DEBUG: 7/3/2016 2:09:58 AM: 0eb916e4-7954-49f4-af1d-88bbd74a45da - TokenCache: Looking up cache for a token...
DEBUG: Microsoft.IdentityModel.Clients.ActiveDirectory Information: 2 :
DEBUG: 7/3/2016 2:09:58 AM: 0eb916e4-7954-49f4-af1d-88bbd74a45da - TokenCache: An item matching the requested resource
was found in the cache
DEBUG: Microsoft.IdentityModel.Clients.ActiveDirectory Verbose: 1 :
DEBUG: 7/3/2016 2:09:58 AM: 0eb916e4-7954-49f4-af1d-88bbd74a45da - TokenCache: 35.432215295 minutes left until token in
 cache expires
DEBUG: Microsoft.IdentityModel.Clients.ActiveDirectory Information: 2 :
DEBUG: 7/3/2016 2:09:58 AM: 0eb916e4-7954-49f4-af1d-88bbd74a45da - TokenCache: A matching item (access token or refresh
 token or both) was found in the cache
DEBUG: Microsoft.IdentityModel.Clients.ActiveDirectory Information: 2 :
DEBUG: 7/3/2016 2:09:58 AM: 0eb916e4-7954-49f4-af1d-88bbd74a45da - AcquireTokenHandlerBase: === Token Acquisition
finished successfully. An access token was retuned:
 Access Token Hash: U6rJPpVK8sjTrgmy8rhx2mLGRET5in70Wwj/8UsS324=
 Refresh Token Hash: yt0iFqKEHar7Aoraumrp0UAawuW/IvBdI9HM07n3kPA=
 Expiration Time: 7/3/2016 2:45:23 AM +00:00
 User Hash: 8QIR9RcspE6WAOxBYSrldv4y1ixVkVLcKLDiaCfXEKM=

DEBUG: Microsoft.IdentityModel.Clients.ActiveDirectory Information: 2 :
DEBUG: 7/3/2016 2:09:58 AM:  - TokenCache: Serializing token cache with 3 items.
DEBUG: Microsoft.IdentityModel.Clients.ActiveDirectory Information: 2 :
DEBUG: 7/3/2016 2:09:58 AM: b1bb55c5-9347-4958-9dce-3a8e664ccd0e - AcquireTokenHandlerBase: === Token Acquisition
started:
 Authority: https://login.microsoftonline.com/c6e14170-2cd7-451a-9955-72ac3eabbd1b/
 Resource: https://management.core.windows.net/
 ClientId: 1950a258-227b-4e31-a9cf-717495945fc2
 CacheType: Microsoft.IdentityModel.Clients.ActiveDirectory.TokenCache (3 items)
 Authentication Target: User

DEBUG: Microsoft.IdentityModel.Clients.ActiveDirectory Verbose: 1 :
DEBUG: 7/3/2016 2:09:58 AM: b1bb55c5-9347-4958-9dce-3a8e664ccd0e - TokenCache: Looking up cache for a token...
DEBUG: Microsoft.IdentityModel.Clients.ActiveDirectory Information: 2 :
DEBUG: 7/3/2016 2:09:58 AM: b1bb55c5-9347-4958-9dce-3a8e664ccd0e - TokenCache: An item matching the requested resource
was found in the cache
DEBUG: Microsoft.IdentityModel.Clients.ActiveDirectory Verbose: 1 :
DEBUG: 7/3/2016 2:09:58 AM: b1bb55c5-9347-4958-9dce-3a8e664ccd0e - TokenCache: 35.43143363 minutes left until token in
cache expires
DEBUG: Microsoft.IdentityModel.Clients.ActiveDirectory Information: 2 :
DEBUG: 7/3/2016 2:09:58 AM: b1bb55c5-9347-4958-9dce-3a8e664ccd0e - TokenCache: A matching item (access token or refresh
 token or both) was found in the cache
DEBUG: Microsoft.IdentityModel.Clients.ActiveDirectory Information: 2 :
DEBUG: 7/3/2016 2:09:58 AM: b1bb55c5-9347-4958-9dce-3a8e664ccd0e - AcquireTokenHandlerBase: === Token Acquisition
finished successfully. An access token was retuned:
 Access Token Hash: U6rJPpVK8sjTrgmy8rhx2mLGRET5in70Wwj/8UsS324=
 Refresh Token Hash: yt0iFqKEHar7Aoraumrp0UAawuW/IvBdI9HM07n3kPA=
 Expiration Time: 7/3/2016 2:45:23 AM +00:00
 User Hash: 8QIR9RcspE6WAOxBYSrldv4y1ixVkVLcKLDiaCfXEKM=

DEBUG: ============================ HTTP REQUEST ============================

HTTP Method:
GET

Absolute Uri:
https://management.azure.com/subscriptions/f7996802-3da7-4a3a-bf02-80fee24df3fb/resourceGroups/arm-rg/providers/Microso
ft.Network/connections/asm-vnet-local?api-version=2016-03-30

Headers:
x-ms-client-request-id        : fa63c9f6-0c3e-4a68-a8cb-ee599ca36e0b
accept-language               : en-US

Body:


DEBUG: ============================ HTTP RESPONSE ============================

Status Code:
OK

Headers:
Pragma                        : no-cache
x-ms-request-id               : 59fc197b-0e4c-4257-aad0-728a7069a465
Strict-Transport-Security     : max-age=31536000; includeSubDomains
Cache-Control                 : no-cache
Server                        : Microsoft-HTTPAPI/2.0,Microsoft-HTTPAPI/2.0
x-ms-ratelimit-remaining-subscription-reads: 14998
x-ms-correlation-request-id   : e79a179f-d242-45f0-b370-42ab20fcfd66
x-ms-routing-request-id       : JAPANEAST:20160703T020959Z:e79a179f-d242-45f0-b370-42ab20fcfd66
Date                          : Sun, 03 Jul 2016 02:09:59 GMT

Body:
{
  "name": "asm-vnet-local",
  "id":
"/subscriptions/f7996802-3da7-4a3a-bf02-80fee24df3fb/resourceGroups/arm-rg/providers/Microsoft.Network/connections/asm-
vnet-local",
  "etag": "W/\"eeb34c1a-1c47-4019-b57d-0671c2194f7a\"",
  "type": "Microsoft.Network/connections",
  "location": "japaneast",
  "properties": {
    "provisioningState": "Succeeded",
    "resourceGuid": "d1a92429-1a95-4ede-84b1-34cf000ee9d8",
    "virtualNetworkGateway1": {
      "id":
"/subscriptions/f7996802-3da7-4a3a-bf02-80fee24df3fb/resourceGroups/arm-rg/providers/Microsoft.Network/virtualNetworkGa
teways/vpn-gateway"
    },
    "localNetworkGateway2": {
      "id":
"/subscriptions/f7996802-3da7-4a3a-bf02-80fee24df3fb/resourceGroups/arm-rg/providers/Microsoft.Network/localNetworkGate
ways/asm-vnet-gateway"
    },
    "connectionType": "IPsec",
    "routingWeight": 0,
    "sharedKey": "grec42191",
    "enableBgp": false,
    "connectionStatus": "Connected",
    "ingressBytesTransferred": 195332,
    "egressBytesTransferred": 615678
  }
}



AuthorizationKey           :
VirtualNetworkGateway1     : Microsoft.Azure.Commands.Network.Models.PSVirtualNetworkGateway
VirtualNetworkGateway2     :
LocalNetworkGateway2       : Microsoft.Azure.Commands.Network.Models.PSLocalNetworkGateway
Peer                       :
ConnectionType             : IPsec
RoutingWeight              : 0
SharedKey                  : grec42191
EnableBgp                  : False
ConnectionStatus           : Connected
EgressBytesTransferred     : 615678
IngressBytesTransferred    : 195332
ProvisioningState          : Succeeded
VirtualNetworkGateway1Text : "/subscriptions/f7996802-3da7-4a3a-bf02-80fee24df3fb/resourceGroups/arm-rg/providers/Micro
                             soft.Network/virtualNetworkGateways/vpn-gateway"
VirtualNetworkGateway2Text :
LocalNetworkGateway2Text   : "/subscriptions/f7996802-3da7-4a3a-bf02-80fee24df3fb/resourceGroups/arm-rg/providers/Micro
                             soft.Network/localNetworkGateways/asm-vnet-gateway"
PeerText                   :
ResourceGroupName          : arm-rg
Location                   : japaneast
ResourceGuid               : d1a92429-1a95-4ede-84b1-34cf000ee9d8
Tag                        : {}
TagsTable                  :
Name                       : asm-vnet-local
Etag                       : W/"eeb34c1a-1c47-4019-b57d-0671c2194f7a"
Id                         : /subscriptions/f7996802-3da7-4a3a-bf02-80fee24df3fb/resourceGroups/arm-rg/providers/Micros
                             oft.Network/connections/asm-vnet-local

DEBUG: 2:09:59 AM - GetAzureVirtualNetworkGatewayConnectionCommand end processing.
DEBUG: 2:09:59 AM - GetAzureVirtualNetworkGatewayConnectionCommand end processing.
```

Get-AzureRmVirtualNetworkGatewayConnection -Name asm-vnet-local -ResourceGroupName arm-rg -Debug
Get-AzureRmVirtualNetworkGatewayConnection -Name arm-vnet-local -ResourceGroupName Default-Networking -Debug

## ネットワーク周りのコマンド

ネットワーク経路をリスト表示する tracert
netstat ・・・ネットワーク接続状況を確認する
route ・・・ルーティングテーブルを表示・変更する
pathping ・・・ネットワーク経路の品質を調査する
ping ・・・IPパケットが到達するか確認する
nslookup ・・・DNSサーバに名前解決の問い合わせを行
http://www.k-tanaka.net/cmd/tracert.php


[WindowsでICMPを許可（ping応答可能）するにはどうすれば良いですか？ | クラウド・エヌ・インフォメーション](http://www.cloudn-service.com/faq/2165)

[Windows Azure 仮想ネットワーク内のマシンに対するネットワーク分離オプション | Microsoft Azure Japan Team Blog (ブログ)](https://blogs.msdn.microsoft.com/windowsazurej/2014/04/02/windows-azure/)


## 参考
[異なるサブスクリプションで VNET 間接続を試してみる at SE の雑記](http://blog.engineer-memo.com/2014/06/24/%E7%95%B0%E3%81%AA%E3%82%8B%E3%82%B5%E3%83%96%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%97%E3%82%B7%E3%83%A7%E3%83%B3%E3%81%A7-vnet-%E9%96%93%E6%8E%A5%E7%B6%9A%E3%82%92%E8%A9%A6%E3%81%97%E3%81%A6%E3%81%BF/)

[同サブスクリプションでVNET間接続を行う。ポータルでも設定できます。 « 技術的な何か。](http://level69.net/archives/24093)

[Microsoft Azure 仮想ネットワークとプライベートネットワーク接続 〜 仮想ネットワークの作成 〜 | SUMIT.JP](http://sumit.jp/cloud/azure/172/)

[VNET 間接続: 異なるリージョン間での Azure Virtual Network の接続 | Microsoft Azure Japan Team Blog (ブログ)](https://blogs.msdn.microsoft.com/windowsazurej/2014/06/23/vnet-azure-virtual-network/)

## 別件

image作成関連
[Azure 仮想マシンリージョン間の移動 - yanoの日記](http://yano.hatenadiary.jp/entry/20141207/1420127597)
