import endpoints from '../utils/endpoints.js';
import GAxios from '../utils/GAxios.js'

const ROLES = ['ANONYMOUS', 'ARTIST', 'CUSTOMER'];
const CUSTOMER_ACCOUNT_CREDENTIALS = 'pug';
const ARTIST_ACCOUNT_CREDENTIALS = 'rosalia';

class GSecurity {

    constructor(username = 'anonymous', role = 'anonymous', token = ''){
      
      this._username = username;
      
      if (role != undefined && ROLES.includes(role.toUpperCase())){
        this._role = role.toUpperCase();
      }

      this._token = token;
      this._photo = '';
      this._id = '';
      this._firstName = '';

    }

    getRole(){
        return this._role;
    }

    getPhoto() {
        return this._photo;
    }

    getFirstName() {
        return this._firstName;
    }
  
    authenticate(username, password){

        var res = false;

        GAxios.post(endpoints.login, {
            "username": username,
            "password": password
          }).then(response => {

            console.log(response)
        
                if(response.data.artist != undefined){
                    this._username = response.data.artist.user.username;
                    this._role = 'ARTIST';
                    this._id = response.data.artist.id;
                    this._photo = response.data.artist.photo;
                    this._firstName = response.data.artist.user.first_name;
                }else{
                    this._username = response.data.customer.user.username;
                    this._role = 'CUSTOMER';
                    this._id = response.data.customer.id;
                    this._photo = response.data.customer.photo;
                    this._firstName = response.data.customer.user.first_name;
                }

                this._token = response.headers['x-auth'];

                res = true;

              }).catch(ex => {
                console.log(ex);
                res = false;
              });

        return res;
    }

    deauthenticate(){
        this._username = 'anonymous';
        this._role = 'ANONYMOUS';
        this._token = '';
    }

    isAuthenticated(){
        return this._token != undefined && this._token.length > 0;
    }

    isAnonymous(){
        return this._token != undefined && this._token.length <= 0;
    }
    
    hasRole(role){

        if(role != undefined && ROLES.includes(role.toUpperCase())){
            return this._role.toUpperCase() === role.toUpperCase();
        }
        else
            return false;
    }

    setRole(role){
        console.log('Debug only... Remove this method')
        if(role != undefined && ROLES.includes(role.toUpperCase())){
            this._role = role;
            return true;
        }
        else
            return false;
    }

  }
  
  const instance = new GSecurity();
  export default instance;