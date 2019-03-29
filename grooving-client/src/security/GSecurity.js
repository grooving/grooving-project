import endpoints from '../utils/endpoints.js';
import GAxios from '../utils/GAxios.js'

const ROLES = ['ANONYMOUS', 'ARTIST', 'CUSTOMER'];

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

    // Getters

    getUsername(){
        return this._username;
    }

    getId(){
        return this._id;
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

    getToken() {
        return this._token;
    }

    // Other Business Methods

    obtainSavedCredentials(){
        if(localStorage.getItem('token') !== undefined){
            // There are items in session to be restored...

            this._token = localStorage.getItem("token");
            this._username = localStorage.getItem("username");
            this._firstName = localStorage.getItem("firstName");
            this._role = localStorage.getItem("role");
            this._photo = localStorage.getItem("photo");
            this._id = localStorage.getItem("id");
        }
    }

    saveCredentialsInCache(){
        window.localStorage.setItem("username",this.getUsername());
        window.localStorage.setItem("role",this.getRole());
        window.localStorage.setItem("id",this.getId());
        window.localStorage.setItem("photo",this.getPhoto());
        window.localStorage.setItem("firstName",this.getFirstName());
        window.localStorage.setItem("token",this.getToken());
    }

    deleteCredentialsInCache(){
        window.localStorage.clear();
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

                this.saveCredentialsInCache();

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
        this._firstName = '';
        this._id = '';
        this._photo = '';

        this.deleteCredentialsInCache();
    }

    isAuthenticated(){
        return this._token != undefined && this._token.length > 0;
    }

    isAnonymous(){
        return this._token != undefined && this._token.length <= 0;
    }
    
    hasRole(role){

        if(role != undefined && this._role != null && ROLES.includes(role.toUpperCase())){
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