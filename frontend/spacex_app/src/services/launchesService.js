import http from './httpService'

export function getLaunchesAll(params){
    return http.get('/launches/', { params })
}

export function getLatestLaunche(params){
    return http.get('/launches/latest/', {params})
}