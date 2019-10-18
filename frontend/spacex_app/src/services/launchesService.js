import http from './httpService'

export function getLaunchesAll(params){
    return http.get('/launches/', { params })
}

export function getLatestLaunche(){
    return http.get('/launches/latest_consumption/')
}

export function updateLaunchesAPI(){
    return http.post('/launches/consumption_api/')
}

export function nextLaunche(){
    return http.post('/launches/next_launche/')
}