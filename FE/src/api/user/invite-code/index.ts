import requests from '../../../utils/requests'
import * as ApiUrls from './urls'
import * as ApiRes from './response'


export function apiInviteCodes(): Promise<ApiRes.ApiResInviteCode[]> {
    return requests.apiGet(ApiUrls.apiUrlInviteCodes)
}

