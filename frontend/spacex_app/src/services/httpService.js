import axios from 'axios';

axios.defaults.baseURL =
  process.env.REACT_APP_API_URL || 'http://127.0.0.1:8000/';

export default {
  get: axios.get,
  post: axios.post,
  put: axios.put,
  delete: axios.delete
};