import requests from '../../utils/requests'
import * as ApiUrls from './urls'
import * as ApiRes from './responses'


export function apiProductDetail(id: number): Promise<ApiRes.ApiResProductDetail> {
    return requests.apiGet(ApiUrls.apiUrlProductDetail(id))
}

export function apiProductList(): Promise<ApiRes.ApiResProducts> {
    return requests.apiGet(ApiUrls.apiUrlAllProducts)
}
