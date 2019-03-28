import axios from 'axios';

const BASE_URI = 'http://localhost:8000/';
const CORS_HEADERS = {
    'Access-Control-Request-Method' : "GET",
    'Access-Control-Request-Headers' : "Content-Type"
};

export default axios.create({
    baseURL: BASE_URI,
    headers: CORS_HEADERS
});