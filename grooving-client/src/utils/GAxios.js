import axios from 'axios';

const BASE_URI = 'http://localhost:8000';
const CORS_HEADERS = {
    'Access-Control-Allow-Origin': "*",
    'Access-Control-Allow-Credentials': 'true',
    'Access-Control-Allow-Methods': "DELETE, GET, OPTIONS, PATCH, POST, PUT",
    'Access-Control-Allow-Headers': "Origin, X-Requested-With, Content-Type, Accept, Authorization, x-auth",

}

export default axios.create({
    baseURL: BASE_URI,
    headers: CORS_HEADERS,
    withCredentials: true,
});